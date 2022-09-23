def cargar_canciones(nombre_archivo: str)->list:
    canciones = []
    file = open(nombre_archivo)
    titulos=file.readline()
    linea = file.readline()
    while len(linea) > 0:
        datos = linea.split(",")
        cancion = {}
        cancion["posicion"] = datos[0]
        cancion["nombre_cancion"] = datos[1]
        cancion["nombre_artista"] = datos[2]
        cancion["anio"] = datos[3]
        cancion["letra"] = datos[4]
        canciones.append(cancion)
        linea = file.readline()
    file.close()

    return canciones

def buscar_cancion(canciones: list, nombre_cancion: str, anio: int)->dict:
    song = None
    for s in canciones:
        nombre = s["nombre_cancion"]
        anio_cancion = s["anio"]
        if nombre == nombre_cancion and anio_cancion == str(anio):
            song = s
            break;
    return song

def buscar_por_anio(canciones: list, anio: int)->list:
    songs_by_year = []
    for s in canciones:
        year_song = s["anio"]
        if year_song == str(anio):
            del s["letra"]
            songs_by_year.append(s)
    return songs_by_year

def buscar_artista_por_periodo(canciones: list, artista: str, a_inicial: int, a_final: int)->list:
    songs = []
    for s in canciones:
        if s["nombre_artista"] == artista and int(s["anio"]) >= a_inicial and int(s["anio"]) <= a_final:
            del s["letra"]
            songs.append(s)
    return songs

def buscar_por_artista(canciones: list, artista: str)->list:
    song_by_artist = []
    for s in canciones:
        artist = s["nombre_artista"]
        if artist == artista:
            del s["letra"]
            song_by_artist.append(s)
    return song_by_artist

def todos_artistas_cancion(canciones: list, nombre_cancion: str)->list:
    artist = []
    for s in canciones:
        if s["nombre_cancion"] == nombre_cancion:
            artist.append(s["nombre_artista"])
    return artist

def artistas_mas_populares(canciones: list, nCanciones: int)->dict:
    artist_names = {}
    num_canciones = 0
    for s in canciones:
        if s["nombre_artista"] in artist_names:
            if artist_names[s["nombre_artista"]] == 1:
                num_canciones += 1
            artist_names[s["nombre_artista"]] += 1 
        else:
            artist_names[s["nombre_artista"]] = 1
    for k, v in artist_names.copy().items():
        if v < nCanciones:
            del artist_names[k]  
    return artist_names

def artista_mas_popular(canciones: list)->dict:
    artist_names = {}
    num_canciones = 0
    for s in canciones:
        if s["nombre_artista"] in artist_names:
            if artist_names[s["nombre_artista"]] == 1:
                num_canciones += 1
            artist_names[s["nombre_artista"]] += 1 
        else:
            artist_names[s["nombre_artista"]] = 1
    return {max(artist_names, key=lambda key: artist_names[key]): max(artist_names.values())}

def artistas_y_sus_canciones(canciones: list)->dict:
    names = []
    artist_and_songs = {}
    i = 0
    for s in canciones:
        if not s["nombre_artista"] in artist_and_songs:
            artist_and_songs[s["nombre_artista"]] = []
    for s in canciones:
        if not s["nombre_cancion"] in artist_and_songs[s["nombre_artista"]]:
            artist_and_songs[s["nombre_artista"]].append(s["nombre_cancion"])
    return artist_and_songs

def promedio_canciones_por_artista(canciones: list)->float:
    art_and_songs = artistas_y_sus_canciones(canciones)
    artists = 0
    songs = 0
    for art in art_and_songs:
        artists+=1
        songs += len(art_and_songs[art])         
    prom = songs/artists
    return prom
        
    



