# Wacken 2024 - Orden de actuación

Leer en [English](./README.md)

Proyecto personal para automatizar el proceso de creación de un calendario personalizado de conciertos del Wacken 2024 en excel, utilizando la información de la web oficial y cruzando los resultados con tus gustos personales de Spotify. 

También la creación de una lista de spotify personalizada en base a tus gustos personales de los artistas del festival.

https://www.wacken.com/en/

**Actualmente WIP** la exportacion a excel y alguna configuracion extra.

## Instalación Facil

### Requisitos

- Usar Windows.

- Necesitarás una cuenta de spotify así como crear una aplicación como desarrollador en su web para tener acceso a las claves API.

    https://developer.spotify.com/dashboard

    1. Una vez creada, escribe en **Redirect URIs**:

        `http://localhost:8080/callback`

        - Esto es sólo para uso local.

    2. A la pregunta, ¿qué API/SDKs piensas utilizar? Marca:

        ***Web API***

    3. Ahora guarda tu ***Client ID***, ***Client Secret*** y tu ***Redirect URI*** para introducirlos más tarde cuando finalmente ejecutes la app.

## Instalación

- Descarga el archivo .zip en su última versión y descomprímelo en su totalidad en cualquier ubicación de tu ordenador, dejándolo dentro de su carpeta original.

- Tienes dos opciones, una sustituye a la otra:

  - Descargar el webdriver de edge:

    - Descargar el archivo y descomprimirlo en la carpeta:
  
        https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

        `C:\webdriver`

    - Añadir al PATH de usuario de windows la misma ruta.

    - **Ventajas**: Solo se realiza una vez.

    - **Desventajas**: Es ligeramente mas complicado que el siguiente paso.

  - Descargar manualmente los html:
  
    -  Mediante el navegador usando el guardar como... , crear una carpeta html dentro de la carpeta original y guarda con el navegador toda la web dentro.

        https://www.wacken.com/en/program/bands/#/

        https://www.wacken.com/en/program/complete-running-order/#/

    - **Ventajas**: Es mas sencillo.

    - **Desventajas**: No se actualiza la informacion y hay que repetir el proceso siempre que se quieran los datos actualizados.

## Uso
   
- Ejecute el archivo ***Main.exe***.
  
   1. (Sólo la primera vez) Introduzca su ***Client ID***, ***Client Secret*** y su ***Redirect URI*** previamente obtenidos cuando se le solicite.

   2. Responda con 'y' o 'n' a las diferentes preguntas. Para una funcionalidad completa, responda siempre con 'y'.

   3. El fichero final con todos los datos se llama ***wacken_running_order_merged.csv***, puedes exportarlo a Excel si quieres.