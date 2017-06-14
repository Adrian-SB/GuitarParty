% include('header.tpl', title='cancion')

                        <h2>{{titulo}}</h2>
                        <p>Código canción: {{codigo}}</p>
                        <p>Instrumento: {{instrumento}}</p>
                        <p>Acorde: {{acorde}}</p>
                        <p><img src="{{fotoacorde}}"></p>
                        <p>Tipo: {{tipo}}</p>
                        <p>Autor: {{nombreautor}}</p>
                        <p>Código autor: {{autorcodigo}}</p>
%include('footer.tpl')

