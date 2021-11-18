import serial
from serial import serial
import string, time, pyrebase
ser = serial.Serial('/dev/ttyUSB0')
ser.baudrate=300

config = {
    "apiKey": "3eVfh80gD4Gkx8oeoowsl17a5jnU46wXBIOT2iGJ",
    "authDomain": "monitordistancechecker.firebaseapp.com",
    "databaseURL": "https://monitordistancechecker-default-rtdb.europe-west1.firebasedatabase.app",
    "storageBucket": "monitordistancechecker.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

while True:
    if ser.in_waiting > 0:
        rawserial = ser.readline()
        serialdata = rawserial.decode('utf-8').strip('\r\n')
        print(serialdata)
        db.update({"SensorData":serialdata})