from pathlib import Path
from spotipy_app import Wacken_Artist_From_html
from spotipy_app import MyArtists_From_Spotify_count   
from spotipy_app import Common_Artist_with_count
from spotipy_app import My_Wacken_Artist_to_Spotify
        
def main_path(load_spotify_data = True):
        
    try:
        Wacken_Artist_From_html.run()
    except Exception as e:
        print(f"Error al leer el html: {e}")
        return
    # Carga los datos de Spotify
    if load_spotify_data:
        try:
            print("\nCargando datos de Spotify...\n")
            MyArtists_From_Spotify_count.run()
        except Exception as e:
            print(f"Error al cargar los datos de Spotify: {e}")
            return
    
    try:
        Common_Artist_with_count.run()
    except Exception as e:
        print(f"Error al comparar los artistas de Spotify: {e}")
        return
    
def custom_list_spotify():
    while True:
        response = input("\nQuieres crear una lista de reproducción con todas tus canciones favoritas de los artistas del Wacken? Y/N: ")
        
        if response == "Y" or response == "y":
            try:
                print("\nCreando lista de reproducción en Spotify...\n")
                My_Wacken_Artist_to_Spotify.run()
            except Exception as e:
                print(f"Error al crear la lista de reproducción: {e}")
                return
            break
        elif response == "N" or response == "n":
            break
        print(f"{response} no es un carácter válido.")
    
def run():
    # Ruta del archivo con todos los artistas de spotify
    csv_file_path = Path("data/all_liked_artists_wacken_with_count.csv")
    
    # Verifica si el archivo CSV existe
    if csv_file_path.exists():
        while True:
            response = input("Ya existen datos. Esto puede llevar tiempo. Quieres recargar tus artistas de Spotify? Y/N: ")
            if response == "Y" or response == "y":
                main_path()
                break
            elif response == "N" or response == "n":
                main_path(load_spotify_data = False)
                break
            print(f"{response} no es un carácter válido.")
        custom_list_spotify()
    else:
        main_path()
        custom_list_spotify()