from django.contrib import admin


from .models import BaseDetail

# Register your models here.
class BaseModify(admin.ModelAdmin):
     
    

    list_display = ('id', 'email', 'phone')
    list_display_links = ('id', 'email',)
  
    

admin.site.register(BaseDetail, BaseModify)