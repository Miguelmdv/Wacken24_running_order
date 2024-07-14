import pandas as pd
from pathlib import Path

def run():
    
    data_dir = Path("spotipy_app/data")
    # Si la carpeta "data" no existe, créala
    data_dir.mkdir(parents=True, exist_ok=True)
    
    band_list_path = data_dir / "band_list.csv"
    liked_artists_path = data_dir / "liked_artists_spoti_with_count.csv"

    df_band_list = pd.read_csv(band_list_path)
    df_liked_artists = pd.read_csv(liked_artists_path)

    df_common_count = pd.merge(df_band_list, df_liked_artists, on="Artista").sort_values(by='Artista').reset_index(drop=True)
    df_common_count_all = pd.merge(df_band_list, df_liked_artists, on="Artista", how="left").sort_values(by='Artista').reset_index(drop=True) 
    ## QUITAR EL HOW=LEFT PARA TENER EL DF LIMPIO

    wacken_common_path = data_dir / "liked_artists_wacken_with_count.csv"
    all_wacken_common_path = data_dir / "all_liked_artists_wacken_with_count.csv"
    df_common_count.to_csv(wacken_common_path, index=False)
    df_common_count_all.to_csv(all_wacken_common_path, index=False)
    
    print(f"La lista de artistas y el número de canciones que te gustan del wacken se ha guardado en {wacken_common_path}")