from django.contrib import admin
from .models import Hiretuber
# Register your models here.

class HireTuberDetail(admin.ModelAdmin):


    

    list_display = ('id','first_name','email', 'tuber_name', 'created_date')
    list_display_links = ('first_name', 'id')
    search_fields = ('first_name', 'tuber_name')
    list_filter =('city',)
admin.site.register(Hiretuber,HireTuberDetail)