# Great Uni Hack 18
### Repo for Great Uni Hack Manchester 2018 MLH Hackathon

*10-11 November 2018*

## We made a real-time object-tracking setup utilising the following hardware:
* Raspberry Pi Model 3B
* PiCam v2.0
* Arduino for TTL-to-PWM conversion
* servos
* and (most importantly) a LASER!

### The objective of our hack is to create a demo of a real-time object tracking system, which can be deployed on existing CCTV hardware in order to track wristbands/markers etc in the public.

### The target audience is organisations wishing to track and be aware of vulnerable people in crowds. (The laser is just a cool add-on to make you go wow ;D ).

![demo](https://github.com/MNahad/great-uni-hack-18/blob/master/assets/demo.gif)

## We won the hardware track and then went on to beat all other tracks to win the grand prize!

![laser](https://github.com/MNahad/great-uni-hack-18/blob/master/assets/laser.gif)

## Code

*Final code is available in src*

Code is shown to work on Raspbian Jessie and Stretch.

## Software Prerequisites
* Python 2 (cannot run on Python 3 ;( )

*The following Python libs*:
* collections
* numpy
* argparse
* imutils
* cv2
* math
* time (Pi specific)
* serial (Pi specific)

## Known issues and workarounds
On old Raspbian Jessie versions, the specific module needed for cv2.VideoCapture() to access the camera stream does not load on bootup. We certainly spent a few good hours through the night troubleshooting this ;D .

Issue can be prevented by downloading (or building) then adding the following module in */etc/modules*:

*bcm2835-v4l2*
