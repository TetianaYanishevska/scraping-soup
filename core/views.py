from django.shortcuts import render
from services import ScrapTVShowsService
from tvshows.models import TVShow


def index(request):
    service = ScrapTVShowsService()
    top_tvshows = service.get_top_tvshows()

    for top_tvshow in top_tvshows:
        tvshow = (
            TVShow.objects
            .filter(
                poster_image=top_tvshow.get('poster_image'),
                title=top_tvshow.get('title'),
                year=top_tvshow.get('year')
            )
            .first()
        )
        if tvshow:
            tvshow.poster_image = top_tvshow.get('poster_image')
            tvshow.rating = top_tvshow.get('rating')
            tvshow.save()
        else:
            tvshow = TVShow(**top_tvshow)
            tvshow.save()

    return render(request, 'core/index.html')
