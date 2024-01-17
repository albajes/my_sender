from django.urls import path
from .views import PageView

urlpatterns = [
    path('<str:room_name>', PageView.as_view(), name='index')
]

