from smbus import SMBus
import math
import time
import backlight
import screen
import os
import RPi.GPIO as GPIO
from time import sleep
pushed1 = 0
pushed2 = 0
pushed3 = 0
pushed4 = 0
pushed5 = 0
pushed6 =0
output = ''
total_output = ''
total_output2 = ''
line = 0
pushedC = 0

class Display(object):
    backlight = None
    screen = None

    def __init__(self, bus):
        self.backlight = backlight.Backlight(bus, 0x62)
        self.screen    = screen.Screen(bus, 0x3e)

    def write(self, text):
        self.screen.write(text)

    def color(self, r, g, b):
        self.backlight.set_color(r, g, b)

    def move(self, col, row):
        self.screen.setCursor(col, row)

def button_callback1(channel):
    global pushed1
    pushed1 = 1
    
    
def button_callback2(channel):
    global pushed2
    pushed2 = 1

    
def button_callback3(channel):
    global pushed3
    pushed3 = 1
    
def button_callback4(channel):
    global pushed4
    pushed4 = 1
    
def button_callback5(channel):
    global pushed5
    pushed5 = 1

def button_callback6(channel):
    global pushed6
    pushed6 = 1

def button_callbackD(channel):
    global total_output
    global total_output2
    global line
    if(line == 0):
        if(len(total_output)>0):
            total_output = total_output[0:len(total_output)-1]
            d = Display(SMBus(1))
            d.move(0, line)
            d.write(total_output)
    else:
        if(len(total_output2)>0):
            total_output2 = total_output2[0:len(total_output2)-1]
            d = Display(SMBus(1))
            d.move(0, line)
            d.write(total_output2)    
    
def button_callbackS(channel):
    global total_output
    global total_output2
    global line
    if(line == 0):
        total_output = total_output + ' '
        d = Display(SMBus(1))
        d.move(0, line)
        d.write(total_output)
    else:
        total_output2 = total_output2 + ' '
        d = Display(SMBus(1))
        d.move(0, line)
        d.write(total_output2)      
    
def button_callbackE(channel):
    global line
    if(line == 0):
        line = 1
    else:
        line = 0
    
def button_callbackC(channel):
    global pushedC
    if(pushedC==0):
        pushedC = 1
    else:
        pushedC = 0
    
    
def button_callbackR(channel):
    global line
    global total_output
    global total_output2
    if(line == 0):
        F=total_output
    else:
        F=total_output2
    os.system('echo %s | festival --tts %F)


def button_callback0():
    global pushed1
    global pushed2
    global pushed3
    global pushed4
    global pushed5
    global pushed6
    global output
    global total_output
    global total_output2
    global line
    global pushedC
    
    
    if (pushedC==0):
        if (pushed1==1) and (pushed2==0) and (pushed3==0) and (pushed4==0) and (pushed5==0) and (pushed6==0):
            output = 'a'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==1) and (pushed4==0) and (pushed5==0) and (pushed6==0):
            output = 'b'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==0) and (pushed4==0) and (pushed5==0) and (pushed6==0):
            output = 'c'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==0) and (pushed4==1) and (pushed5==0) and (pushed6==0):
            output = 'd'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==0) and (pushed4==1) and (pushed5==0) and (pushed6==0):
            output = 'e'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==1) and (pushed4==0) and (pushed5==0) and (pushed6==0):
            output = 'f'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==1) and (pushed4==1) and (pushed5==0) and (pushed6==0):
            output = 'g'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==1) and (pushed4==1) and (pushed5==0) and (pushed6==0):
            output = 'h'
            
        if (pushed1==0) and (pushed2==1) and (pushed3==1) and (pushed4==0) and (pushed5==0) and (pushed6==0):
            output = 'i'
            
        if (pushed1==0) and (pushed2==1) and (pushed3==1) and (pushed4==1) and (pushed5==0) and (pushed6==0):
            output = 'j'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==0) and (pushed4==0) and (pushed5==1) and (pushed6==0):
            output = 'k'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==1) and (pushed4==0) and (pushed5==1) and (pushed6==0):
            output = 'l'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==0) and (pushed4==0) and (pushed5==1) and (pushed6==0):
            output = 'm'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==0) and (pushed4==1) and (pushed5==1) and (pushed6==0):
            output = 'n'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==0) and (pushed4==1) and (pushed5==1) and (pushed6==0):
            output = 'o'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==1) and (pushed4==0) and (pushed5==1) and (pushed6==0):
            output = 'p'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==1) and (pushed4==1) and (pushed5==1) and (pushed6==0):
            output = 'q'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==1) and (pushed4==1) and (pushed5==1) and (pushed6==0):
            output = 'r'
            
        if (pushed1==0) and (pushed2==1) and (pushed3==1) and (pushed4==0) and (pushed5==1) and (pushed6==0):
            output = 's'
            
        if (pushed1==0) and (pushed2==1) and (pushed3==1) and (pushed4==1) and (pushed5==1) and (pushed6==0):
            output = 't'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==0) and (pushed4==0) and (pushed5==1) and (pushed6==1):
            output = 'u'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==1) and (pushed4==0) and (pushed5==1) and (pushed6==1):
            output = 'v' 
             
        if (pushed1==1) and (pushed2==0) and (pushed3==1) and (pushed4==0) and (pushed5==1) and (pushed6==1):
            output = 'w'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==0) and (pushed4==0) and (pushed5==1) and (pushed6==1):
            output = 'x'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==0) and (pushed4==1) and (pushed5==1) and (pushed6==1):
            output = 'y'
        
        if (pushed1==1) and (pushed2==0) and (pushed3==0) and (pushed4==1) and (pushed5==1) and (pushed6==1):
            output = 'z'
            
        if (pushed1==0) and (pushed2==1) and (pushed3==0) and (pushed4==1) and (pushed5==1) and (pushed6==1):
            output = '0'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==0) and (pushed4==0) and (pushed5==0) and (pushed6==1):
            output = '1'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==1) and (pushed4==0) and (pushed5==0) and (pushed6==1):
            output = '2'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==0) and (pushed4==0) and (pushed5==0) and (pushed6==1):
            output = '3'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==0) and (pushed4==1) and (pushed5==0) and (pushed6==1):
            output = '4'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==0) and (pushed4==1) and (pushed5==0) and (pushed6==1):
            output = '5'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==1) and (pushed4==0) and (pushed5==0) and (pushed6==1):
            output = '6'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==1) and (pushed4==1) and (pushed5==0) and (pushed6==1):
            output = '7'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==1) and (pushed4==1) and (pushed5==0) and (pushed6==1):
            output = '8'
            
        if (pushed1==0) and (pushed2==1) and (pushed3==1) and (pushed4==0) and (pushed5==0) and (pushed6==1):
            output = '9'
            
    if (pushedC==1):
        if (pushed1==1) and (pushed2==0) and (pushed3==0) and (pushed4==0) and (pushed5==0) and (pushed6==0):
            output = 'A'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==1) and (pushed4==0) and (pushed5==0) and (pushed6==0):
            output = 'B'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==0) and (pushed4==0) and (pushed5==0) and (pushed6==0):
            output = 'C'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==0) and (pushed4==1) and (pushed5==0) and (pushed6==0):
            output = 'D'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==0) and (pushed4==1) and (pushed5==0) and (pushed6==0):
            output = 'E'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==1) and (pushed4==0) and (pushed5==0) and (pushed6==0):
            output = 'F'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==1) and (pushed4==1) and (pushed5==0) and (pushed6==0):
            output = 'G'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==1) and (pushed4==1) and (pushed5==0) and (pushed6==0):
            output = 'H'
            
        if (pushed1==0) and (pushed2==1) and (pushed3==1) and (pushed4==0) and (pushed5==0) and (pushed6==0):
            output = 'I'
            
        if (pushed1==0) and (pushed2==1) and (pushed3==1) and (pushed4==1) and (pushed5==0) and (pushed6==0):
            output = 'J'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==0) and (pushed4==0) and (pushed5==1) and (pushed6==0):
            output = 'K'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==1) and (pushed4==0) and (pushed5==1) and (pushed6==0):
            output = 'L'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==0) and (pushed4==0) and (pushed5==1) and (pushed6==0):
            output = 'M'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==0) and (pushed4==1) and (pushed5==1) and (pushed6==0):
            output = 'N'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==0) and (pushed4==1) and (pushed5==1) and (pushed6==0):
            output = 'O'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==1) and (pushed4==0) and (pushed5==1) and (pushed6==0):
            output = 'P'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==1) and (pushed4==1) and (pushed5==1) and (pushed6==0):
            output = 'Q'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==1) and (pushed4==1) and (pushed5==1) and (pushed6==0):
            output = 'R'
            
        if (pushed1==0) and (pushed2==1) and (pushed3==1) and (pushed4==0) and (pushed5==1) and (pushed6==0):
            output = 'S'
            
        if (pushed1==0) and (pushed2==1) and (pushed3==1) and (pushed4==1) and (pushed5==1) and (pushed6==0):
            output = 'T'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==0) and (pushed4==0) and (pushed5==1) and (pushed6==1):
            output = 'U'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==1) and (pushed4==0) and (pushed5==1) and (pushed6==1):
            output = 'V' 
             
        if (pushed1==1) and (pushed2==0) and (pushed3==1) and (pushed4==0) and (pushed5==1) and (pushed6==1):
            output = 'W'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==0) and (pushed4==0) and (pushed5==1) and (pushed6==1):
            output = 'X'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==0) and (pushed4==1) and (pushed5==1) and (pushed6==1):
            output = 'Y'
        
        if (pushed1==1) and (pushed2==0) and (pushed3==0) and (pushed4==1) and (pushed5==1) and (pushed6==1):
            output = 'Z'
            
        if (pushed1==0) and (pushed2==1) and (pushed3==0) and (pushed4==1) and (pushed5==1) and (pushed6==1):
            output = '0'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==0) and (pushed4==0) and (pushed5==0) and (pushed6==1):
            output = '1'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==1) and (pushed4==0) and (pushed5==0) and (pushed6==1):
            output = '2'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==0) and (pushed4==0) and (pushed5==0) and (pushed6==1):
            output = '3'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==0) and (pushed4==1) and (pushed5==0) and (pushed6==1):
            output = '4'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==0) and (pushed4==1) and (pushed5==0) and (pushed6==1):
            output = '5'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==1) and (pushed4==0) and (pushed5==0) and (pushed6==1):
            output = '6'
            
        if (pushed1==1) and (pushed2==1) and (pushed3==1) and (pushed4==1) and (pushed5==0) and (pushed6==1):
            output = '7'
            
        if (pushed1==1) and (pushed2==0) and (pushed3==1) and (pushed4==1) and (pushed5==0) and (pushed6==1):
            output = '8'
            
        if (pushed1==0) and (pushed2==1) and (pushed3==1) and (pushed4==0) and (pushed5==0) and (pushed6==1):
            output = '9'
        
    if (pushed1!=0) or (pushed2!=0) or (pushed3!=0) or (pushed4!=0) or (pushed5!=0) or (pushed6!=0):
        if(line == 0):
            d = Display(SMBus(1))
            d.move(0, 1)
            d.write(total_output2)
            total_output += output
            d.move(0, 0)
            d.write(total_output) 
            
        if(line == 1):
            d = Display(SMBus(1))
            d.move(0, 0)
            d.write(total_output)
            total_output2 += output
            d.move(0, 1)
            d.write(total_output2)           
        pushed1=0
        pushed2=0
        pushed3=0
        pushed4=0
        pushed5=0
        pushed6=0
        pushedC=0
        output=""


if __name__ == "__main__":
    cnt = 0
    
    button_pin1 = 15
    button_pin2 = 16
    button_pin3 = 17
    button_pin4 = 18
    button_pin5 = 19
    button_pin6 = 20
    button_pinD = 10
    button_pinS = 11
    button_pinE = 12   
    button_pinC = 13
    button_pinR = 14
    
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(button_pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(button_pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(button_pin3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(button_pin4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(button_pin5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(button_pin6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
    GPIO.setup(button_pinD, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(button_pinS, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(button_pinE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(button_pinC, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    GPIO.add_event_detect(button_pin1, GPIO.RISING, callback=button_callback1, bouncetime=300)
    GPIO.add_event_detect(button_pin2, GPIO.RISING, callback=button_callback2, bouncetime=300)
    GPIO.add_event_detect(button_pin3, GPIO.RISING, callback=button_callback3, bouncetime=300)
    GPIO.add_event_detect(button_pin4, GPIO.RISING, callback=button_callback4, bouncetime=300)
    GPIO.add_event_detect(button_pin5, GPIO.RISING, callback=button_callback5, bouncetime=300)
    GPIO.add_event_detect(button_pin6, GPIO.RISING, callback=button_callback6, bouncetime=300)
    GPIO.add_event_detect(button_pinD, GPIO.RISING, callback=button_callbackD, bouncetime=300)
    GPIO.add_event_detect(button_pinS, GPIO.RISING, callback=button_callbackS, bouncetime=300)
    GPIO.add_event_detect(button_pinE, GPIO.RISING, callback=button_callbackE, bouncetime=300)
    GPIO.add_event_detect(button_pinC, GPIO.RISING, callback=button_callbackC, bouncetime=300)
    GPIO.add_event_detect(button_pinR, GPIO.RISING, callback=button_callbackR, bouncetime=2000)
    
    
    while 1:
        time.sleep(0.5)
        if (pushed1==1) or (pushed2==1) or (pushed3==1) or (pushed4==1) or (pushed5==1) or (pushed6==1):
            button_callback0()







