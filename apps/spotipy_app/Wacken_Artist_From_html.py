from bs4 import BeautifulSoup
import pandas as pd
from file_paths import BANDS_FILE, BAND_LIST_FILE


def run():
    # Abrir el archivo HTML y leer su contenido
    with open(BANDS_FILE, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Analizar el HTML con BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extraer todos los elementos <h5> con la clase y atributo especificado
    artist_elements = soup.find_all('h5', class_='card-title text-center')

    # Crear una lista con el texto de cada elemento encontrado
    band_names = [element.get_text() for element in artist_elements]
    
    # Crear un DataFrame con los data y guardarlos en un archivo CSV
    df = pd.DataFrame(band_names, columns=['Artista'])
    df.to_csv(BAND_LIST_FILE, index=False)

    print(f"\nLa lista de bandas extraída del html de wacken.com ha sido guardada en {BAND_LIST_FILE}")
