from django.shortcuts import render
from django.apps import apps


def index(request):
    app_config = apps.get_app_config('article')
    app_name = app_config.name
    return render(
        request,
        "article/index.html",
        context={
            'name': app_name,
        }
    )
