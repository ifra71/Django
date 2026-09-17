import logging
from datetime import datetime

import redis
from django.conf import settings
from django.http import HttpResponse

logger = logging.getLogger(__name__)

RATE_LIMITS = {
    "gold": 10,
    "silver": 5,
    "bronze": 2,
}


class IPLogging:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = request.META.get("REMOTE_ADDR")
        request_time = datetime.now()
        message = f"IP: {ip_address} | Time: {request_time}"
        logger.info(message)

        response = self.get_response(request)

        return response


class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.redis = redis.Redis(
            host=settings.REDIS_HOST,
            port=int(settings.REDIS_PORT),
            db=int(settings.REDIS_DB),
        )

    def __call__(self, request):
        if request.path == "/login/":
            return self.get_response(request)

        ip = request.META.get("REMOTE_ADDR")
        key = f"requests:ip:{ip}"

        if request.user.is_authenticated:
            limit = RATE_LIMITS.get(request.user.role)

            if limit is None:
                return HttpResponse(
                    "Invalid user role",
                    status=403,
                )
        else:
            limit = 1

        count = self.redis.get(key)

        if count is None:
            self.redis.set(key, 1, ex=60)
            count = 1
        else:
            count = self.redis.incr(key)

        if count > limit:
            return HttpResponse(
                "Too many requests - chill",
                status=429,
            )

        return self.get_response(request)
