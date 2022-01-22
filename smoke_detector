import Adafruit_DHT
import sys
import RPi.GPIO as GPIO
import time
import subprocess

#from RPLCD.i2c import CharLCD
#lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,cols=16, rows=2, dotsize=8,charmap='A02',auto_linebreaks=True,backlight_enabled=True)

from gas_detection import GasDetection
smoke_detector = GasDetection()

config = {
    'alarm_level_threshold': 0.02,
    'alarm_update_interval': 60,
    'sensor_reading_delay': 1
}

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4


#GPIO SETUP
#buzz_pin = 27
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(buzz_pin, GPIO.OUT, initial=GPIO.LOW)
#GPIO.setwarnings(False)
#def callback(vibs_pin):

#GPIO.add_event_detect(vibs_pin, GPIO.BOTH, bouncetime=300) # let us know when the pin goes HIGH or LOW
#GPIO.add_event_callback(vibs_pin, callback)  # assign function to GPIO PIN, Run function on change

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        #lcd.clear
        '''lcd.cursor_pos = (0, 0)
        lcd.write_string('Temperature:{0:0.1f} C'.format(temperature))
        lcd.cursor_pos = (1, 0)
        lcd.write_string('Humidity:{0:0.1f} %'.format(humidity))'''
        time.sleep(1)
        ppm = smoke_detector.percentage()
        smoke_value = ppm[smoke_detector.SMOKE_GAS]
        print('Current smoke value: {}'.format(smoke_value))
        if smoke_value > config['alarm_level_threshold']:
            print('!!!!!!!!!!!!!!!FIRE ALARM!!!!!!!!!!!')
            subprocess.call(['sh', './smoke_mail.sh'])
            time.sleep(20)

    else:
        print("Failed to retrieve data from humidity sensor")
