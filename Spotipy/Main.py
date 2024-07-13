import os
import Wacken_Artist_From_html
import MyArtists_From_Spotify_count   
import Common_Artist_with_count
import My_Wacken_Artist_to_Spotify
        
def main():
        
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
    
if __name__ == "__main__":
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Ruta de la carpeta "data" dentro de la carpeta base
    data_dir = os.path.join(base_dir, "data")

    # Si la carpeta "data" no existe, créala
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    csv_file_path = os.path.join(data_dir, "liked_artists_wacken_with_count.csv")

    # Verifica si el archivo CSV existe
    if os.path.exists(csv_file_path):
        while True:
            response = input("You have already data. Do you want to reload all of your data of your favorite songs of the artists in wacken? Y/N: ")
            if response == "Y" or response == "y":
                main()
                break
            elif response == "N" or response == "n":
                break
            print(f"{response} is not a valid character.")
        main_to_spotify()
    else:
        main()
        main_to_spotify()