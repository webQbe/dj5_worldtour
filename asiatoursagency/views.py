from django.shortcuts import render
from .models import Tour
#from django.http import HttpResponse

# Create your views here.
def index(request):
    tours = Tour.objects.all()
    context = {'tours':tours}
    return render(request, 'tours/index.html', context)
    #return HttpResponse("Asia Tours Agency")