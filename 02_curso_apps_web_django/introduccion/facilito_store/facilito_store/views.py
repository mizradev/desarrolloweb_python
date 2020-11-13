from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import login, logout
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
			messages.success(request, 'Bienvenido {}'.format(user.username))
			return redirect('index')
		else:
			print(messages)
			messages.success(request, 'Usuario o contraseña no válido')

	return render(request,'auth/login.html',{
		'title':'Login'
	})

def logout_view(request):
	logout(request)
	messages.success(request, 'Sesion cerrada exitosamente!')
	return redirect('login')