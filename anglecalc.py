import serial
import math

#x-coordinate = 0.0
y_coordinate = 
#truex = x_coordinate*30/600
truey = y_coordinate*16/600
refrencenumber = 1300
radius = 
ycam = 0.0
cameratoobject = refrencenumber/radius
#if truey <= 8:
   
 #   end if
    
    
if truey > 8:    
    ycam = truey - 8
    z = ((cameratoobject)**2-ycam**2)**0.5
    verticaleangle = math.atan2(ycam, z)
    angle = math.degrees(verticalangle) + 90


else:
    ycam = 8 - truey
    z = ((cameratoobject)**2-ycam**2)**0.5#-ycam**2)#**0.5
    verticalangle = math.atan2(z, ycam)
    angle = math.degrees(verticalangle)

print (angle)
    
val = angle
#6SB = int(math.floor(val %  1000000))
#5SB = int(math.floor((val % 100000 )/10000))
#4SB = int(math.floor((val % 10000))/1000)
MSB = int(math.floor((val % 1000)/100))
ISB = int(math.floor((val % 100) / 10))
LSB = val % 10

print(MSB)
print(ISB)
print(LSB)
ser.write(str(MSB))
sleep(0.5)
ser.write(str(ISB))
sleep(0.5)
ser.write(str(LSB))


#D = 2.0
 #and truex 
    