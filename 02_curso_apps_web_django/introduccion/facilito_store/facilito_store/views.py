from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import login 
from django.contrib.auth import authenticate

def index(request):
	#return HttpResponse('Hola desde views.py')
	return render(request,'index.html',{
		#context
		'message':'Mensaje desde la vista',
		'title': 'Index',
		'products': [
			{
				'title': 'Playera' ,
				'price': 5,
				'stock': True
			},
			{
				'title': 'Camisa' ,
				'price': 6,
				'stock': True
			},
			{
				'title': 'Mochila' ,
				'price': 10,
				'stock': False
			},
		] 
	})


def login_view(request):
	
	if request.method == 'POST':
		username = request.POST.get('username') #diccionario
		password = request.POST.get('password') #diccionario/None
		
		user = authenticate(username=username, password=password) # /None

		if user != None:
			login(request, user)
			return redirect('index')

	return render(request,'auth/login.html',{
		'title':'Login'
	})