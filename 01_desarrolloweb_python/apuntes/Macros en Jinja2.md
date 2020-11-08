# Macros en Jinja2

Podemos ver los macros como funciones de Python. Haremos uso de ellos cuando tengamos la necesidad de reutilizar lógica de programación así como etiquetas HTML.

Para definir una macro seguiremos la siguiente estructura.

'''

{% macro nombre_macro (parametros) %}
  Etiquetas HTML y Códigp Python
{% endmacro %}

'''

> Ejemplo.

'''
{% macro suma (valor1, valor2) %}
    <p>La suma del valor {{ valor1 }} + más el valor {{ valor2 }} es : 
       <strong> {{ valor1 + valor2 }} </strong>
{% endmacro %}
'''

> Es recomendable tener un macro por archivo. 

Por convención el nombre de los archivos macros comenzarán con un guión bajo **(_)**.
Para hacer uso de un macro dentro de nuestra plantilla será obligatorio realizar un import.

'''

{% from "_macro.html" import suma %}
<div class="container">
    {{ suma(val1, val2) }}
</div>

'''