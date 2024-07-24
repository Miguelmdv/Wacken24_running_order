from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time
from file_paths import PATH_DIRS, BANDS_FILE, RUNNING_FILE, DRIVER_DIR, MSEDGEDRIVER_FILE

def is_webdriver_in_path(driver_path : str):
    # Comprobar si "C:/webdriver" está en las rutas del PATH
    if driver_path in PATH_DIRS:
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
    
    if not MSEDGEDRIVER_FILE.is_file():
        print("\nEl archivo 'msedgedriver.exe' no existe en la ruta especificada.")
        print(f"Por favor, asegúrese de que el archivo se encuentra en la ruta {MSEDGEDRIVER_FILE}.")
        input("\nPresiona Enter para terminar...")
        exit("Programa cerrado.")
        
    elif not is_webdriver_in_path(str(DRIVER_DIR)):
        print("\nNo se encuentra la variable de entorno 'PATH' configurada.")
        print(f"Por favor, asegúrese de que añade el directorio {DRIVER_DIR} al valor de la variable de entorno 'PATH'.")
        input("\nPresiona Enter para terminar...")
        exit("Programa cerrado.")
        
    print("\nDescargando archivos HTML...\n")
    # Configurar el servicio de Egde con la ruta local al msedgedriver
    service = webdriver.EdgeService(executable_path=str(MSEDGEDRIVER_FILE))
    
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
    
    download_html(driver, url, BANDS_FILE)
    time.sleep(2)
    download_html(driver, url2, RUNNING_FILE)
    # Cerrar el navegador
    driver.quit()

