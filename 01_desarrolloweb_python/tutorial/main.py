# importamos el modulo de Flask
from flask import Flask
from flask import render_template, request

# Inicializa Flask
app = Flask(__name__)

#hooks o callbacks en flask en peticiones al server
@app.before_request # antes del request
def before_request():
    print('Antes del request')

@app.after_request # despues del request
def after_request(response):# response obligatorio es lo que devuelve las rutas descritas
    print('Despues del request')
    return response

# ruta del index
@app.route('/')
def index():
    #return "<h1>Hola mundo desde el server de Flask</h1>"
    name = 'Jorge Mizrain Aguilar'
    course = 'Python Web'
    is_premium = False
    courses = ['Python', 'Ruby', 'Java', 'Elixir']
    return render_template('index.html', username=name, 
    									course_name=course,
    									is_premium=is_premium,
    									courses=courses)# carga el html del templates/


@app.route('/about')
def about():
    return render_template('about.html')


# ruta con parametros
#@app.route('/usuario/<username>')
#@app.route('/usuario/<last_name>/<name>')
@app.route('/usuario/<last_name>/<name>/<int:age>')
def usuario(name, last_name, age):
    return 'Hola '+name + last_name + ' ' + str(age)
    
#lectura de querys
@app.route('/datos')  # /datos?nombre=jorge&curso=python web
def datos():
    nombre = request.args.get('nombre') # diccionario
    curso = request.args.get('curso') # diccionario
    return 'Listado de datos: '+nombre+ ' - curso: '+curso


# servidor flask corriendo en el puerto 9000 y modo debugin
if __name__ == '__main__':
    app.run(debug=True, port=9000)

