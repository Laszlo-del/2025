from machine import Pin
from time import sleep

# LED beállítása
led = Pin(15, Pin.OUT)

# Főprogram
while True:
    # LED bekapcsolása
    led.on()
    print("LED világít")
    sleep(5)  # 5 másodpercig világít

    # LED kikapcsolása
    led.off()
    print("LED nem világít")
    sleep(5)  # 5 másodpercig sötét van
