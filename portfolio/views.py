from django.shortcuts import render
from portfolio.models import Project

# Create your views here.
def Home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})
