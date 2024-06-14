from django.shortcuts import get_object_or_404, render
from .models import Youtuber
from django.core.paginator import Paginator
from youtubers.filters import YoutuberFilter 
from basicinfo.models import BaseDetail
# Create your views here. 

def youtubers(request):
   #tubers = Youtuber.objects.all().order_by('created_date')
   #paginator= Paginator(tubers,2)
   #page_number=request.GET.get('page')
   #b tubers=paginator.get_page(page_number)
    # city_search=Youtuber.objects.values_list('city', flat=True).distinct()
    # camera_search=Youtuber.objects.values_list('camera_type', flat=True).distinct()
    # category_search=Youtuber.objects.values_list('category', flat=True).distinct()
     # Preserve filter parameters
    yt_filter= YoutuberFilter(request.GET, queryset=Youtuber.objects.all())
    baseinfo= BaseDetail.objects.all()
    filtered_qs = yt_filter.qs
    filter_params = request.GET.copy()
    if 'page' in filter_params:
        del filter_params['page']
      
    # Apply pagination
    paginator = Paginator(filtered_qs, per_page=2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
  
        
    
    

    # if 'keyword' in request.GET:
    #     keyword = request.GET['keyword']
    #     if keyword:
    #         tubers = tubers.filter(description__icontains=keyword)
    
    # if 'city' in request.GET:
    #     city= request.GET['city']
    #     if city:
    #         tubers=tubers.filter(city__iexact=city)

    # if 'camera_type' in request.GET:
    #     camera_type= request.GET['camera_type']
    #     if camera_type:
    #         tubers=tubers.filter(camera_type__iexact=camera_type)
    
    # if 'category' in request.GET:
    #     category= request.GET['category']
    #     if category:
    #         tubers=tubers.filter(category__iexact=category)
    
    context = {
        'yt_filter': yt_filter,
        'page_obj': page_obj,
        'filter_params': filter_params.urlencode(),
        'baseinfo': baseinfo,
    }
    
    return render(request, 'youtubers/youtubers.html',context=context)

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