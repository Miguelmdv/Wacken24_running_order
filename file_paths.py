from pathlib import Path
import os

BASE_DIR = Path("")


DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

ALL_ART_W_C_FILE = DATA_DIR / "all_liked_artists_wacken_with_count.csv"
BAND_LIST_FILE = DATA_DIR / "band_list.csv"
ART_SPO_C_FILE = DATA_DIR / "liked_artists_spoti_with_count.csv"
ART_WA_C_FILE = DATA_DIR / "liked_artists_wacken_with_count.csv"
RUN_ORD_MERGED_FILE = DATA_DIR / "wacken_running_order_merged.csv"
RUN_ORD_VOID_FILE = DATA_DIR / "wacken_running_order_void.csv"
RUN_ORD_FILE = DATA_DIR / "wacken_running_order.csv"


HTML_DIR = BASE_DIR / "html"
HTML_DIR.mkdir(exist_ok=True)

BANDS_FILE = HTML_DIR / "Bands _ Wacken Open Air.html"
RUNNING_FILE = HTML_DIR / "Complete Running Order _ Wacken Open Air.html"


ENV_FILE = BASE_DIR / ".env"

CACHE_FILE = BASE_DIR / ".cache"


DRIVER_DIR = Path("C:/webdriver").resolve()
MSEDGEDRIVER_FILE = DRIVER_DIR / "msedgedriver.exe"


# Obtener el valor de la variable de entorno PATH
PATH_OS = os.environ.get('PATH', '')
# Dividir el PATH en las diferentes rutas
PATH_DIRS = PATH_OS.split(os.pathsep)

EXCEL_FILE = BASE_DIR / "Final Running Order Wacken24.xlsx"
