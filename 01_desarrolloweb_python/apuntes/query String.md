# El Query String

Dentro del protocolo HTTP podemos encontrar diferentes métodos (verbos) con los cuales podemos realizar diferentes tipos de peticiones. El método más utilizado sin duda es el método GET, método cual nos permite obtener un recurso por parte del servidor, ya sea una página web, un archivo txt, un gif etc...

Siempre que nosotros ingresamos a una sitio web, por ejemplo, www.google.com utilizando nuestro navegador la petición al servidor se hará atraves del método GET.

Algo interesante de este método es que podemos enviar información al servidor de tal forma que seamos más precisos en el recurso que deseamos obtener. La información la enviaremos atraves de la URL, en una sección denominada Query String. Veamos un ejemplo.

Si nosotros realizamos una petición a la ruta

`/users`

Espereamos que la respuesta (ya sea una página web, un objeto JSON o XML) tenga relación con usuarios. Si queremos (y el servidor lo permite) podemos enviar información extra.

`/users?order=true`

En este caso realizamos la petición indicando que el servidor nos debe retornar los usuarios de forma ordenada. Todo lo que se encuentre después del signo de interrogación (?) lo conoceremos como Query String y posee la siguiente estructura:

__ llave (nombre del parametro) , signo igual (=) y valor. __

