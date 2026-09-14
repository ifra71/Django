import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class IPLogging():

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):

        ip_address = request.META.get("REMOTE_ADDR")
        request_time = datetime.now
        message = f"IP: {ip_address} | Time: {request_time} "  
        logger.info(message)

        response = self.get_response(request)
        return response




