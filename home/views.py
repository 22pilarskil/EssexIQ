from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homeView(request):
	 print("HomeView")
	 return render(request, 'home.html', {"submitted": False})
