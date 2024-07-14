import pandas as pd
import running_order
from os import getenv
from dotenv import load_dotenv
from pathlib import Path
from spotipy_app import Main

def settings_persons(auto = True) -> list:
    people = []
    if auto:
        dotenv_path = Path('spotipy_app/.env')
        load_dotenv(dotenv_path=dotenv_path)
        people.append(getenv('PERSON_1'))
        people.append(getenv('PERSON_2'))
        people.append(getenv('PERSON_3'))
        
    else:
        your_name = input("Como te llamas? ")
        
        people.append(your_name)
        
        num_people = 0
        while True:
            response = input("Cuantas personas quieres añadir? ")
            try:
                num_people = int(response)
                break
            except ValueError:
                print("Eso no es un número!")
                
        if num_people > 0:
            for num in range(num_people):
                name = input(f"Nombre de la persona nº{str(num+1)}: ")
                people.append(name)    
    return people
        
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


if __name__ == "__main__":
    Main.run()
    
    running_order.run()

    # Leer el archivo CSV de horarios
    schedule_df = pd.read_csv('data/wacken_running_order.csv')

    # Leer el segundo archivo CSV con los artistas y número de canciones
    songs_df = pd.read_csv('spotipy_app/data/all_liked_artists_wacken_with_count.csv')

    # Dividir la columna 'Horario' en 'Hora Inicio' y 'Hora Fin'
    schedule_df[['Hora_Inicio', 'Hora_Fin']] = schedule_df['Horario'].str.split(' - ', expand=True)

    # Insertar las nuevas columnas en las posiciones adecuadas
    schedule_df.insert(3, 'Hora_Inicio', schedule_df.pop('Hora_Inicio'))
    schedule_df.insert(4, 'Hora_Fin', schedule_df.pop('Hora_Fin'))

    auto = True
    while True:
        response = input("Quieres usar los ajustes automáticos? Y/N: ")
        
        if response == "Y" or response == "y":
            break
        elif response == "N" or response == "n":
            auto = False
            break
        print(f"{response} no es un carácter válido.")
    
    people = settings_persons(auto)
    
    merged_rute = Path('data/wacken_running_order_merged.csv')
    void_rute = Path('data/wacken_running_order_void.csv')
    
    data_merge(schedule_df, songs_df, "left", merged_rute, people)
    data_merge(schedule_df, songs_df, "right", void_rute, people, drop=True)
