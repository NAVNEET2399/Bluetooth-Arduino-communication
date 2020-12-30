import serial
import time
print("Starting Communication between Bluetooth and python")
port = "COM21"    # specify the com port  - check the COM Port in Device manager (Windows)
while True:
    try:
        bluetooth = serial.Serial(port, 9600)    #create instance of Serial communication
        print("Connection Established")
        break
    except:
        print("Waiting for Connection")
        pass
        
def readData():
    raw_data = bluetooth.readline()
    data = input_data.decode()
    print(data)
    time.sleep(1)

readData()
