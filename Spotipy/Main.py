from pathlib import Path
import Wacken_Artist_From_html
import MyArtists_From_Spotify_count   
import Common_Artist_with_count
import My_Wacken_Artist_to_Spotify
        
def main_path():
        
    try:
        Wacken_Artist_From_html.run()
    except Exception as e:
        print(f"Error while running script: {e}")
        return
    
    try:
        MyArtists_From_Spotify_count.run()
    except Exception as e:
        print(f"Error while running script: {e}")
        return
    
    try:
        Common_Artist_with_count.run()
    except Exception as e:
        print(f"Error while running script: {e}")
        return
    
def main_to_spotify():
    while True:
        response = input("Do you want to create a playlist with all your favorite songs of the artists in wacken? Y/N: ")
        
        if response == "Y" or response == "y":
            try:
                My_Wacken_Artist_to_Spotify.run()
            except Exception as e:
                print(f"Error while running script: {e}")
                return
            break
        elif response == "N" or response == "n":
            break
        print(f"{response} is not a valid character.")
    
def run():
    
    # Ruta de la carpeta "data"
    csv_file_path = Path("data/liked_artists_wacken_with_count.csv")
    # Si la carpeta "data" no existe, créala
    csv_file_path.parent.mkdir(parents=True, exist_ok=True)

    # Verifica si el archivo CSV existe
    if csv_file_path.exists():
        while True:
            response = input("You have already data. Do you want to reload all of your data of your favorite songs of the artists in wacken? Y/N: ")
            if response == "Y" or response == "y":
                main_path()
                break
            elif response == "N" or response == "n":
                break
            print(f"{response} is not a valid character.")
        main_to_spotify()
    else:
        main_path()
        main_to_spotify()
        
if __name__ == "__main__":
    run()