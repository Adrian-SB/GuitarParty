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


#Busca el nombre del artista,muestra el nombre completo y la biografía.

@route('/artista/resultado_artista', method="post")
def artista():
	artista = request.forms.get('artista')
	r=requests.get(url+'artists/?query='+artista,headers=headers)

	lis_nombrecompleto = []
	lis_biografia = []

	if r.status_code == 200:
		bus_artista = json.loads(r.text)
	   	for art in bus_artista.get("objects"):
	   		lis_nombrecompleto.append(art["name"])
	   		lis_biografia.append(art["bio"])

	return template("result_artista.tpl", lis_nombrecompleto=lis_nombrecompleto, lis_biografia=lis_biografia)

#Busqueda por canciones

@route('/cancion/bus_cancion', method="post")
def cancion():
	cancion= request.forms.get('cancion')
	r=requests.get(url+'songs/?query='+cancion,headers=headers)
	
	lis_titulo = []
	lis_instrumento = []
	lis_tipo = []
	lis_nombreautor = []

	if r.status_code == 200:
		 
		bus_cancion = json.loads(r.text)
		
		for t in bus_cancion["objects"]:
			lis_titulo.append(t["title"])
			lis_tipo.append(t["authors"][0]["types"])
			lis_instrumento.append(t["chords"][0]["instrument"]["name"])
			lis_nombreautor.append(t["authors"][0]["name"])
			

	return template("result_cancion.tpl",lis_titulo=lis_titulo,lis_tipo=lis_tipo,lis_instrumento=lis_instrumento, lis_nombreautor=lis_nombreautor)

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

#Muestra las fiestas

@route('/listado', method="get")
def listado():

	r=requests.get(url+'parties/',headers=headers)

	lis_tif = []
	lis_descf = []
	lis_url = []

	if r.status_code == 200:
		bus_listado = json.loads(r.text)
			
		for l in bus_listado["objects"]:
			lis_tif.append(l["title"])
			lis_descf.append(l["description"])
			lis_url.append(l["human_uri"])

		return template("result_listado.tpl", lis_tif=lis_tif,lis_descf=lis_descf,lis_url=lis_url)


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')


run(host='0.0.0.0',port=argv[1])

