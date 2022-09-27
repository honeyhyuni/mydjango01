from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from app.models import Post


def index(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    # qs = [{"id": 1, "title": "post 1"}, {"id": 2, "title": "post 2"}]
    return render(
        request,
        "app/index.html",
        {"post_list": qs},
    )


# Create your views here.
