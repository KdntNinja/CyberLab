from django.urls import path

from . import views

urlpatterns = [
    path("", views.room_list, name="room-list"),
    path("<slug:slug>/", views.room_detail, name="room-detail"),
]
