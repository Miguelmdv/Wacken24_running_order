from pathlib import Path
import pandas as pd
from bs4 import BeautifulSoup

def run():
    # Ruta completa de la carpeta "html"
    html_file = Path("html/Running Order Music _ Wacken Open Air.html")
    # Si la carpeta "html" no existe, crearla
    html_file.parent.mkdir(parents=True, exist_ok=True) 

    # Cargar el contenido del archivo HTML
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parsear el contenido del archivo HTML con BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Inicializar listas para almacenar los datos
    days = []
    scenarios = []
    times = []
    artists = []

    # Variables de control para el día y escenario actuales
    current_day = "Wednesday"
    day_counter = 0
    days_of_week = ["Wednesday", "Thursday", "Friday", "Saturday"]

    # Inicializar variables para el tiempo y escenario actuales
    current_time = None
    current_scenario = None

    # Lista de escenarios reconocidos
    recognized_scenarios = [
        "FASTER", "LOUDER", "HEADBANGERS STAGE", "W:E:T STAGE", 
        "WACKINGER STAGE", "WASTELAND STAGE", "HARDER"
    ]

    # Variable para indicar si cambiar de día
    change_day = False
    # Variable para saber si estamos dentro de una etiqueta <a>
    inside_a_tag = False

    # Iterar sobre todos los elementos del cuerpo del HTML
    for item in soup.body.descendants:
        if item.name == 'h4':
            # Cambiar de escenario solo si está en la lista de escenarios reconocidos
            scenario_text = item.get_text(strip=True).upper()
            if scenario_text in recognized_scenarios:
                if change_day:
                    day_counter += 1
                    current_day = days_of_week[day_counter]
                    print(f"Día cambiado a: {current_day}")
                    change_day = False
                
                current_scenario = scenario_text
                print(f"Escenario encontrado: {current_scenario}")
                
                # Marcar para cambiar de día después de "WASTELAND STAGE"
                if current_scenario == "WASTELAND STAGE":
                    change_day = True
                    
        elif item.name == 'div' and 'ro-list-time mr-2' in ' '.join(item.get('class', [])):
            # Extraer el rango horario
            current_time = item.get_text(strip=True)
            print(f"Horario encontrado: {current_time}")
            
        elif item.name == "a":
            inside_a_tag = True
            
        elif item.name == 'strong' and inside_a_tag:
            inside_a_tag = False
            # Extraer el nombre del artista
            artist = item.get_text(strip=True)
            if current_time and current_scenario:
                # Agregar los datos a las listas solo si tiempo y escenario están definidos
                
                # Verificar si el nombre de la banda no contiene caracteres raros
                
                # excluded_terms = ["Metal Battle", "40", "Anniversary", "Show", "Years", "MB", "USA"]
                # if all(term not in artist for term in excluded_terms):
                days.append(current_day)
                scenarios.append(current_scenario)
                times.append(current_time)
                artists.append(artist)
                print(f"Artista agregado: {artist} en {current_day}, {current_scenario}, {current_time}")

    # Crear un DataFrame con los datos extraídos
    data = {
        'Día': days,
        'Escenario': scenarios,
        'Horario': times,
        'Artista': artists
    }
    df = pd.DataFrame(data)

    
    # Exportar el DataFrame a un archivo CSV
    rute = Path('data/wacken_running_order.csv')
    rute.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(rute, index=False)

    print(f"Datos exportados a {rute}")
