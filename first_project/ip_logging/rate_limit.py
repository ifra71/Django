import redis
from django.conf import settings
from django.http import HttpResponse


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

        if request.user.is_authenticated:

            role_limits = {
                "gold": 10,
                "silver": 5,
                "bronze": 2,
            }

            limit = role_limits.get(request.user.role, 2)

            key = f"requests:user:{request.user.id}"

        else:

            limit = 1

            ip = request.META.get("REMOTE_ADDR")
            key = f"requests:ip:{ip}"

        count = self.redis.get(key)

        if count is None:
            self.redis.set(key, 1, ex=60)
            count = 1

        else:
            count = self.redis.incr(key)

        if count > limit:
            return HttpResponse("Too many requests-chill", status=429)

        return self.get_response(request)
