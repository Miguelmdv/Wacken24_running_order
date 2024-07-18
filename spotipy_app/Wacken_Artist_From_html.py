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

    # Encontrar el div con id="artistlist"
    artist_list_div = soup.find('div', {'id': 'artistlist'})

    # Encontrar todos los divs dentro del div con id="artistlist"
    inner_divs = artist_list_div.find_all('div')

    # Conjunto para almacenar los nombres de las bandas únicos
    band_names_set = set()

    # Iterar sobre los divs internos
    for div in inner_divs:
        # Encontrar las etiquetas 'a' dentro de cada div
        a_tags = div.find_all('a')
        # Iterar sobre las etiquetas 'a'
        for a_tag in a_tags:
            # Encontrar las etiquetas h5 dentro de cada etiqueta 'a'
            h5_tags = a_tag.find_all('h5')
            # Iterar sobre las etiquetas h5 y obtener el texto
            for h5_tag in h5_tags:
                # Obtener el texto de la etiqueta h5
                band_name = h5_tag.get_text(strip=True)
                # Verificar si el nombre de la banda no contiene las cadenas "Band Name" o "Batlle"
                if "Metal Battle" not in band_name and "40" not in band_name and "Anniversary" not in band_name and "Show" not in band_name:
                    # Agregar el nombre de la banda al conjunto
                    band_names_set.add(band_name)

    # Convertir el conjunto a una lista
    band_names = list(band_names_set)
    
    # Ruta completa de la carpeta "data"
    csv_file = Path("data/band_list.csv")
    # Si la carpeta "data" no existe, crearla
    csv_file.parent.mkdir(parents=True, exist_ok=True)

    # Crear un DataFrame con los data y guardarlos en un archivo CSV
    df = pd.DataFrame(band_names, columns=['Artista'])
    df.to_csv(csv_file, index=False)

    print(f"\nLa lista de bandas extraída del html de wacken.com ha sido guardada en {csv_file}")
