from django.db import models

# Create your models here.


class SocialMedia(models.Model):
    telegram = models.CharField(max_length=30)
    instagram = models.CharField(max_length=15)
    facebook = models.CharField(max_length=18)
