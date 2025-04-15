import sys
from time import time, perf_counter, sleep
#import wiringpi
#from wiringpi import GPIO
from gpiozero import LED

DATA_LEN = 8
MSG_LEN = 11 # Each message is 1 start bit + 9 Data bits + 1 stop bit
BAUD_RATE = 4800 # DEFAULT: 9600 --- If you change this here, you must also change it on the Teensy
Tx_PIN = 4

#wiringpi.wiringPiSetup()
#wiringpi.pinMode(Tx_PIN, GPIO.OUTPUT)
#wiringpi.digitalWrite(Tx_PIN, GPIO.HIGH)


TURN_MSG  = 0
DIST_MSG  = 1
THROW_MSG = 2

import time

def UARTTrans(MSG_TYPE, msg, Tx_PIN):
    
    if MSG_TYPE == TURN_MSG:
        tx_msg = binaryConvert(msg, 0)
    elif MSG_TYPE == DIST_MSG:
        tx_msg = binaryConvert(msg, 1)
    elif MSG_TYPE == THROW_MSG:
        tx_msg = "111111111111"
    tx_buf = [0] # Insert START bit at beginning
    
    #print("tx_msg", tx_msg)

    # Convert into GPIO-friendly terms
    for i in range(1, MSG_LEN-1): 
        if tx_msg[-i] == "1":
            tx_buf.append(1)
        else:
            tx_buf.append(0)

    tx_buf.append(1) # Insert STOP bit at end
    
    #print("tx_buf", tx_buf)

    # BEGIN TRANSMISSION
    trans_in_prog = True
    i = 0
    bit_timer = perf_counter() + (1 / BAUD_RATE)
    while trans_in_prog:
        tick = perf_counter()
        if bit_timer - tick <= 0:
            if tx_buf[i] == 1:
                Tx_PIN.on()
            elif tx_buf[i] == 0:
                Tx_PIN.off()
            else:
                print("ERR bad tx_buf", tx_buf[i])
            #wiringpi.digitalWrite(Tx_PIN, tx_buf[i])
            i += 1
            bit_timer += 1 / BAUD_RATE
        if i > MSG_LEN-1: 
            trans_in_prog = False

    Tx_PIN.on()
    #wiringpi.digitalWrite(Tx_PIN, GPIO.HIGH) # Ensure pin rests high
    #print("Transmission complete")

        
def binaryConvert(msg, msg_type):
    if msg < 0:
        #print("Neg")
        msg += (1 << DATA_LEN)
    
    num = bin(int(msg))[2:]
    #print("binary", num) 
    num = num.zfill(DATA_LEN) # Pad to length if necessary
    #print("before type:", num)
    out = str(msg_type) + str(num)
    #print("after type:", out)
    return out

#Tx_PIN = LED(24)
#Tx_PIN.on()

#time.sleep(2)

#UARTTrans(0, 55, Tx_PIN)
