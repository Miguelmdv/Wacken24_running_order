from dotenv import dotenv_values
from file_paths import ENV_FILE
import subprocess

def load_env_vars() -> dict[str, str]:
    env_vars = dotenv_values(ENV_FILE)
    return env_vars

def manage_env_file() -> list: 
    # Crear el archivo .env si no existe
    if ENV_FILE.exists() and ENV_FILE.stat().st_size > 0:
        # Si el archivo existe, carga las variables y devuelve env_vars y False
        env_vars = dotenv_values(ENV_FILE)
        people = manage_settings(env_vars, True)
        return people
    else:
        # Crear el archivo vacío
        ENV_FILE.touch()
        subprocess.run(['attrib', '+h', str(ENV_FILE)])
            # Establecer permisos seguros
        ENV_FILE.chmod(0o600)
        
        print("\nCreando archivo de configuración por primera vez.")
        print("Se necesitan los datos de desarrollador de Spotify.\n")
            
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
        
        people = manage_settings(env_vars, False)
        
        print("\nConfiguración guardada satisfactoriamente.")
        
        return people

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
            response = input("\nQuieres usar los ajustes automáticos? Sino, podrás cambiar los nombres y numero de las personas.\nY/N: ")
            
            if response.lower() == "y":
                break
            if response.lower() == "n":
                auto_settings = False
                break
            print(f"'{response}' no es un carácter válido.")
    
    people = settings_persons(env_vars, auto_settings)
    return people

def settings_persons(env_vars : dict[str, str], auto = True) -> list:
    people = []
    
    if auto: 
        # Recorrer los nombres de las personas y agregarlos a la lista de personas
        for num in range(int(env_vars["NUM_PEOPLE"])):
            people.append(env_vars[f"PERSON_{num+1}"])
    else:
        your_name = input("\nComo te llamas? ")
        
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
        # env_vars = clean_env_person_values(env_vars)
        # Escribir las variables modificadas de nuevo en el archivo .env
        write_env_file(env_vars)
    return people

def write_env_file(env_vars : dict[str, str]):
    # Modo r+ para evitar permiso denegado al escribir
    with open(ENV_FILE, 'r+') as f:
        for key, value in env_vars.items():
            f.write(f'{key}={value}\n')