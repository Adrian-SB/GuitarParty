% include('header.tpl', title='fotos')
%for titulos, imagen in zip(lis_titulos,lis_imagenes):
                        <h2>{{titulos}}</h2>
                        <p><img width="500" height="300" src="{{imagen[0]}}"/></p>
%end
%include('footer.tpl')

