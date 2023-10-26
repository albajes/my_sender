import requests
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def index(request, room_name):

    token = request.COOKIES.get('access')
    if token is None:
        return Response('Access closed', status=status.HTTP_401_UNAUTHORIZED)

    response2 = requests.post('http://service1:8000/verify', json={'token': token})

    if response2.status_code == 401:
        return Response('Access closed', status=status.HTTP_401_UNAUTHORIZED)

    if room_name != response2.json()['username']:
        return Response('Access closed', status=status.HTTP_401_UNAUTHORIZED)
    else:
        response1 = requests.get('http://service2:8090/room/')

        try:
            room = [k for k in response1.json() if k['receiver'] == room_name][0]['id']
        except IndexError:
            room = 0

        response2 = requests.get('http://service2:8090/sms_list/')

        list_messages = []
        try:
            list_messages = [k for k in response2.json() if k['room'] == room]
        except NameError:
            pass

        return render(request, 'my_sender/index.html', {'room_name': room_name, 'messages': list_messages})
