import pandas as pd
import running_order
import os
from dotenv import load_dotenv
from pathlib import Path

def data_merge(schedule_df : pd.DataFrame, songs_df: pd.DataFrame, direction : str, nombre_archivo : str, ruta : str, drop = False):
    
    dotenv_path = Path('Spotipy\.env')
    load_dotenv(dotenv_path=dotenv_path)
    person_1 = os.getenv('PERSON_1')
    person_2 = os.getenv('PERSON_2')
    person_3 = os.getenv('PERSON_3')
    
    # Unir los DataFrames por la columna 'Artista'
    merged_df = pd.merge(schedule_df, songs_df, on='Artista', how=direction)


    # Convertir la columna 'Numero de Canciones' a enteros, reemplazar todos los valores excepto los vacíos o los 0 por 1 y renombrarlo
    merged_df[person_1] = merged_df['Numero de Canciones'].fillna(0).astype(int).apply(lambda x: 1 if pd.notna(x) and x != '' and x != 0 else x)

    # Eliminar la columna original 'Numero de Canciones' y 'Horario'
    merged_df.drop(columns=['Numero de Canciones','Horario'], inplace=True)

    # Añadir columnas vacías person_2 y person_3
    merged_df[person_2] = 0
    merged_df[person_3] = 0
    merged_df[person_2].astype(int)
    merged_df[person_3].astype(int)

    #Deja solo las vacias
    if drop:
        merged_df = merged_df[merged_df['Día'].isna()]
    
    # Guardar el DataFrame resultante en un nuevo archivo CSV
    merged_df.to_csv(ruta + nombre_archivo, index=False)

    print("Datos combinados y exportados a " + ruta + nombre_archivo)

running_order.run()

# Leer el archivo CSV de horarios
schedule_df = pd.read_csv('data\wacken_schedule.csv')

# Leer el segundo archivo CSV con los artistas y número de canciones
songs_df = pd.read_csv('Spotipy\data\liked_artists_wacken_with_count.csv')

# Dividir la columna 'Horario' en 'Hora Inicio' y 'Hora Fin'
schedule_df[['Hora_Inicio', 'Hora_Fin']] = schedule_df['Horario'].str.split(' - ', expand=True)

# Insertar las nuevas columnas en las posiciones adecuadas
schedule_df.insert(3, 'Hora_Inicio', schedule_df.pop('Hora_Inicio'))
schedule_df.insert(4, 'Hora_Fin', schedule_df.pop('Hora_Fin'))

data_merge(schedule_df, songs_df, "left", "wacken_schedule_merged.csv", "data\\")
data_merge(schedule_df, songs_df, "right", "wacken_schedule_void.csv", "data\\", True)
