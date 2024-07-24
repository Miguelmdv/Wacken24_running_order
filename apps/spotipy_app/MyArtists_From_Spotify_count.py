import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import CacheFileHandler
import pandas as pd
from file_paths import ART_SPO_C_FILE
from apps.conf_app.config_env import load_env_vars

def run():
    # Carga las variables de entorno
    env_vars = load_env_vars()
    # Configura tu información de autenticación de Spotify
    client_id = env_vars["CLIENT_ID"]
    client_secret = env_vars["CLIENT_SECRET"]
    redirect_uri = env_vars["REDIRECT_URI"]

    # Inicializa el objeto SpotifyOAuth
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope="user-library-read",
            cache_handler=CacheFileHandler(),
        )
    )

    # Inicializa un diccionario para contar el número de canciones por artista
    liked_artists_count = {}

    offset = 0
    while True:
        liked_tracks_response = sp.current_user_saved_tracks(limit=50, offset=offset)
        if not liked_tracks_response["items"]:
            break
        for item in liked_tracks_response["items"]:
            artist = item["track"]["artists"][0]["name"]
            if artist not in liked_artists_count:
                liked_artists_count[artist] = 1
            else:
                liked_artists_count[artist] += 1
        offset += 50

    # Convierte el diccionario en una lista de tuplas (artista, número de canciones)
    liked_artists_list = [
        (artist, count) for artist, count in liked_artists_count.items()
    ]

    # Crea un DataFrame a partir de la lista de tuplas
    df = pd.DataFrame(liked_artists_list, columns=["Artista", "Numero de Canciones"])

    # Guarda el DataFrame en un archivo CSV
    df.to_csv(ART_SPO_C_FILE, index=False)
    print(
        f"La lista de artistas y el número de canciones se ha guardado en {ART_SPO_C_FILE}"
    )
