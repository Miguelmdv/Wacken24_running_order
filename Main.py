import pandas as pd
import running_order
from pathlib import Path
from spotipy_app import spotipy_main
import config_env
import data_merge_running_order as dm


if __name__ == "__main__":
    # Carga las variables de entorno y el numero de personas
    env_vars, people = config_env.manage_env_file()
    
    spotipy_main.run()
    
    running_order.run()

    # Leer el archivo CSV de horarios
    schedule_df = pd.read_csv('data/wacken_running_order.csv')

    # Leer el segundo archivo CSV con los artistas y número de canciones
    songs_df = pd.read_csv('data/all_liked_artists_wacken_with_count.csv')

    # Dividir la columna 'Horario' en 'Hora Inicio' y 'Hora Fin'
    schedule_df[['Hora_Inicio', 'Hora_Fin']] = schedule_df['Horario'].str.split(' - ', expand=True)

    # Insertar las nuevas columnas en las posiciones adecuadas
    schedule_df.insert(3, 'Hora_Inicio', schedule_df.pop('Hora_Inicio'))
    schedule_df.insert(4, 'Hora_Fin', schedule_df.pop('Hora_Fin'))
    
    merged_rute = Path('data/wacken_running_order_merged.csv')
    void_rute = Path('data/wacken_running_order_void.csv')
    
    print("\nCreando horarios...\n")
    
    dm.data_merge(schedule_df, songs_df, "left", merged_rute, people)
    dm.data_merge(schedule_df, songs_df, "right", void_rute, people, drop=True)
    
    input("\nPresiona Enter para terminar...")
