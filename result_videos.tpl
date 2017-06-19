% include('header.tpl', title='videos')
%for titulo,des,cal,id in zip(lis_videos,desc_videos,canales_videos,lis_ids):
                        <h2>{{titulo}}</h2>
                        <p>{{des}}</p>
                        <p><iframe width="500" height="300" src="https://www.youtube.com/embed/{{id}}" frameborder="0" allowfullscreen></iframe></p>
%end
%include('footer.tpl')
