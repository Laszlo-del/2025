import gpiozero  # A GPIO könyvtár a Raspberry Pi-hez
import time      # Lehetővé teszi a Python számára az időzítést

led = gpiozero.LED(17) # Referencia a 17-es GPIO-hoz

while True:
    led.on()       # A LED felkapcsolása
    time.sleep(5)  # 5 másodpercig világít

    led.off()      # A LED lekapcsolása
    time.sleep(5)  # 5 másodpercig sötét van
