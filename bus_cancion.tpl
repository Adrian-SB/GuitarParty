%include('header.tpl' )
                        <h2>Buscador de canción</h2>
                        <p><form method="post" action="/cancion/bus_cancion" accept-charset="utf-8">
                    <input type="text" name = "cancion" class="text">
                    <input type="submit" class="submit" value="Buscar"></form>
%include('footer.tpl')

