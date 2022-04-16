import socketio
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 21

GPIO.setup(led,GPIO.OUT)

sio = socketio.Client() #logger=True, engineio_logger=True

@sio.event
def connect():
    print('connection established')

@sio.event
def disconnect():
    print('disconnect')

@sio.event
def order_taken(data):
    GPIO.output(led,1)
    time.sleep(0.5)
    GPIO.output(led,0)
    print(data)

def main():
    sio.connect('http://airadrone.herokuapp.com')
    sio.emit("order",{"hola":"prueba"})
    sio.emit("order",{"hola":"prueba1"})
    sio.emit("order",{"hola":"prueba2"})

if __name__=="__main__":
    main()
    

