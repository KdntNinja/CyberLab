from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Room


def room_list(request: HttpRequest) -> HttpResponse:
    rooms = Room.objects.filter(enabled=True)

    return render(
        request,
        "rooms/room_list.html",
        {"rooms": rooms},
    )


def room_detail(request: HttpRequest, slug: str) -> HttpResponse:
    room = get_object_or_404(
        Room,
        slug=slug,
        enabled=True,
    )

    return render(
        request,
        "rooms/room_detail.html",
        {"room": room},
    )
