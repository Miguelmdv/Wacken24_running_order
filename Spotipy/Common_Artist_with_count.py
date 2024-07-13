import pandas as pd
import os

def run():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")

    # Si la carpeta "data" no existe, créala
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        
    band_list_path = os.path.join(data_dir, "band_list.csv")
    liked_artists_path = os.path.join(data_dir, "liked_artists_spoti_with_count.csv")

    df_band_list = pd.read_csv(band_list_path)
    df_liked_artists = pd.read_csv(liked_artists_path)

    df_common_count = pd.merge(df_band_list, df_liked_artists, on="Artista", how="left").sort_values(by='Artista').reset_index(drop=True) ## QUITAR EL HOW=LEFT PARA TENER EL DF LIMPIO

    wacken_comun_path = os.path.join(data_dir, "liked_artists_wacken_with_count.csv")
    df_common_count.to_csv(wacken_comun_path, index=False)
    
    print(f"La lista de artistas y el número de canciones que te gustan del wacken se ha guardado en {wacken_comun_path}")