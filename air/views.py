from django.shortcuts import render
from .models import Projects

def home(request):
    data = Projects.objects.all().order_by('-id')[:10]
    return render(request, 'home.html', {'data': data})
# Create your views here.
