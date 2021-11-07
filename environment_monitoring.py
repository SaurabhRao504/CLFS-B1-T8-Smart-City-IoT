import Adafruit_DHT
import sys
import RPi.GPIO as GPIO
import time

from RPLCD.i2c import CharLCD
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,cols=16, rows=2, dotsize=8,charmap='A02',auto_linebreaks=True,backlight_enabled=True)

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

#GPIO SETUP
vibs_pin = 17
buzz_pin = 27
flame_pin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(vibs_pin, GPIO.IN)
GPIO.setup(buzz_pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(flame_pin, GPIO.IN)
#def callback(vibs_pin):

#GPIO.add_event_detect(vibs_pin, GPIO.BOTH, bouncetime=300) # let us know when the pin goes HIGH or LOW
#GPIO.add_event_callback(vibs_pin, callback)  # assign function to GPIO PIN, Run function on change

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string('Temperature:{0:0.1f} C'.format(temperature))
        lcd.cursor_pos = (1, 0)
        lcd.write_string('Humidity:{0:0.1f} %'.format(humidity))
        time.sleep(1)
        lcd.clear()
        if GPIO.input(vibs_pin):
            lcd.clear()
            lcd.cursor_pos=(0, 0)
            lcd.write_string("Earthquake!")
            print("earthquake")
            GPIO.output(buzz_pin, GPIO.HIGH)
            time.sleep(4)
            GPIO.output(buzz_pin, GPIO.LOW)
        elif GPIO.input(flame_pin):
            lcd.clear()
            lcd.cursor_pos=(0, 0)
            lcd.write_string("Fire!")
            print("fire")
            GPIO.output(buzz_pin, GPIO.HIGH)
            time.sleep(4)
            GPIO.output(buzz_pin, GPIO.LOW)
    else:
        print("Failed to retrieve data from humidity sensor")
