import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from dotenv import load_dotenv
from pathlib import Path

def run():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Ruta de la carpeta "data" dentro de la carpeta base
    data_dir = os.path.join(base_dir, "data")

    # Si la carpeta "data" no existe, créala
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Ruta completa del archivo CSV dentro de la carpeta "data"
    csv_file_path = os.path.join(data_dir, "liked_artists_wacken_with_count.csv")

    # Verifica si el archivo CSV existe
    if not os.path.exists(csv_file_path):
        print("El archivo CSV no existe.")
        exit()

    # Lee el archivo CSV y obtén los nombres de los artistas
    artistas_comunes_df = pd.read_csv(csv_file_path)
    artistas_comunes = artistas_comunes_df['Artista'].tolist()

    # Función para dividir la lista de artistas en lotes
    def chunks(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    # from dotenv import load_dotenv
    dotenv_path = Path('Spotipy\.env')
    load_dotenv(dotenv_path=dotenv_path)
    
    # Configura tu información de autenticación de Spotify
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    redirect_uri = os.getenv('REDIRECT_URI')

    # Inicializa el objeto SpotifyOAuth
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                client_secret=client_secret,
                                                redirect_uri=redirect_uri,
                                                scope="playlist-modify-private"))

    # Inicializa una lista para almacenar las canciones filtradas
    filtered_tracks = []

    # Divide la lista de artistas en lotes de 5 artistas
    for batch_artists in chunks(artistas_comunes, 5):
        # Busca las canciones por cada artista común y filtra las canciones
        for artista in batch_artists:
            results = sp.search(q=f'artist:{artista}', type='track', limit=50)
            tracks = results['tracks']['items']
            for track in tracks:
                filtered_tracks.append(track['id'])

    # Crea una nueva lista de reproducción en Spotify
    playlist_name = "My Wacken 2024 😎"
    playlist = sp.user_playlist_create(sp.me()['id'], playlist_name, public=False)
    playlist_id = playlist['id']

    # Divide la lista de canciones en lotes de 100 canciones
    for chunk_tracks in chunks(filtered_tracks, 100):
        # Agrega las canciones filtradas a la nueva lista de reproducción por lotes
        sp.playlist_add_items(playlist_id, chunk_tracks)

    print(f"Se ha creado la lista de reproducción '{playlist_name}' con las canciones de artistas comunes.")