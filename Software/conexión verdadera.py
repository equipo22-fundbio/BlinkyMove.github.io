import serial, time
ard = serial.Serial ('COM3', 9600)
datos = ard.readline()
while 1:
    print(datos.decode('utf-8'))
    time.sleep(3)
