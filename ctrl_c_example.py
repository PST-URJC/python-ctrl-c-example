import threading
import time

hilos_ejecutando = True

def hilo():   
    while hilos_ejecutando:
        print("ejecutando bucle hilo()")
        time.sleep(1)

def hilo2():   
    while hilos_ejecutando:
        print("ejecutando bucle hilo2()")
        time.sleep(2)

        
if __name__ == "__main__":
    x = threading.Thread(target=hilo, args=())
    y = threading.Thread(target=hilo2, args=())
    x.start()
    y.start()
    # espero hilo
    try:
        x.join()
        y.join()
    except KeyboardInterrupt:
        hilos_ejecutando = False
        x.join()
        y.join()
        print("final de los hilos detectado")