import requests
from django.shortcuts import render
from rest_framework.views import APIView

from service_3.settings import services


class PageView(APIView):
    def get(self, request, room_name):
        response1 = requests.get(services.service_2_room, cookies={'access': request.token})
        try:
            room = [k for k in response1.json() if k['receiver'] == room_name][0]['id']
        except IndexError:
            room = 0

        response2 = requests.get(services.service_2_sms_list, cookies={'access': request.token})
        list_messages = []
        try:
            list_messages = [k for k in response2.json() if k['room'] == room]
        except NameError:
            pass

        return render(request, 'my_sender/index.html', {'room_name': room_name, 'messages': list_messages})
