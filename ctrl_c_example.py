import threading
import time

HILOS_EJECUTANDO = True

def hilo():
    while HILOS_EJECUTANDO:
        print("ejecutando bucle hilo()")
        time.sleep(1)

def hilo2():
    while HILOS_EJECUTANDO:
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
        HILOS_EJECUTANDO = False
        x.join()
        y.join()
        print("final de los hilos detectado")
