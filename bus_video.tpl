%include('header.tpl' )
                    <h2>Buscador de videos</h2>
                    <p>
                    <form method="post" action="/videos/bus_videos" accept-charset="utf-8">
                   	<input type="text" name = "q" class="text">
                    
                    <br/><br/>
                    <strong><label for='maxResults'>Límite De Resultados</label></strong>
						<select id='maxResults' name='maxResults'>
							<option value="" selected="selected">-Selecciona-</option>
							<option value="5">5 resultados</option>
							<option value="10">10 resultados</option>
   							<option value="15">15 resultados</option>
 							<option value="20">20 resultados</option>
  							<option value="25">25 resultados</option>
    						<option value="30">30 resultados</option>
    						<option value="35">35 resultados</option>
    						<option value="40">40 resultados</option>
  							<option value="45">45 resultados</option>
  							<option value="50">50 resultados</option>
						</select>

					<strong><label for='order'>Orden De Resultados</label></strong>
						<select id='order' name='order'>
							<option value="" selected="selected">-Selecciona -</option>			
							<option value='date'>Fecha</option>
							<option value='relevance'>Relevancia</option>
	    					<option value='viewCount'>Conteo De Visitas</option>
						</select>
						
						<br/><br/>
						<input type = "submit" value = "Buscar">
						<input type="reset" value = "Limpiar">
						
					</form>
					</p>

%include('footer.tpl')
