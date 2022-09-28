from django.contrib import admin
from .models import Slider, Team, Pargraph
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img/ src ="{}"width="40">'.format(object.photo.url))

    list_display = ('id', 'myphoto','first_name','role', 'create_date')
    list_display_links = ('first_name', 'id')
    search_fields = ('first_name', 'role')
    list_filter =('role',)

class SliderDetail(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img/ src ="{}"width="50">'.format(object.photo.url))

    list_display = ('id', 'headline','myphoto','button_text', 'create_date')
    list_display_links = ('headline', 'id')
   

admin.site.register(Slider, SliderDetail)
admin.site.register(Team, TeamAdmin)
admin.site.register(Pargraph)