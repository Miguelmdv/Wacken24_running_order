from os import getenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from dotenv import load_dotenv
from pathlib import Path

def run():
    
    cache_file_path = Path("spotipy_app/.cache/.cache")
    # Si la carpeta ".cache" no existe, créala
    cache_file_path.parent.mkdir(parents=True, exist_ok=True)

    csv_file_path = Path("spotipy_app/data/liked_artists_spoti_with_count.csv")
    # Si la carpeta "data" no existe, créala
    csv_file_path.parent.mkdir(parents=True, exist_ok=True)

    # from dotenv import load_dotenv
    dotenv_path = Path('spotipy_app/.env')
    load_dotenv(dotenv_path=dotenv_path)
    
    # Configura tu información de autenticación de Spotify
    client_id = getenv('CLIENT_ID')
    client_secret = getenv('CLIENT_SECRET')
    redirect_uri = getenv('REDIRECT_URI')

    # Inicializa el objeto SpotifyOAuth
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                client_secret=client_secret,
                                                redirect_uri=redirect_uri,
                                                scope="user-library-read",
                                                cache_path=cache_file_path))

    # Inicializa un diccionario para contar el número de canciones por artista
    liked_artists_count = {}

    offset = 0
    while True:
        liked_tracks_response = sp.current_user_saved_tracks(limit=50, offset=offset)
        if not liked_tracks_response['items']:
            break
        for item in liked_tracks_response['items']:
            artist = item['track']['artists'][0]['name']
            if artist not in liked_artists_count:
                liked_artists_count[artist] = 1
            else:
                liked_artists_count[artist] += 1
        offset += 50

    # Convierte el diccionario en una lista de tuplas (artista, número de canciones)
    liked_artists_list = [(artist, count) for artist, count in liked_artists_count.items()]

    # Crea un DataFrame a partir de la lista de tuplas
    df = pd.DataFrame(liked_artists_list, columns=["Artista", "Numero de Canciones"])

    # Guarda el DataFrame en un archivo CSV
    df.to_csv(csv_file_path, index=False)
    print(f"La lista de artistas y el número de canciones se ha guardado en {csv_file_path}")
