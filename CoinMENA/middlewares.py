import os
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from constants import CUSTOM_TOKEN_HEADER, CUSTOM_TOKEN


class VerifyTokenMiddleware(MiddlewareMixin):
    AUTHENTICATED_URLS = ['/api/v1']

    def __init__(self, get_response):
        super().__init__(get_response)
        self.get_response = get_response
        self.custom_token = CUSTOM_TOKEN

    def __call__(self, request):
        if list(filter(request.path.startswith, self.AUTHENTICATED_URLS)):
            if not request.headers.__contains__(CUSTOM_TOKEN_HEADER):
                return HttpResponse('Access Denied, Unauthorized Access', status=401)
            custom_token = request.headers.get(CUSTOM_TOKEN_HEADER)

            if custom_token != self.custom_token:
                return HttpResponse('Access Denied, Invalid API Token', status=401)

        response = self.get_response(request)
        return response
