import pandas as pd
from bs4 import BeautifulSoup
from file_paths import RUNNING_FILE, RUN_ORD_FILE

def run():
    # Cargar el contenido del archivo HTML
    with open(RUNNING_FILE, 'r', encoding='utf-8') as file:
        html_content = file.read()
        
    print("\nCreando el horario...\n")

    # Parsear el contenido del archivo HTML con BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Inicializar listas para almacenar los datos
    days = []
    scenarios = []
    times = []
    artists = []
    details = []
    doors = []

    # Variables de control para el día y escenario actuales
    current_day = "Domingo"
    day_counter = 0
    days_of_week = ("Domingo","Lunes","Martes","Miércoles", "Jueves", "Viernes", "Sábado")

    # Inicializar variables para el tiempo y escenario actuales
    current_time = None
    current_scenario = None
    current_doors = None
    # Str que aparece en la apertura de puertas del escenario
    door_str = "Doors: "

    # Lista de escenarios reconocidos
    recognized_scenarios = (
        "FASTER", "LOUDER", "HEADBANGERS STAGE", "W:E:T STAGE", 
        "WACKINGER STAGE", "WASTELAND STAGE", "HARDER", 
        "LGH CLUBSTAGE", "WELCOME TO THE JUNGLE"
    )
    # Variable para indicar si el escenario actual es el deseado
    wanted_scenario = False
    # Variable para indicar si cambiar de día
    change_day = False
    # Variable para saber si estamos dentro de una etiqueta <a>
    inside_a_tag = False
    inside_artist_detail = False

    # Iterar sobre todos los elementos del cuerpo del HTML
    for item in soup.body.descendants:
        if item.name == 'h4':
            inside_artist_detail = False
            # Cambiar de escenario solo si está en la lista de escenarios reconocidos
            scenario_text = item.get_text(strip=True).upper()
            if scenario_text in recognized_scenarios:
                wanted_scenario = True
                if change_day:
                    day_counter += 1
                    current_day = days_of_week[day_counter]
                    change_day = False
                
                current_scenario = scenario_text
                
                # Marcar para cambiar de día después de "LGH CLUBSTAGE"
                if current_scenario == "LGH CLUBSTAGE":
                    change_day = True
            else:
                wanted_scenario = False
        # Extrae el horario de apertura de puertas del escenario 
        elif door_str in item:
            current_doors = str(item).replace(door_str, "")
                    
        elif item.name == 'div' and 'ro-list-time mr-2' in ' '.join(item.get('class', [])) and wanted_scenario:
            inside_artist_detail = False
            # Extraer el rango horario
            current_time = item.get_text(strip=True)
            
        elif item.name == "a" and wanted_scenario:
            inside_a_tag = True
            
        elif item.name == 'strong' and inside_a_tag and wanted_scenario:
            inside_a_tag = False
            inside_artist_detail = True
            # Extraer el nombre del artista
            artist = item.get_text(strip=True)
            if current_time and current_scenario:
                # Agregar los datos a las listas solo si tiempo y escenario están definidos
                days.append(current_day)
                scenarios.append(current_scenario)
                doors.append(current_doors)
                times.append(current_time)
                artists.append(artist)
                details.append("_")
        # Extrae los datos extra de los artistas si los hubiera
        elif item.name == 'strong' and inside_artist_detail:
            if current_time and current_scenario:
                inside_artist_detail = False
                detail = item.get_text(strip=True)
                details[-1] = detail


    # Crear un DataFrame con los datos extraídos
    data = {
        'Día': days,
        'Escenario': scenarios,
        'Apertura Puertas': doors,
        'Horario': times,
        'Artista': artists,
        'Detalle': details
    }
    df = pd.DataFrame(data)
    
    # Exportar el DataFrame a un archivo CSV
    df.to_csv(RUN_ORD_FILE, index=False)

    print(f"Datos exportados a {RUN_ORD_FILE}")
