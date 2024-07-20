# Wacken 2024 - Orden de actuación

Leer en [English](./README.md)

Proyecto personal para automatizar el proceso de creación de un calendario personalizado de conciertos del Wacken 2024 en excel, utilizando la información de la web oficial y cruzando los resultados con tus gustos personales de Spotify. 

También la creación de una lista de spotify personalizada en base a tus gustos personales de los artistas del festival.

https://www.wacken.com/en/

**Actualmente WIP**, con descarga manual de html dinámico e importación de excel.

## Instalación Facil

### Requisitos

- Necesitarás una cuenta de spotify así como crear una aplicación como desarrollador en su web para tener acceso a las claves API.

    https://developer.spotify.com/dashboard

    1. Una vez creada, escribe en **Redirect URIs**:

        `http://localhost:8080/callback`

        - Esto es sólo para uso local.

    2. A la pregunta, ¿qué API/SDKs piensas utilizar? Marca:

        ***Web API***

    3. Ahora guarda tu ***Client ID***, ***Client Secret*** y tu ***Redirect URI*** para introducirlos más tarde cuando finalmente ejecutes la app.

## Instalación

- Descarga el archivo .zip de la última versión y descomprímelo en su totalidad en cualquier ubicación de tu ordenador, dejándolo dentro de su carpeta original.

- Esta configuración es **temporal**, por ahora es **WIP**:

    - Crea una carpeta html dentro de la carpeta, ve a estas urls y guarda con el navegador toda la web dentro.

        https://www.wacken.com/en/program/bands/#/

        https://www.wacken.com/en/program/complete-running-order/#/

## Uso
   
- Ejecute el archivo ***Main.exe***.
  
   1. (Sólo la primera vez) Introduzca su ***Client ID***, ***Client Secret*** y su ***Redirect URI*** previamente obtenidos cuando se le solicite.

   2. Responda con 'y' o 'n' a las diferentes preguntas. Para una funcionalidad completa, responda siempre con 'y'.

   3. El fichero final con todos los datos se llama ***wacken_running_order_merged.csv***, puedes exportarlo a Excel si quieres.

## Tu propia instalación de desarrollo

### Requisitos

1. Para ejecutar este programa necesitas tener instalado al menos miniconda.

    https://docs.anaconda.com/miniconda/miniconda-install/

2. Y necesitarás una cuenta de spotify así como crear una aplicación como desarrollador en su web para tener acceso a las claves API.

    https://developer.spotify.com/dashboard

    1. Una vez creada, escribe en **Redirect URIs**:

        `http://localhost:8080/callback`

        - Esto es sólo para uso local.

    2. A la pregunta, ¿qué API/SDKs piensas utilizar? Marca:

        ***Web API***

    3. Ahora guarda tu ***Client ID***, ***Client Secret*** y tu ***Redirect URI*** para introducirlos más tarde cuando finalmente ejecutes la app.

## Instalación

1. Clona este proyecto en un directorio a tu elección.

2. Ejecuta la consola miniconda e introduzca este comando:

    `conda env create -f environment.yml`

3. Esta configuración es **temporal**, por ahora es **WIP**:

    - Crea una carpeta html dentro de la carpeta, ve a estas urls y guarda con el navegador toda la web dentro.

        https://www.wacken.com/en/program/bands/#/

        https://www.wacken.com/en/program/complete-running-order/#/

## Uso

1. Ejecuta la consola de miniconda e introduce este comando:

    `conda activate wacken24`

2. Navega hasta el directorio del proyecto donde se encuentra el archivo main.py.

3. Una vez en el directorio correcto, ejecute el archivo main.py utilizando el comando python:
   
    `python main.py`

4. (Sólo la primera vez) Introduzca su ***Client ID***, ***Client Secret*** y su ***Redirect URI*** obtenidos previamente cuando se le solicite.

5. Responda con «y» o «n» a las diferentes preguntas. Para una funcionalidad completa, responda siempre con «y».

6. El archivo final con todos los datos se llama ***wacken_running_order_merged.csv***, puede exportarlo a Excel si lo desea.