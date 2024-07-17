import pandas as pd
from pathlib import Path

def data_merge(schedule_df : pd.DataFrame, songs_df: pd.DataFrame, direction : str, complete_rute : Path, people : list, drop = False):
    
    # Unir los DataFrames por la columna 'Artista'
    merged_df = pd.merge(schedule_df, songs_df, on='Artista', how=direction)

    # Convertir la columna 'Numero de Canciones' a enteros, reemplazar todos los valores excepto los vacíos o los 0 por 1 y renombrarlo
    merged_df[people[0]] = merged_df['Numero de Canciones'].fillna(0).astype(int).apply(lambda x: 1 if pd.notna(x) and x != '' and x != 0 else x)
    for person in people[1:]:
        # Añadir columnas vacías person_2 y person_3
        merged_df[person] = 0
        merged_df[person].astype(int)

    # Eliminar la columna original 'Numero de Canciones' y 'Horario'
    merged_df.drop(columns=['Numero de Canciones','Horario'], inplace=True)
    
    #Deja solo las vacias
    if drop:
        merged_df = merged_df[merged_df['Día'].isna()]

    # Guardar el DataFrame resultante en un nuevo archivo CSV
    merged_df.to_csv(complete_rute, index=False)

    print(f"Datos combinados y exportados a {complete_rute}")