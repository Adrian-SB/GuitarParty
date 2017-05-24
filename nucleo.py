
import requests
import json

headers={'Guitarparty-Api-Key': '6115b4a078d150136759b6e1b85dfba83b68190b'}
url='http://api.guitarparty.com/v2/'

@route('/', method="get")
def intro():
	return template('template.tpl')

#Busqueda por artista

@route('/biografia', method="post")
def artista():
nombre="Jimi"
r=requests.get(url+'artists/?query='+nombre,headers=headers)
if r.status_code == 200:
    text=r.json()
 	 nombrecompleto =  text["objects"][0]["name"]
 	 bigrafia = text["objects"][0]["bio"]

#Busqueda por canciones

@router('/canciones')
def canciones():
cancion="Jolene"
r=requests.get(url+'songs/?query='+cancion,headers=headers)
if r.status_code == 200:
    text=r.json()
    print text["objects"][0]["title"]
    print text["objects"][0]["uri"]
    print text["objects"][0]["chords"][1]["instrument"]["name"]
    print text["objects"][0]["chords"][1]["name"] + ' --> ' + text["objects"][0]["chords"][1]["image_url"]
    print text["objects"][0]["authors"][1]["types"]
    print text["objects"][0]["authors"][1]["name"]
    print text["objects"][0]["authors"][1]["uri"]

#Muestra los acordes

@router('/acordes')
def acorde():
acorde="Am"
r=requests.get(url+'chords/?query='+acorde,headers=headers)
if r.status_code == 200:
    text=r.json()
    print 'Acorde: ', text["objects"][0]["name"]
    print 'Instrumento: ',text["objects"][0]["instrument"]["name"]
    print 'Afinacion: ',text["objects"][0]["instrument"]["tuning"]
    print 'Imagen: ',  text["objects"][0]["image_url"]
 
#Muestra las fiestas que han sido creadas

@router('/fiestas')
def listafiesta():
r=requests.get(url+'parties/',headers=headers)
if r.status_code == 200:
    text=r.json()
    print text["objects"][0]["title"]
    print text["objects"][0]["description"]
    print text["objects"][0]["current_song"]
    print text["objects"][0]["short_code"]
    print text["objects"][0]["human_uri"]

#Crea fiestas

@router('/crearfiestas')
def crearfiesta():

fiesta={"title": "FEDERICOOOOO","description": "DON FEDERICOOOOOOOO","current_song": 5,"song_seed": 5}

r=requests.post(url+'parties/', json=fiesta ,headers=headers)
if r.status_code != 201:
	print "Fiesta creada"

	

if __name__ == '__main__':
	run(host='0.0.0.0',port=argv[1])