import pandas as pd
from pathlib import Path

def reorganize(df : pd.DataFrame):
    # Convertir la columna 'Hora_Inicio' a formato datetime
    df['Hora_Inicio'] = pd.to_datetime(df['Hora_Inicio'], format='%H:%M').dt.time
    df['Hora_Fin'] = pd.to_datetime(df['Hora_Fin'], format='%H:%M').dt.time

    # Crear la columna 'buffer'
    df['buffer'] = df['Hora_Inicio'].apply(lambda x: 1 if x >= pd.to_datetime('00:00').time() and x < pd.to_datetime('03:00').time() else 0)

    # Definir el orden de los días de la semana
    dias_ordenados = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']
    df['Día'] = pd.Categorical(df['Día'], categories=dias_ordenados, ordered=True)
    
    # Ordenar el DataFrame por 'Día', 'buffer', y 'Hora_Inicio'
    df_sorted = df.sort_values(by=['Día', 'buffer', 'Hora_Inicio'], ascending=[True, True, True])

    # Eliminar la columna 'buffer' si ya no es necesaria
    df_sorted = df_sorted.drop(columns=['buffer'])
    
    # Resetear los índices
    df_sorted = df_sorted.reset_index(drop=True)

    return df_sorted

def data_merge(schedule_df : pd.DataFrame, songs_df: pd.DataFrame, direction : str, complete_rute : Path, people : list, drop = False):
    
    # Unir los DataFrames por la columna 'Artista'
    merged_df = pd.merge(schedule_df, songs_df, on='Artista', how=direction)

    # Convertir la columna 'Numero de Canciones' a enteros, reemplazar todos los valores excepto los vacíos o los 0 por 1 y renombrarlo
    merged_df[people[0]] = merged_df['Numero de Canciones'].fillna(0).astype(int).apply(lambda x: 1 if pd.notna(x) and x != '' and x != 0 else x)
    for person in people[1:]:
        # Añadir columnas vacías para el resto de personas (si las hay) 
        merged_df[person] = 0
        merged_df[person].astype(int)

    # Eliminar la columna original 'Numero de Canciones' y 'Horario'
    merged_df.drop(columns=['Numero de Canciones','Horario'], inplace=True)
    
    #Deja solo las vacias
    if drop:
        merged_df = merged_df[merged_df['Día'].isna()]
    else:
        merged_df = reorganize(merged_df)
        
    # Guardar el DataFrame resultante en un nuevo archivo CSV
    merged_df.to_csv(complete_rute, index=False)

    print(f"Datos combinados y exportados a {complete_rute}")
    
    
def run(people : list):
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
    
    print("\nCombinando el horario...\n")
    
    data_merge(schedule_df, songs_df, "left", merged_rute, people)
    data_merge(schedule_df, songs_df, "right", void_rute, people, drop=True)
    