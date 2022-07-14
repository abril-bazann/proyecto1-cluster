# ProyectoCoder/AppCoder
## Funcionalidad y pruebas del Proyecto
Para probarlo lo primero que se debe hacer es:
1. En la consola de VSC (Command Prompt), colocar: "python manage.py runserver" para que el servidor empiece a correr el proyecto. 

## Creación de formularios (api form Django)
 Un formulario es una vista que permite poder agregar datos a nuestro model directamente desde nuestra web. El archivo html correspondiente recibe la información que le enviamos por medio de la vista y su template asociado. Al apretar un botón (Submit) esa información viaja por medio de un método GET o POST y llega al servidor, donde esos datos se manipulan.

Los archivos dentro de AppCoder que son muy necesarios para entender el Proyecto son:
 - El archivo models.py, encontrados allí los modelos.
 - El archivo forms.py, con las clases para crear el o los formularios.
 - El archivo views.py, donde se pueden ver las vistas.
 - El archivo urls.py, en el cual se linkean esas mismas vistas.
 - El archivo admin.py, en donde se podrá linkear el modelo correspondiente para que se muestre en Django administration.
 - Y las templates html, en donde se mostrarán las vistas. 

Se crea un modelo en models.py. Luego, se actualiza forms.py añadiendo la clase correspondiente al modelo para que se cree un formulario. Después, se crean sus respectivas vistas en views.py, en caso de ejemplo, para el modelo Album, se agregaron, vistas album_formulario, busqueda_album y buscar_album. Una vez realizado esto, se deben de crear los archivos html donde se renderizan estas clases en su orden. También, para que todo funcione, se necesita agregar los paths a urls.py de aquellas views para que se puedan acceder desde la web, una vez el servidor esté corriendo. No se debe olvidar linkear todos los modelos, junto con sus formularios, que sean necesarios con un import al principio del archivo views.py ya que de eso depende de que las vistas funcionen correctamente. 

Recibimos en el html, la etiqueta form para crear el formulario, de esa manera se utiliza menos código html. Luego, podemos ver la carga de datos en views.py, en el caso particular de album_formulario nos encontramos con tres campos: nombre_album, creador y año, que reciben información externa mediante el formulario. Se puede observar que es requerido mediante el método POST dentro de un if desde el formulario creado anteriormente (Album_form) dentro de forms.py. Si la información requerida es válida, cumple con los requisitos del segundo if, en donde se crea un diccionario con esa misma información retirando lo innecesario con "info= form.cleaned_data". Luego de que los datos se coloquen en las variables correspondientes, se llama a la clase Album con sus tres atributos: albums=Album(nombre_album=nombre_album, creador=creador, año=año), guardándolos y renderizando hacia el archivo html inicio. Sino, se crea un formulario vacío, se renderiza y se manda como un diccionario para que lo pueda usar la template html.

 Si nos concentramos en la etiqueta form podemos ver:
1) Action, que es el nombre de la url.
2) Method, el cual es la forma en la que se envían los datos.
3) Input, aquellos espacios para escribir información.
4) Input Submit, que sería el botón que envía la información.

En el caso en el cual se necesita el token de validación que nos exige Django (csrf_token), es aquel donde se utiliza el método POST. Al contrario, si se utiliza el método GET, no se debe utilizar. 
De esta forma podemos guardar en la base de datos los datos recibidos por medio del form. 

_Es muy importante modificar el archivo views.py importanto de esta manera la api forms:
from AppCoder.forms import album_formulario_

## Formulario para búsqueda
Si queremos saber si tenemos el nombre de un album que corresponde a una determinada lista de albums, hay dos alternativas, o existe o no existe.
Lo que se necesitó es:

1- Una vista busqueda_album(request)

2- El url registrado en urls.py

3- La template busqueda_album.html

4- Y la vista buscar (también registrada en urls.py)

Primero, en busqueda_album(request), se renderiza al archivo busqueda_album.html para que muestre el formulario de busqueda. Después, dentro de la vista buscar, utilizando el método GET, buscamos el album guardándolo dentro de una variable denominada "nombre_album". En la variable "albums", notamos una búsqueda por filtros en la base de datos con objects.filter dentro de la clase Album. Luego, se renderiza en un archivo nuevo, resultados_busqueda_album.html, y se muestra el resultado. Dentro de la template de respuesta, podemos ver una sentencia if y dentro, un for, donde se encuentra la lista con el nombre del album y su creador de manera en la que se requirió.  Sino, se encuentra un error en lo requerido, devolviendo otro diccionario: {"error": "No se ingresó ninguna comisión"}.

 En los archivos html, si nos enfocamos en los formularios, están realizados con Django, el cual permite importar formularios desde este mismo framework. También se encuentran los errores del formulario por si algo sale mal, es decir, si no se encuentra lo que se busca, si no completó algún campo, etc. 










