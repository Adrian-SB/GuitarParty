%include('header.tpl' )
                        <h2>Creación de fiestas</h2>
                        <p>En esta página puedes crear tu propia fiesta con tus canciones preferidas</p>
                        <h3>Título</h3>
                        <p><form method="post" action="/fiesta/crea_crearfiestas" accept-charset="utf-8">
                    	<input type="text" name = "titulo" class="text"></form></p>
                    	<h3>Descripción</h3>
                    	<p><form method="post" action="/fiesta/crea_crearfiestas" accept-charset="utf-8">
                    	<input type="text" name = "descripcion" class="text"></form></p>
                    	<h3>Canción</h3>
                    	<p><form method="post" action="/fiesta/crea_crearfiestas" accept-charset="utf-8">
                    	<input type="text" name = "cancion" class="text"></form></p>
%include('footer.tpl')

