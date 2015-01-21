Crear y subir archivos a un repositorio remoto desde Git Bash.

Para crear un proyecto nuevo lo primero que hay que hacer es en línea de
comandos poner las siguientes líneas:

![](media/image1.png)

![](media/image2.png)

Una vez hecho esto, lo que hacemos es crear el nuevo repositorio desde
la página de GitHub

![](media/image3.png)

A continuación agrego la rama master al repositorio remoto de la
siguiente forma:

![](media/image4.png)

Una vez hecho esto, puedo comprobar la URL a la que tengo asignado ese
repositorio de la siguiente forma:

![](media/image5.png)

Luego tengo que hacer el pull y push de la siguiente manera

![](media/image6.png)

![](media/image7.png)

A continuación creamos una nueva rama:

![](media/image8.png)

Como en esta rama no quiero agregar ningún archivo, solo quiero que se
cree con el readme.md, directamente hago el push de dicha rama de la
siguiente forma (no es necesario hacer el pull):

![](media/image9.png)

Ahora creas la rama contenedora de los proyectos de la siguiente forma:

![](media/image10.png)

![](media/image11.png)

Y agregamos todos los ficheros necesarios

![](media/image12.png)

Finalmente hacemos commit para guardar los cambios generados y una vez
hecho eso, hago push para subir esa rama al repositorio remoto

![](media/image13.png)

![](media/image14.png)

En este caso podemos ver cómo están creadas las tres ramas:

![](media/image15.png)

Siendo que la rama projects es la única que contiene los proyectos
(imagen 1), mientras que las ramas develop y master tienen únicamente un
readme.md (imagen 2).

![](media/image16.png)

Imagen1

![](media/image17.png)![](media/image18.png)

Imagen 2
