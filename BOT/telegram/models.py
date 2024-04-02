from django.db import models


# Create your models here.
class Friend(models.Model):
    def __str__(self):
        return str(self.name)

    name = models.CharField(max_length=200)
    link = models.URLField()
    count = models.IntegerField(default=0)
