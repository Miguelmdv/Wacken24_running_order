from pathlib import Path
from spotipy_app import Wacken_Artist_From_html
from spotipy_app import MyArtists_From_Spotify_count   
from spotipy_app import Common_Artist_with_count
from spotipy_app import My_Wacken_Artist_to_Spotify
        
def main_path():
        
    try:
        Wacken_Artist_From_html.run()
    except Exception as e:
        print(f"Error al ejecutar el script: {e}")
        return
    
    try:
        MyArtists_From_Spotify_count.run()
    except Exception as e:
        print(f"Error al ejecutar el script: {e}")
        return
    
    try:
        Common_Artist_with_count.run()
    except Exception as e:
        print(f"Error al ejecutar el script: {e}")
        return
    
def main_to_spotify():
    while True:
        response = input("Quieres crear una lista de reproducción con todas tus canciones favoritas de los artistas del Wacken? Y/N: ")
        
        if response == "Y" or response == "y":
            try:
                My_Wacken_Artist_to_Spotify.run()
            except Exception as e:
                print(f"Error al ejecutar el script: {e}")
                return
            break
        elif response == "N" or response == "n":
            break
        print(f"{response} no es un carácter válido.")
    
def run():
    
    # Ruta de la carpeta "data"
    csv_file_path = Path("spotipy_app/data/all_liked_artists_wacken_with_count.csv")
    
    # Verifica si el archivo CSV existe
    if csv_file_path.exists():
        while True:
            response = input("Ya existen datos. Quieres recargar todos los datos de tus canciones favoritas de los artistas del Wacken? Y/N: ")
            if response == "Y" or response == "y":
                main_path()
                break
            elif response == "N" or response == "n":
                break
            print(f"{response} no es un carácter válido.")
        main_to_spotify()
    else:
        main_path()
        main_to_spotify()
        
if __name__ == "__main__":
    run()