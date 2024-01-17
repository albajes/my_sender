import requests
from django.http import HttpResponse
from rest_framework import status

from service_3.settings import services


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        request.token = request.COOKIES.get('access')

        if request.token is None:
            return HttpResponse('Unauthorized', status=status.HTTP_401_UNAUTHORIZED)
        response2 = requests.post(services.service_1_verify, json={'token': request.token})

        if response2.status_code == 401:
            return HttpResponse('Access closed', status=status.HTTP_401_UNAUTHORIZED)

        if view_kwargs['room_name'] != response2.json()['username']:
            return HttpResponse('Access closed', status=status.HTTP_401_UNAUTHORIZED)
