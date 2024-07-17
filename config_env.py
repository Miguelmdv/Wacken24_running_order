from dotenv import dotenv_values
from pathlib import Path

def load_env_vars() -> dict[str, str]:
    dotenv_path = Path('.env')
    env_vars = dotenv_values(dotenv_path)
    return env_vars

def manage_env_file() -> tuple[dict[str, str], list]: 
    dotenv_path = Path('.env')
    # Crear el archivo .env si no existe
    if dotenv_path.exists():
        # Si el archivo existe, carga las variables y devuelve env_vars y False
        env_vars = dotenv_values(dotenv_path)
        people = manage_settings(env_vars, True)
        return env_vars, people
    else:
        dotenv_path.touch()
        dotenv_path.chmod(0o600)  # Permisos seguros: solo lectura/escritura para el propietario
        
        print("Creando archivo de configuración por primera vez.")
        print("Introduce los datos de tu cuenta de Spotify.")
            
        # Pedir al usuario que ingrese los valores de las tres primeras variables
        client_id = input("Introduce CLIENT_ID: ")
        client_secret = input("Introduce CLIENT_SECRET: ")
        redirect_uri = input("Introduce REDIRECT_URI: ")
        
        # Crear un diccionario con las variables
        env_vars = {
            'CLIENT_ID': client_id,
            'CLIENT_SECRET': client_secret,
            'REDIRECT_URI': redirect_uri,
            'NUM_PEOPLE': "1",
            'PERSON_1': "Nombre_Persona_1"
        }
        
        write_env_file(env_vars)
        
        print("Archivo .env creado y actualizado con las variables especificadas.")
        
        people = manage_settings(env_vars, False)
        return env_vars, people

def write_env_file(env_vars : dict[str, str]):
    dotenv_path = Path('.env')
    with open(dotenv_path, 'w') as f:
        for key, value in env_vars.items():
            f.write(f'{key}={value}\n')

def clean_env_person_values(env_vars : dict[str, str]) -> dict[str, str]:
    # Limpiar las variables sobrantes basadas en NUM_PEOPLE
    num_people = int(env_vars.get('NUM_PEOPLE', 0))
    keys_to_remove = [f'PERSON_{i}' for i in range(num_people + 1, len(env_vars) + 1) if f'PERSON_{i}' in env_vars]
    
    for key in keys_to_remove:
        env_vars.pop(key)

    return env_vars

def manage_settings(env_vars : dict[str, str], auto_settings : bool) -> list:
    if auto_settings:
        while True:
            response = input("Quieres usar los ajustes automáticos? Sino, podrás cambiar los nombres de las personas. Y/N: ")
            
            if response == "Y" or response == "y":
                break
            elif response == "N" or response == "n":
                auto_settings = False
                break
            print(f"{response} no es un carácter válido.")
    
    people = settings_persons(env_vars, auto_settings)
    return people

def settings_persons(env_vars : dict[str, str], auto = True) -> list:
    people = []
    
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
        env_vars = clean_env_person_values(env_vars)
        # Escribir las variables modificadas de nuevo en el archivo .env
        write_env_file(env_vars)
    return people