from django.db import models
from django.core.validators import FileExtensionValidator


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    participants = models.IntegerField()
    date = models.DateField()
    time = models.CharField(max_length=100)  # Assuming time is a string like '6PM-9PM'
    lat = models.FloatField()
    lng = models.FloatField()

    # Replace imageUrl with this
    image = models.ImageField(
        upload_to='events/images/', 
        blank=True, 
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    )
    # Replace videoUrl with this
    video = models.FileField(
        upload_to='events/videos/', 
        blank=True, 
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'avi', 'mkv'])]
    )


    # imageUrl = models.URLField(max_length=1024, blank=True, null=True)
    # videoUrl = models.URLField(max_length=1024, blank=True, null=True)

    # image = models.ImageField(upload_to='images/')  # Assuming you want to store images as well
    # video = models.FileField(upload_to='videos/')   # Directory where the videos will be stored
    
    # imageUrl = models.URLField(max_length=1024, blank=True, null=True)
    # videoUrl = models.URLField(max_length=1024, blank=True, null=True)


    # # Replace imageUrl with this
    # image = models.ImageField(
    #     upload_to='events/images/', 
    #     blank=True, 
    #     null=True,
    #     validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    # )
    # # Replace videoUrl with this
    # video = models.FileField(
    #     upload_to='events/videos/', 
    #     blank=True, 
    #     null=True,
    #     validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'avi', 'mkv'])]
    # )

    def __str__(self):
        return self.name