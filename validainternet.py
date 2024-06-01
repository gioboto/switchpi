import requests
import time
import modulogpioON as ON
import modulogpioOFF as OFF

def hay_conexion():
    url = "http://www.google.com"
    timeout = 5
    try:
        # Intentar realizar una solicitud GET a la URL especificada
        requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False

def accion_sin_conexion():
    print("No hay conexión a internet. Activa relay...") )
    ON.relayon()
    time.sleep(10)
    OFF.relayoff()

if __name__ == "__main__":
    if hay_conexion():
        print("Conexión a internet establecida."))
    else:
        accion_sin_conexion()
