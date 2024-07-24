import apps.conf_app.edgenium as edgenium
from file_paths import BANDS_FILE, RUNNING_FILE


def check():

    while True:
        # Verificar si los archivos HTML no existen
        if not BANDS_FILE.exists() or not RUNNING_FILE.exists():
            print("\nNo existen los archivos HTML en la ruta 'html'.\n")
            print("Quieres descargar los archivos HTML?")
        else:
            print("Quieres actualizar los archivos HTML?")
        
        response = input("Y/N: ")

        if response.lower() == "y":
            try:
                edgenium.run()
                return
            except Exception as e:
                print(f"Error al descargar los archivos html: {e}")
                return
        elif response.lower() == "n":
            # Verificar si los archivos HTML no existen
            if not BANDS_FILE.exists() or not RUNNING_FILE.exists():
                print("\nEn caso de no descargar los archivos, deberás descargarlos por tu cuenta en la carpeta 'html' y el programa se cerrara.\n",)
                while True:
                    response = input("Estas seguro? Y/N: ")
                    if response.lower() == "y":
                        input("\nPresiona Enter para terminar...")
                        exit("Programa cerrado.")
                    elif response.lower() == "n":
                        break
                    else:
                        print(f"'{response}' no es un carácter válido.")
            else:
                break
        else:
            print(f"'{response}' no es un carácter válido.")


def run():
    check()
