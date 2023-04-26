from django.shortcuts import render

from tvshows.models import TVShow


def top_tvshows(request):
    tvshows = TVShow.objects.all()
    context = {
        'tvshows': tvshows
    }
    return render(request, template_name="core/tvshows.html", context=context)
