#-*-coding:utf-8-*-
from bottle import *
import requests
import os
from sys import argv
import json

key = os.environ["key"]

headers={'Guitarparty-Api-Key': key }
url='http://api.guitarparty.com/v2/'

#Páginas

@route('/')
def inicio():
	return template('inicio.tpl')

@route('/artista')
def in_artista():
	return template('bus_artista.tpl')

@route('/cancion')
def in_cacnion():
	return template('bus_cancion.tpl')

@route('/acorde')
def inicio_acorde():
	return template('bus_acorde.tpl')

@route('/fiesta')
def in_fiesta():
	return template('form_fiesta.tpl')

@route('/fiesta/crea_crearfiestas/ok')
def in_mensaje():
	return template('fiesta_ok.tpl')

@route('/mensaje')
def in_mensaje():
	return template('form_mensaje.tpl')

@route('/mensaje/enviar/ok')
def in_mensaje():
	return template('mensaje_ok.tpl')


#Busca el nombre del artista un le muestra el nombre completo y la biografía.

@route('/artista/resultado_artista', method="post")
def artista():
	artista = request.forms.get('artista')
	r=requests.get(url+'artists/?query='+artista,headers=headers)
	if r.status_code == 200:
	    text=r.json()  

	    nombrecompleto =  text["objects"][0]["name"]
	    biografia = text["objects"][0]["bio"]

	return template("result_artista.tpl", artista=artista, nombrecompleto=nombrecompleto, biografia=biografia)

#Busqueda por canciones

@route('/cancion/bus_cancion', method="post")
def cancion():
	cancion= request.forms.get('cancion')
	r=requests.get(url+'songs/?query='+cancion,headers=headers)
	
	lis_titulo = []
	lis_instrumento = []
	lis_acorde = []
	lis_fotoacorde = []
	lis_tipo = []
	lis_nombreautor = []

	if r.status_code == 200:
	    text=r.json()
	    canciones = r4.text
		busqueda_cancion = json.loads(canciones)

	    for titulos in bus_cancion["objects"]:
	    	lis_titulo.append(titulos["title"])

	    for instrumentos in bus_cancion["objects"]["chords"]["instrument"]:
	    	lis_instrumento.append(instrumentos["name"])

	    for acordes in bus_cancion["objects"]["chords"]:
	    	lis_acorde.append(acordes["name"])

	    for fotos in bus_cancion["objects"]["chords"]:
	    	lis_fotoacorde.append(fotos["image_url"])

	    for tipos in bus_cancion["objects"]["authors"]:
	    	lis_tipo.append(tipos["types"])

	    for nombresautores in bus_cancion["objects"]["authors"]:
	    	lis_nombreautor.append(nombresautores["name"])


	return template("result_cancion.tpl",lis_titulo=lis_titulo,lis_instrumento=lis_instrumento,lis_acorde=lis_acorde, lis_fotoacorde=lis_fotoacorde, lis_nombreautor=lis_nombreautor)

#Muestra informacion sobre los acordes

@route('/acorde/bus_acorde', method="post")
def acorde():
	acorde = request.forms.get('acorde')
	r=requests.get(url+'chords/?query='+acorde,headers=headers)
	if r.status_code == 200:
	    text=r.json()

	    nombreacorde = text["objects"][0]["name"]
	    instrumento = text["objects"][0]["instrument"]["name"]
	    afinacion = text["objects"][0]["instrument"]["tuning"]
	    imagen = text["objects"][0]["image_url"]

	return template("result_acorde.tpl", acorde=acorde, nombreacorde=nombreacorde, instrumento=instrumento, afinacion=afinacion,imagen=imagen)


#Crear fiestas 

@route('/fiesta/crea_crearfiestas', method="post")
def crearfiesta():

	titulo= request.forms.get('titulo')
	descripcion= request.forms.get('descripcion')
	codcancion= request.forms.get('codcancion')

	fiesta={"title": "titulo","description": "descripcion","current_song": codcancion}

	r=requests.post(url+'parties/', data=fiesta ,headers=headers)
	if r.status_code != 201:
		return redirect("/fiesta/crea_crearfiestas/ok") 
	    

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')


run(host='0.0.0.0',port=argv[1])

