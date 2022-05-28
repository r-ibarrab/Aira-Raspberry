import socketio
# import RPi.GPIO as GPIO
import time

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)

# 

# GPIO.setup(led,GPIO.OUT)

sio = socketio.Client(logger=True, engineio_logger=True) #logger=True, engineio_logger=True

@sio.event
def connect():
    print('connection established')

@sio.event
def disconnect():
    print('disconnect')

def my_background_task(myArgument):
    c = 0;
    while True:
        try:
            c+=1
            plant_data = {
                "humidity":c,
                "temperature":c,
                "soilHumidity":c,
                "light":c,
                "water":c,
            }
            
            sio.emit("plantData",plant_data)
            time.sleep(10)
        except:
            break
      
    pass

def main():
    sio.connect('http://localhost:3001/')
    task = sio.start_background_task(my_background_task, 123)
   
if __name__=="__main__":
    main()
    

