import gpiozero
import time

led = gpiozero.LED(17)  # LED a 17-es GPIO lábon
button = gpiozero.Button(2)  # Nyomógomb a 2-es GPIO lábon

while True:
    if button.is_pressed:
        # Gyorsabb villogás, ha a gomb le van nyomva
        led.on()
        time.sleep(0.1)
        led.off()
        time.sleep(0.1)
    else:
        # Lassabb villogás, ha a gomb nincs lenyomva
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)
