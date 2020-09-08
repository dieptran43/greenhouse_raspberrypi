try:
    import RPi.GPIO as GPIO
except:
    pass
import time
'''
all try statements only are for using program on main deb machine
'''

RELAIS_GPIO_pump=26
RELAIS_GPIO_fan=19
RELAIS_GPIO_growlights=13
relaydevicelist=[RELAIS_GPIO_pump,RELAIS_GPIO_fan,RELAIS_GPIO_growlights]

try:
    GPIO.setmode(GPIO.BCM) # normal Gpio numbers, not pin numbers
    GPIO.setup(RELAIS_GPIO_pump, GPIO.OUT) # GPIO Modus zuweisen
    GPIO.setup(RELAIS_GPIO_fan, GPIO.OUT) # GPIO Modus zuweisen
    GPIO.setup(RELAIS_GPIO_growlights, GPIO.OUT) # GPIO Modus zuweisen

except:
    pass

def relais(widgidx,bool):
    try:
        if widgidx<=2:
            if bool==True:
                print('Geraet ein')
                GPIO.output(relaydevicelist[widgidx], GPIO.HIGH)
            else:
                print('geraet aus')
                GPIO.output(relaydevicelist[widgidx], GPIO.LOW)
    except:
        pass

def cleanclose():
    print('hi')
    try:                                                                        #try only is for using program on main deb machine
        print('Ich geh hier rein!')

        GPIO.output(relaydevicelist, GPIO.LOW)
        GPIO.cleanup()
        print('gehst du hier wirklich rein?')
    except:
        pass