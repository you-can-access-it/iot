import serial,time
ser=serial.Serial('/dev/serial0',9600,timeout=1)
AUTHORIZED_CARD="400034E6E97B"
print("RFID Access System Ready")
print("Tap your card...")
try:
    while True:
        data=ser.read(12)
        if data:
            card_id=data.decode('utf-8').strip()
            print("Card Detected: "+card_id)
            if card_id==AUTHORIZED_CARD:
                print(" Access Granted — Hello!")
            else:
                print(" Access Denied — Nah!")
            time.sleep(1)
except KeyboardInterrupt:
    print("\nExiting program...")
finally:
    ser.close()
