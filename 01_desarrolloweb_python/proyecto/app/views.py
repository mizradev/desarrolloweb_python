from flask import Blueprint
from flask import render_template, request

from .forms import LoginForm

page = Blueprint('page', __name__)

#Error 404
@page.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

@page.route('/login', methods=['GET', 'POST'])
def login():
    #obtenemos los datos del login al hacer submit
    form = LoginForm(request.form)
    #Validamos la request por el metodo POST
    if request.method == 'POST':
        # se muestra en consola la informacion del login
        print(form.username.data)
        print(form.password.data)
        print('Nueva sesion creada')
    
    return render_template('auth/login.html', title='Login', form=form)

@page.route('/')
def index():
    return render_template('index.html', title='INDEX')