from bottle import Bottle,route,run,request,template

headers={'Guitarparty-Api-Key': '6115b4a078d150136759b6e1b85dfba83b68190b'}
url='http://api.guitarparty.com/v2/'

@route('/Inicio')
def inicio():
	return template('header.tpl')

@route('/Inicio/Artista', method="post")
def artista(artista):
#artista = request.forms.get('artista')
r=requests.get(url+'artists/?query='+artista,headers=headers)

if r.status_code == 200:
    text=r.json()

 	 nombrecompleto =  text["objects"][0]["name"]
 	 bigrafia = text["objects"][0]["bio"]
 	 return template('buscador.tpl', artista=artista )

run(host='0.0.0.0', port=8080)