from django.db import models


class TVShow(models.Model):
    poster_image = models.URLField()
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    rating = models.CharField(max_length=10)

    def __repr__(self):
        return f"{self.title} ({self.year})"
