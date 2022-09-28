from django.shortcuts import render
from .models import Slider, Team, Pargraph
from youtubers.models import Youtuber
from basicinfo.models import BaseDetail
# Create your views here.

def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    baseinfo= BaseDetail.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    all_youtubers = Youtuber.objects.all()
    data ={
        'sliders': sliders,
        'teams': teams,
        'baseinfo': baseinfo,
        'featured_youtubers': featured_youtubers,
        'all_youtubers': all_youtubers,
    }
    return render(request,'webpages/home.html', data)

def about(request):
    paras = Pargraph.objects.all()

    teams = Team.objects.all()
    data ={
        
        'teams': teams,
        'paras': paras,
       
    }
    return render(request,'webpages/about.html',data)

def services(request):
    return render(request,'webpages/services.html')

def contact(request):
     return render(request,'webpages/contact.html')
