import pandas as pd
from file_paths import BAND_LIST_FILE, ART_SPO_C_FILE, ART_WA_C_FILE, ALL_ART_W_C_FILE

def run():

    df_band_list = pd.read_csv(BAND_LIST_FILE)
    df_liked_artists = pd.read_csv(ART_SPO_C_FILE)

    df_common_count = pd.merge(df_band_list, df_liked_artists, on="Artista").sort_values(by='Artista').reset_index(drop=True)
    df_common_count_all = pd.merge(df_band_list, df_liked_artists, on="Artista", how="left").sort_values(by='Artista').reset_index(drop=True) 
    ## QUITAR EL HOW=LEFT PARA TENER EL DF LIMPIO

    df_common_count.to_csv(ART_WA_C_FILE, index=False)
    df_common_count_all.to_csv(ALL_ART_W_C_FILE, index=False)
    
    print(f"La lista de artistas y el número de canciones que te gustan del wacken se ha guardado en {ART_WA_C_FILE}")