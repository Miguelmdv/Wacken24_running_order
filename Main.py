import schedule_app.running_order as running_order
from spotipy_app import spotipy_main
import conf_app.config_env as config_env
import schedule_app.data_merge_running_order as data_merge

from conf_app import html_checker

if __name__ == "__main__":
    html_checker.run()
    # Carga las variables de entorno y el numero de personas
    people = config_env.manage_env_file()
    
    spotipy_main.run()
    
    running_order.run()

    data_merge.run(people)
    
    input("\nPresiona Enter para terminar...")
