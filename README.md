# Wacken 2024 running order

Personal project to automate the process of creating a personalized calendar of concerts of a festival in excel, using information from the official website and crossing the results with your personal likes from spotify. 

Also the creation of a personalized spotify list based on personal tastes of the artists of the festival.

https://www.wacken.com/en/

**Currently WIP**, with manual dynamic html download and excel import.

## Requirements

1. To run this program you need to have at least miniconda installed.

    https://docs.anaconda.com/miniconda/miniconda-install/

2. And you will need a spotify account as well as creating an app as a developer on their website to have access to the API keys.

    https://developer.spotify.com/dashboard

    1. Once you have created it, type in **Redirect URIs**:

        `http://localhost:8080/callback`

        - This is for local use only.

    2. To the question, which API/SDKs are you planning to use? Check:

        ***Web API***

    3. Now just save your ***Client ID***, ***Client Secret*** and your ***Redirect URI*** to enter them later when you finally run the app.

## Installation

1. Clone this project to a directory of your choice.

2. Run miniconda console and enter this command:

    `conda env create -f environment.yml`

3. This configuration is **temporary** for now, it is **WIP**:

   1. Create an html folder inside spotipy_app, go to this url and save with the browser the whole web inside.

        https://www.wacken.com/en/program/bands/#/

   2. Create an html folder inside the main folder, go to this url and save with the browser the whole web inside.

        https://www.wacken.com/en/program/running-order-music/#/

## Usage

1. Run miniconda console and enter this command:

    `conda activate wacken24`

2. Navigate to the project directory where main.py file is located.

3. Once in the correct directory, execute the main.py file using the python command:
   
    `python main.py`

4. (First time only) Enter your previously obtained ***Client ID***, ***Client Secret*** and your ***Redirect URI*** when prompted.

5. Answer with “y” or “n” to the different questions. For full functionality, always answer “y”.

6. The final file with all the data is called ***wacken_running_order_merged.csv***, you can export it to Excel if you want.