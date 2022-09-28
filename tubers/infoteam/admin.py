from django.contrib import admin
from .models import ContactForm
# Register your models here.

class ContactInfo(admin.ModelAdmin):

    list_display = ('id','email', 'fullname', 'created_date')
    list_display_links = ('fullname', 'id')
    
    
admin.site.register(ContactForm,ContactInfo)