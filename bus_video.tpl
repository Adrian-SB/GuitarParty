%include('header.tpl' )
                    <h2>Buscador de videos</h2>
                    <p>
                    <form method="post" action="/videos/bus_videos" accept-charset="utf-8">
                   	<input type="text" name = "q" class="text">
                    
                    <br/><br/>
                    <strong><label for='maxResults'>Número de resultados</label></strong>
						<select id='maxResults' name='maxResults'>
							<option value="" selected="selected">-Selecciona-</option>
							<option value="1">1 resultado</option>
							<option value="5">5 resultados</option>
							<option value="10">10 resultados</option>
   							<option value="15">15 resultados</option>
 							<option value="20">20 resultados</option>
						</select>

					<strong><label for='order'>Tipo de busqueda</label></strong>
						<select id='order' name='order'>
							<option value="" selected="selected">-Selecciona-</option>			
							<option value='date'>Fecha</option>
							<option value='relevance'>Relevancia</option>
	    					<option value='viewCount'>Número visitas</option>
						</select>
						
						<br/><br/>
						<input type = "submit" value = "Buscar">
						
					</form>
					</p>

%include('footer.tpl')

