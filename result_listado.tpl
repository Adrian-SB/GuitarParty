%include('header.tpl', title='listado')
%for tit,des,url in zip(lis_tif,lis_descf,lis_url):
			<h2>{{tit}}</h2>
			<p>{{des}}</p>
			<p>{{url}}</p>
%end
%include('footer.tpl')