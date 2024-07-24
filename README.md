# Wacken 2024 - Running order

Read in [Español](./LEEME.md)

Personal project to automate the process of creating a personalized calendar of concerts of wacken 2024 in excel, using information from the official website and crossing the results with your personal likes from Spotify. 

Also the creation of a personalized spotify list based on personal tastes of the artists of the festival.

https://www.wacken.com/en/


## Easy Installation

### Requirements

- Use Windows.

- You will need a spotify account as well as creating an app as a developer on their website to have access to the API keys.

    https://developer.spotify.com/dashboard

    1. Once you have created it, type in **Redirect URIs**:

        `http://localhost:8080/callback`

        - This is for local use only.

    2. To the question, which API/SDKs are you planning to use? Check:

        ***Web API***

    3. Now just save your ***Client ID***, ***Client Secret*** and your ***Redirect URI*** to enter them later when you finally run the app.

## Installation

- Download the .zip file in its latest version and unzip it entirely to any location on your computer, leaving it inside its original folder.

- You have two options, one replaces the other:

  - Download the webdriver from edge:

    - Download the file and unzip it into the folder:
  
        https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

        `C:\webdriver`

    - Add to the windows user PATH the same path.

    - **Advantages**: It is only done once.

    - **Disadvantages**: It is slightly more complicated than the next step.

  - Manually download the html files:
  
    - Through the browser using the save as.... create an html folder inside the original folder and save with the browser all the web inside.

        https://www.wacken.com/en/program/bands/#/

        https://www.wacken.com/en/program/complete-running-order/#/

    - **Advantages**: It is simpler.

    - **Disadvantages**: The information is not updated and you have to repeat the process whenever you want the updated data.

## Usage
   
- Run the ***Main.exe*** file.
  
   1. (First time only) Enter your previously obtained ***Client ID***, ***Client Secret*** and your ***Redirect URI*** when prompted.

   2. Answer with 'y' or 'n' to the different questions. For full functionality, always answer 'y'.

   3. The final file with all the data is in ***data*** folder and is called ***wacken_running_order_merged.csv***, you can export it to Excel if you want.