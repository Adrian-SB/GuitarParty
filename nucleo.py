from bottle import Bottle,route,run,request,template

headers={'Guitarparty-Api-Key': '6115b4a078d150136759b6e1b85dfba83b68190b'}
url='http://api.guitarparty.com/v2/'

@route('/inicio')
def inicio():
	return template('header.tpl')

#Busca el nombre dle artista un le muestra el nombre completo y la bigrafia.

@route('/inicio/artista', method="post")
def artista():
	artista = request.forms.get('artista')
	r=requests.get(url+'artists/?query='+artista,headers=headers)
	if r.status_code == 200:
	    text=r.json()  

	    nombrecompleto =  text["objects"][0]["name"]
	    biografia = text["objects"][0]["bio"]

	return template("resultadoartista.tpl", artista=artista, nombrecompleto=nombrecompleto, biografia=biografia)

#Busqueda por canciones

@route('/inicio/canciones', method="post")
def canciones():
	cancion= reques.forms.get('cancion')
	r=requests.get(url+'songs/?query='+cancion,headers=headers)
	if r.status_code == 200:
	    text=r.json()

	    titulo = text["objects"][0]["title"]
	    codigo = text["objects"][0]["uri"]
	    instrumento =  text["objects"][0]["chords"][1]["instrument"]["name"]
	    acorde = text["objects"][0]["chords"][1]["name"] 
	    fotoacorde = text["objects"][0]["chords"][1]["image_url"]
	    tipo = text["objects"][0]["authors"][1]["types"]
	    nombreautor = text["objects"][0]["authors"][1]["name"]
	    autorcodigo = text["objects"][0]["authors"][1]["uri"]

	return template("resultadocancion.tpl", cancion=cancion, titulo=titulo, codigo=codigo, instrumento=instrumento,acorde=acorde, fotoacorde=fotoacorde, tipo=tipo, nombreautor=nombreautor, autorcodigo=autorcodigo)

#Muestra informacion sobre los acordes

@route('inicio/acordes', method="post")
def acorde():
	acorde = reques.forms.get('acorde')
	r=requests.get(url+'chords/?query='+acorde,headers=headers)
	if r.status_code == 200:
	    text=r.json()

	    nombreacorde = text["objects"][0]["name"]
	    instrumento = text["objects"][0]["instrument"]["name"]
	    afinacion = text["objects"][0]["instrument"]["tuning"]
	    imagen = text["objects"][0]["image_url"]

	return template("resultadocancion.tpl", acorde=acorde, nombreacorde=nombreacorde, instrumento=instrumento, afinacion=afinacion,imagen=imagen)


#Crear fiestas - Revisar

@route('inicio/crearfiestas', method="post")
def crearfiesta():

	titulo= reques.forms.get('titulo')
	descripcion= reques.forms.get('descripcion')
	codcancion= reques.forms.get('codcancion')

	fiesta={"title": "titulo","description": "descripcion","current_song": codcancion}

	r=requests.post(url+'parties/', data=fiesta ,headers=headers)
	if r.status_code != 201:
		return template("resultadofiestas.tpl") 

#Muestra las fiestas que han sido creadas

@route('inicio/fiestas', method="post")
def listafiesta():
	r=requests.get(url+'parties/',headers=headers)
	if r.status_code == 200:
	    text=r.json()

	    titulo = text["objects"][0]["title"]
	    descripcion = text["objects"][0]["description"]
	    codcancion = text["objects"][0]["current_song"]
	    codacorde = text["objects"][0]["short_code"]
	    codusuario = text["objects"][0]["human_uri"]

	return template("resultadofiestas.tpl", titulo=titulo, descripcion=descripcion, codcancion=codcancion, codacorde=codacorde, codusuario=codusuario) 

run(host='0.0.0.0', port=8080)

