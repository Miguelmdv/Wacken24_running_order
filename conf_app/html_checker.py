import conf_app.edgenium as edgenium
from pathlib import Path


def check():
    html_path = Path("html")
    # Si la carpeta "html" no existe, crearla
    html_path.mkdir(exist_ok=True)
    file1_path = html_path / "Bands _ Wacken Open Air.html"
    file2_path = html_path / "Complete Running Order _ Wacken Open Air.html"

    while True:
        # Verificar si los archivos HTML no existen
        if not file1_path.exists() and not file2_path.exists():
            print("No existen los archivos HTML en la ruta 'html'.\n")
            print("Quieres descargar los archivos HTML?")
        else:
            print("Quieres actualizar los archivos HTML?")
        
        response = input("Y/N: ")

        if response == "Y" or response == "y":
            try:
                edgenium.run()
                return
            except Exception as e:
                print(f"Error al descargar los archivos html: {e}")
                return
        elif response == "N" or response == "n":
            # Verificar si los archivos HTML no existen
            if not file1_path.exists() and not file2_path.exists():
                print(
                    "\nEn caso de no descargar los archivos, deberás descargarlos por tu cuenta en la carpeta 'html'\n",
                    "y el programa se cerrara.\n",
                )
                while True:
                    
                    response = input("Estas seguro? Y/N: ")

                    if response == "Y" or response == "y":
                        input("\nPresiona Enter para terminar...")
                        exit("Programa cerrado.")
                    elif response == "N" or response == "n":
                        break
                    print(f"'{response}' no es un carácter válido.")
            else:
                break
        print(f"'{response}' no es un carácter válido.")


def run():
    check()
