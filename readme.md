undetected_crawling

El lanzamiento de la app se realiza a través de: main/ServiceCrawling.

Task:
    - Realizar un Executor.txt con el query deseado y remplazar el query de DBController
    - Realizar un Servicio para homologados
    - Hacer reintentos

Lanzamiento:

    - Importar todas las librerias
    - Ejecutar los comandos:

        Xvfb -ac :99 -screen 0 1280x1024x16 &
        export DISPLAY=:99

      Estos comandos se ejecutan con el fin de generar una pantalla virtual para poder lanzar google-chrome con cabeza


ruta en windows 
CHROME_DRIVER_PATH = 'C:\\Users\\Userr\\spring-workspace\\chromedriver.exe'
      
ruta en ubuntu
CHROME_DRIVER_PATH = '/usr/bin/chromedriver'

