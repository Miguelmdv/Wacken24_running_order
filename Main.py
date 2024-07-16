import pandas as pd
import running_order
from dotenv import dotenv_values
from pathlib import Path
from spotipy_app import Main

def write_env_file(path, env_vars):
    with open(path, 'w') as f:
        for key, value in env_vars.items():
            f.write(f'{key}={value}\n')

def clean_env_values(env_vars : dict) -> dict:
    # Limpiar las variables sobrantes basadas en NUM_PEOPLE
    num_people = int(env_vars.get('NUM_PEOPLE', 0))
    keys_to_remove = [f'PERSON_{i}' for i in range(num_people + 1, len(env_vars) + 1) if f'PERSON_{i}' in env_vars]
    
    for key in keys_to_remove:
        env_vars.pop(key)

    return env_vars

def settings_persons(auto = True) -> list:
    people = []
    dotenv_path = Path('spotipy_app/.env')
    
    # Leer todas las variables del archivo .env
    env_vars = dotenv_values(dotenv_path)
    
    if auto: 
        # Recorrer los nombres de las personas y agregarlos a la lista de personas
        for num in range(int(env_vars["NUM_PEOPLE"])):
            people.append(env_vars[f"PERSON_{num+1}"])
    else:
        your_name = input("Como te llamas? ")
        
        people.append(your_name)
        env_vars['PERSON_1'] = your_name
        
        while True:
            response = input("Cuantas personas quieres añadir? ")
            try:
                # Convertir la respuesta en un número y sumarle 1 para incluir tu nombre
                env_vars["NUM_PEOPLE"] = int(response)+1
                break
            except ValueError:
                print("Eso no es un número!")
                
        if env_vars["NUM_PEOPLE"] > 1:
            # Recorrer los nombres de las personas y agregarlos a la lista de personas
            for num in range(int(env_vars["NUM_PEOPLE"])-1):
                name = input(f"Nombre de la persona nº{str(num+1)}: ")
                people.append(name)
                env_vars[f'PERSON_{num+2}'] = name
        
        # Limpiar las variables sobrantes basadas en NUM_PEOPLE
        env_vars = clean_env_values(env_vars)
        # Escribir las variables modificadas de nuevo en el archivo .env
        write_env_file(dotenv_path, env_vars)
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
