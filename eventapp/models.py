from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    participants = models.IntegerField()
    date = models.DateField()
    time = models.CharField(max_length=100)  # Assuming time is a string like '6PM-9PM'
    lat = models.FloatField()
    lng = models.FloatField()
    imageUrl = models.URLField(max_length=1024, blank=True, null=True)
    videoUrl = models.URLField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return self.name