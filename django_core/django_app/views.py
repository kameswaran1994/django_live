from django.shortcuts import render

def index(request):
    return render(request, 'django_app/index.html')

# Create your views here.
