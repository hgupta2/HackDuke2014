from django.shortcuts import render_to_response
from models import youtube
from models import courses

def home(request):
    """
    Search > Root
    """
    if 'q' in request.GET:
        search_term = request.GET['q']
        youtuberesults = youtube.objects.filter(description__icontains=search_term).order_by('-view_count')[:5]
	courseraresults = courses.objects.filter(description__icontains=search_term).order_by('-rating')[:5]
	return render_to_response('index.html', {'youtube': youtuberesults, 'courses' : courseraresults, 'search_term' : search_term })
    return render_to_response('index.html', {})
