import django_filters
from youtubers.models import Youtuber

class YoutuberFilter(django_filters.FilterSet):
    
  

    class Meta:
        model= Youtuber
        fields= {'city':['icontains'],
                 'camera_type':['exact'],
                 'category':['exact']
        }
        
   
    
  
    