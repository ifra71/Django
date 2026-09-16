from django.http import HttpResponse


class MyMiddleware:

    def __init__(self, get_response):
        print("Middleware initialized")
        self.get_response = get_response

    def __call__(self, request):
        print("Request received")
        print("Endpoint:", request.path)

        response = self.get_response(request)

        print("Response received")
        print("Status:", response.status_code)

        return response
