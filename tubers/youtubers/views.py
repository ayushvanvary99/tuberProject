from django.shortcuts import get_object_or_404, render
from .models import Youtuber
from django.core.paginator import Paginator
# Create your views here.

def youtubers(request):
    tubers = Youtuber.objects.all().order_by('created_date')
    paginator= Paginator(tubers,2)
    page_number=request.GET.get('page')
    tubers=paginator.get_page(page_number)
    city_search=Youtuber.objects.values_list('city', flat=True).distinct()
    camera_search=Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search=Youtuber.objects.values_list('category', flat=True).distinct()
  

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(description__icontains=keyword)
    
    if 'city' in request.GET:
        city= request.GET['city']
        if city:
            tubers=tubers.filter(city__iexact=city)

    if 'camera_type' in request.GET:
        camera_type= request.GET['camera_type']
        if camera_type:
            tubers=tubers.filter(camera_type__iexact=camera_type)
    
    if 'category' in request.GET:
        category= request.GET['category']
        if category:
            tubers=tubers.filter(category__iexact=category)
    

    data ={
        'tubers': tubers,
        # 'ServiceDatafinal':ServiceDatafinal,
        'city_search': city_search,
        'camera_search':  camera_search,
        'category_search': category_search,
    }
    return render(request, 'youtubers/youtubers.html',data)

def youtubers_detail(request, id):
    tuber = get_object_or_404(Youtuber, pk=id)
    data={
        'tuber': tuber
        
    }
    return render(request, 'youtubers/youtuber_detail.html',data)

def search(request):
    tubers = Youtuber.objects.order_by('-created_date')
    city_search=Youtuber.objects.values_list('city', flat=True).distinct()
    camera_search=Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search=Youtuber.objects.values_list('category', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(description__icontains=keyword)
    
    if 'city' in request.GET:
        city= request.GET['city']
        if city:
            tubers=tubers.filter(city__iexact=city)

    if 'camera_type' in request.GET:
        camera_type= request.GET['camera_type']
        if camera_type:
            tubers=tubers.filter(camera_type__iexact=camera_type)
    
    if 'category' in request.GET:
        category= request.GET['category']
        if category:
            tubers=tubers.filter(category__iexact=category)
    

    data = {
        'tubers': tubers,
        'city_search': city_search,
        'camera_search':  camera_search,
        'category_search': category_search,
    }

    return render(request, 'youtubers/search.html',data)