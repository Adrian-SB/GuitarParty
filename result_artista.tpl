% include('header.tpl', title='artista')
%for nombrecompleto, biografia in zip(lis_nombrecompleto,lis_biografia):
                        <h2>{{nombrecompleto}}</h2>
                        <p>{{biografia}}</p>
%end
%include('footer.tpl')

