%include('header.tpl' )
                        <h2>Buscador de artista</h2>
                        <p><form method="post" action="/artista/resultado_artista" accept-charset="utf-8">
                    <input type="text" name = "artista" class="text">
                    <input type="submit" class="submit" value="Buscar"></form></p>
%include('footer.tpl')

