% include('header.tpl', title='cancion')
<br/>
	%for titulos,instrumentos,acordes,fotos,tipos,nombresautores in zip(lis_titulo=lis_titulo,lis_instrumento=lis_instrumento,lis_acorde=lis_acorde, lis_fotoacorde=lis_fotoacorde, lis_nombreautor=lis_nombreautor):
	<ul>
        <h2>{{titulos}}</h2>
        <p>Tipo: {{tipos}}
        <p>Instrumento: {{instrumentos}}</p>
        <p>Acorde: {{acordes}}</p>
        <p><img src="{{fotos}}"></p>
        <p>Autor: {{nombresautores}}</p>
    %end
%include('footer.tpl')

