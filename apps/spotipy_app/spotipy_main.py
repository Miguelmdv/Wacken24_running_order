from apps.spotipy_app import Wacken_Artist_From_html
from apps.spotipy_app import MyArtists_From_Spotify_count   
from apps.spotipy_app import Common_Artist_with_count
from apps.spotipy_app import My_Wacken_Artist_to_Spotify
from file_paths import ALL_ART_W_C_FILE
        
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
    
    custom_list_spotify()
    
def custom_list_spotify():
    while True:
        response = input("\nQuieres crear una lista de reproducción con todas tus canciones favoritas de los artistas del Wacken?\nY/N: ")
        
        if response.lower() == "y":
            try:
                print("\nCreando lista de reproducción en Spotify...\n")
                My_Wacken_Artist_to_Spotify.run()
            except Exception as e:
                print(f"Error al crear la lista de reproducción: {e}")
                return
            break
        if response.lower() == "n":
            break
        print(f"'{response}' no es un carácter válido.")
    
def run():
    # Verifica si el archivo CSV existe
    if ALL_ART_W_C_FILE.exists():
        while True:
            response = input("\nQuieres recargar los datos de tus artistas de Spotify? Esto puede llevar tiempo.\nY/N: ")
            if response.lower() == "y":
                main_path()
                break
            if response.lower() == "n":
                main_path(load_spotify_data = False)
                break
            print(f"'{response}' no es un carácter válido.")
    else:
        main_path()