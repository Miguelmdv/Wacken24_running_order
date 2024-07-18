import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import CacheFileHandler
import pandas as pd
from pathlib import Path
from config_env import load_env_vars

def run():
    # Carga las variables de entorno
    env_vars = load_env_vars()
    # Configura tu información de autenticación de Spotify
    client_id = env_vars["CLIENT_ID"]
    client_secret = env_vars["CLIENT_SECRET"]
    redirect_uri = env_vars["REDIRECT_URI"]

    # Autenticación con Spotipy
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope="user-library-read playlist-modify-public playlist-modify-private",
            cache_handler=CacheFileHandler(),
        )
    )

    csv_file_path = Path("data/liked_artists_wacken_with_count.csv")
    # Leer el archivo CSV
    df = pd.read_csv(csv_file_path)

    # Asegúrate de que la columna se llama 'Artista'
    artistas = df['Artista'].tolist()

    # Obtener las canciones guardadas en la biblioteca del usuario
    saved_tracks = []
    results = sp.current_user_saved_tracks(limit=50)
    while results:
        for item in results['items']:
            track = item['track']
            saved_tracks.append(track)
        results = sp.next(results) if results['next'] else None

    # Filtrar las canciones guardadas por los artistas designados
    tracks_uris = []
    for track in saved_tracks:
        for artist in track['artists']:
            if artist['name'] in artistas:
                tracks_uris.append(track['uri'])
                break

    # Crear una nueva lista de reproducción
    user_id = sp.me()['id']
    playlist_name = 'My Wacken 2024 😎'
    playlist_description = 'Lista creada automaticamente con Spotipy a partir de mis gustos personales de los artistas del Wacken 2024'
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, description=playlist_description)

    # Dividir la lista de URIs en grupos de máximo 100
    chunk_size = 100
    for i in range(0, len(tracks_uris), chunk_size):
        sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist['id'], tracks=tracks_uris[i:i+chunk_size])

    print(f'Lista de reproducción "{playlist_name}" creada exitosamente.')
