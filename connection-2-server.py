import socketio
sio = socketio.Client(logger=True, engineio_logger=True)

@sio.event
def connect():
    print('connection established')

@sio.event
def disconnect():
    print('disconnect')

@sio.event
def order_taken(data):
    print(data)

def main():
    sio.connect('http://localhost:3000')
    sio.emit("order",{"hola":"prueba"})
    sio.emit("order",{"hola":"prueba1"})
    sio.emit("order",{"hola":"prueba2"})

if __name__=="__main__":
    main()
    

