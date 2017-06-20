# GuitarTube

https://guitartube.herokuapp.com/

Se ha creado una página web alojada en heroku y creada con el web framework python bottle.
Utiliza varios servicio web llamados: 
Guitar Party (http://www.guitarparty.com/developers/api-docs/getting-started/introduction/#overview )
YouTube (https://www.youtube.com/yt/dev/es/api-resources.html) 
Flickr (https://www.flickr.com/services/api/)

Esta aplicación nos porporciona los siguientes servicios:

- Busca un artista y te muestra una descripción.
- Busca una canción y te muestras detalles de esta.
- Busca un acorde y te muestra información de este, junto a una imagen del acorde.
- Busca imágenes y videos.

-----------------------------------------------------------------------------------------------------------------------------------

Notas: 
Estas aplicacines te devuelve un fichero json. 
La contraseña de acceso debe de estar en la url(se especifica mediante una cabecera o payload) dicha contraseña se almacena en una variable creada en heroku.
Despliegue de una aplicación Python Bottle en Heroku --> http://www.josedomingo.org/pledin/2017/04/despliegue-de-una-aplicacion-python-bottle-en-heroku/
