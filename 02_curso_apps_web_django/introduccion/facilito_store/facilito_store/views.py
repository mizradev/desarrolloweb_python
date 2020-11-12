from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	#return HttpResponse('Hola desde views.py')
	return render(request,'index.html',{
		#context
	})