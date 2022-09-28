from django.db import models

# Create your models here.
class BaseDetail(models.Model):
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    insta_Link = models.CharField(max_length=255)
    fb_Link = models.CharField(max_length=255)
    twitter_Link = models.CharField(max_length=255)
    linkedin_Link = models.CharField(max_length=255)


    
