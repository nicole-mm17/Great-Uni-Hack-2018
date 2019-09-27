import math
import serial

x = 7.0
y = 0.0 # y-coordinate from camera
S_c = 0.5 # Current size on camera
D = 1.0 # Distance between laser and camera (assuming in the y-direction)
S_r = 1.0 # Refrence size of object  
d_r = 1.0 # Refrence distance where the object is at the refrence size

d_c = (S_r * d_r)/ S_c # Current distance between camera and object
z = ((d_c)**2 - (x**2) - y**2)**0.5 # z-direction distance
print(z)
z = 3

theta = math.atan2(x, z) # Vertical angle in Radians 
print (theta)

theta = math.degrees(theta) # Vertical angle in Degrees
print (theta)

y_l = y + D # Distance between laser and object in y-direction

d_l = (x**2 + y_l**2 + z**2)**0.5 # Distance between laser and object (a bit useless rn)
print (d_l)

phi = math.atan2(y_l, z) # Horizontal angle in Radians
print (phi)

phi = math.degrees(phi) # Horizontal angle in Degrees
print (phi)

