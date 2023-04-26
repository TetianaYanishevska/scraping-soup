from django.urls import path
from tvshows.views import top_tvshows


urlpatterns = [
   path('tvshows/', top_tvshows, name='tvshows')
]
