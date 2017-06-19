% include('header.tpl', title='cancion')
%for titulos,tipos,instrumentos,nombresautores in zip(lis_titulo,lis_tipo,lis_instrumento,lis_nombreautor):
        <p><h2>{{titulos}}</h2></p>
        <p>Tipo: {{tipos[0]}}</p>
        <p>Instrumento: {{instrumentos}}</p>
		<p>Autor: {{nombresautores}}</p>
%end
%include('footer.tpl')

