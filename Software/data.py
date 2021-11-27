import serial
import time
import schedule


def main_func():
    sensorData = serial.Serial('COM4', 9600)
    print('conexión establecida con bluetooth')
    DatoLeido = sensorData.readline()  # Guardamos el dato leido por el puerto

    DatoDecodificado = str(DatoLeido[0:len(DatoLeido)].decode("utf-8"))
    DatoSeparado = DatoDecodificado.split(";")  # Aqui se establece el delimitador para separarlo

    Sensor1 = DatoSeparado[0]
    Sensor2 = DatoSeparado[1]
    Sensor3 = DatoSeparado[2]
    Sensor4 = DatoSeparado[3]

    for item in DatoSeparado:
        Sensor1.append(float(item))
        Sensor2.append(float(item))
        Sensor3.append(float(item))
        Sensor4.append(float(item))

    print("Data coleccionada de bluetooth: " + Sensor1 + ";" + Sensor2 + ";" + Sensor3 + ";" + Sensor4)

    DatoLeido = 0
    Sensor1.clear()
    Sensor2.clear()
    Sensor3.clear()
    Sensor4.clear()
    DatoSeparado.clear()
    sensorData.close()
    print("Conexión cerrada")
    print("--------------------->")


# ----------------------------------------Main Code------------------------------------

# Declaración de variables a usar

DatoSeparado = [0, 0, 0, 0]
Sensor1 = DatoSeparado[0]
Sensor2 = DatoSeparado[1]
Sensor3 = DatoSeparado[2]
Sensor4 = DatoSeparado[3]

print("Comienzo de programa")

# Set up de bluetooth
schedule.every(10).seconds.do(main_func)

while True:
    schedule.run_pending()
    time.sleep(1)




