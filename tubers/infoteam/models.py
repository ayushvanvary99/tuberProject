from django.db import models
from datetime import datetime
# Create your models here.

# Create your models here.
class ContactForm(models.Model):
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    subject = models.CharField(default="hi",max_length=100)
    detail_msg= models.TextField(blank=True)
    user_id = models.IntegerField(blank=True, default=1)
    created_date = models.DateTimeField(default=datetime.now , blank=True)
    def __str__(self):
        return self.email

