from django.db import models


class Advisor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.URLField(blank=False)

    def __str__(self):
        return self.name
