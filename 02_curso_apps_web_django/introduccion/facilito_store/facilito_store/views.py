from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate

from django.contrib.auth.models import User

from forms import RegisterForm

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

def signup_view(request):
	form = RegisterForm(request.POST or None)

	# lectura de datos del formulario
	if request.method == 'POST' and form.is_valid():
		username = form.cleaned_data.get('username')
		email = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password')
		
		# registro en la base de datos de usuario
		user = User.objects.create_user(username, email, password) # el password se guarda encriptado
		
		if user:
			login(request, user)
			messages.success(request, 'Usuario creado exitosamente')
			return redirect('index')

	return render(request, 'auth/register.html',{
		'form':form
	})

