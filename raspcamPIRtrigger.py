import os
path = 'raspistill -t 4000 -tl 1000 -o image%d.jpg'
import time
import RPi.GPIO as io
io.setmode(io.BCM)
 
pir_pin = 18

 
io.setup(pir_pin, io.IN)

 
while True:
    if io.input(pir_pin):
        
		os.system (path)
		
    
    time.sleep(0.5)