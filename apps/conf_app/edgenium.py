from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time
from pathlib import Path
import os 

def is_webdriver_in_path(driver_path : str):
    # Obtener el valor de la variable de entorno PATH
    path = os.environ.get('PATH', '')
    
    # Dividir el PATH en las diferentes rutas
    path_dirs = path.split(os.pathsep)
    
    # Comprobar si "C:/webdriver" está en las rutas del PATH
    if driver_path in path_dirs:
        return True
    else:
        return False

def download_html(driver, url, filename):
    try:
        # URL a la que queremos acceder
        driver.get(url)

        # Esperar a que la página cargue
        time.sleep(2)

        # Descargar el HTML de la página
        html_content = driver.page_source

        # Guardar el HTML en un archivo
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(html_content)

        print(f"El HTML de la página se ha descargado y guardado en '{filename}'.")

    except Exception as e:
        # Imprimir el mensaje de error si ocurre alguna excepción
        print(f"Ocurrió un error: {e}")
        

def run():
    
    # Ruta local al msedgedriver 
    driver_path = Path("C:/webdriver").resolve()
    msedgedriver_path = driver_path / "msedgedriver.exe"
    
    if not msedgedriver_path.is_file():
        print("\nEl archivo 'msedgedriver.exe' no existe en la ruta especificada.")
        print(f"Por favor, asegúrese de que el archivo se encuentra en la ruta {msedgedriver_path}.")
        input("\nPresiona Enter para terminar...")
        exit("Programa cerrado.")
    # ! elif not is_webdriver_in_path(driver_path):
    # !     print("\nNo se encuentra la variable de entorno 'PATH' configurada.")
    # !    print(f"Por favor, asegúrese de que añade el directorio {driver_path} al valor de la variable de entorno 'PATH'.")
    # !     input("\nPresiona Enter para terminar...")
    # !     exit("Programa cerrado.")
        
    print("\nDescargando archivos HTML...\n")
    # Configurar el servicio de Egde con la ruta local al msedgedriver
    service = webdriver.EdgeService(executable_path=str(msedgedriver_path))
    
    # Configurar las opciones de Egde
    options = Options()
    # Ejecutar en modo headless (sin interfaz gráfica)
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")  # Suprimir la mayoría de los mensajes de registro
    options.binary_location = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
    
    # Iniciar el navegador Egde con el servicio configurado
    driver = webdriver.Edge(service=service, options=options)
    
    url = 'https://www.wacken.com/en/program/bands/#/'
    url2 = 'https://www.wacken.com/en/program/complete-running-order/#/'
    
    html_path = Path("html")
    # Si la carpeta "html" no existe, crearla
    html_path.mkdir(exist_ok=True)
    
    html_file = html_path / "Bands _ Wacken Open Air.html"
    html_file2 = html_path / "Complete Running Order _ Wacken Open Air.html"
    
    download_html(driver,url,html_file)
    time.sleep(2)
    download_html(driver,url2,html_file2)
    # Cerrar el navegador
    driver.quit()

