# importamos el modulo de Flask
from flask import Flask
from flask import render_template

# Inicializa Flask
app = Flask(__name__)

# ruta del index
@app.route('/')
def index():
    #return "<h1>Hola mundo desde el server de Flask</h1>"
    return render_template('index.html')# carga el html del templates/

# servidor flask corriendo en el puerto 9000 y modo debugin
if __name__ == '__main__':
    app.run(debug=True, port=9000)

