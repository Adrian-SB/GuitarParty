#-*-coding:utf-8-*-
from bottle import *
import requests
import os
from sys import argv
import json


key = os.environ["key"]
key2= os.environ["key"]
key3 = os.environ["key"]



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

@route('/videos')
def in_video():
	return template('bus_video.tpl')

@route('/fotos')
def in_fotos():
	return template('bus_fotos.tpl')


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


#Busqueda de videos

@route('/videos/bus_videos', method="post")
def video():
	maxResults = request.forms.get('maxResults')
	q=request.forms.get('q')
	order = request.forms.get('order')

	lis_ids = []
	lis_videos = []
	desc_videos = []
	canales_videos = []
	payload = {"part":"snippet","ForMine":"true","maxResults":maxResults,"q":q,"order":order,"type":"video","key":key2}
	rv = requests.get('https://www.googleapis.com/youtube/v3/search?',params=payload)
	
	if rv.status_code == 200:
		
		bus_video = json.loads(rv.text)

		for v in bus_video["items"]:
			lis_ids.append(v["id"]["videoId"])
			lis_videos.append(v["snippet"]["title"])
			desc_videos.append(v["snippet"]["description"])
			canales_videos.append(v["snippet"]["channelTitle"])
	return template("result_videos.tpl",q=q,lis_ids=lis_ids,lis_videos=lis_videos,desc_videos=desc_videos,canales_videos=canales_videos)

#Busqueda de fotos

@route('/fotos/bus_fotos',method="post")
def fotos():
    text = request.forms.get("text")
    payload2 = {"method":"flickr.photos.search","text":text,"extras":"url_o,url_s","format":"json","api_key":key3}
    rf = requests.get('https://api.flickr.com/services/rest',params=payload2)
   
    lis_imagenes = []
    lis_titulos= []
   
    if rf.status_code == 200:
        bus_imagen = json.loads(rf.text[14:-1])

        for titulo in bus_imagen["photos"]["photo"]:
            lis_titulos.append(titulo["title"])

        for imagen in bus_imagen["photos"]["photo"]:
            if imagen.has_key("url_o"):
                lis_imagenes.append([imagen['url_s'],imagen["url_o"]])
	
	return template("result_fotos.tpl",text=text,lis_imagenes=lis_imagenes,lis_titulos=lis_titulos)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')


run(host='0.0.0.0',port=argv[1])

