from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path


def run():

    # Ruta completa de la carpeta "html"
    html_file = Path("html/Bands _ Wacken Open Air.html")
    # Si la carpeta "html" no existe, crearla
    html_file.parent.mkdir(parents=True, exist_ok=True)

    # Abrir el archivo HTML y leer su contenido
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Analizar el HTML con BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extraer todos los elementos <h5> con la clase y atributo especificado
    artist_elements = soup.find_all('h5', class_='card-title text-center')

    # Crear una lista con el texto de cada elemento encontrado
    band_names = [element.get_text() for element in artist_elements]
    
    # Ruta completa de la carpeta "data"
    csv_file = Path("data/band_list.csv")
    
    # Si la carpeta "data" no existe, crearla
    csv_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Crear un DataFrame con los data y guardarlos en un archivo CSV
    df = pd.DataFrame(band_names, columns=['Artista'])
    df.to_csv(csv_file, index=False)

    print(f"\nLa lista de bandas extraída del html de wacken.com ha sido guardada en {csv_file}")
