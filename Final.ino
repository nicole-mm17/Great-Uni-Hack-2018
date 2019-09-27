#include <Servo.h>

Servo X_Servo;
Servo Y_Servo;

short int i = 0;
int theta = 0;
int oldx = 0;


void setup() {
  X_Servo.attach(9);
  Y_Servo.attach(10);
  Serial.begin(9600);
}


void loop() {
  char inputNUM;
  int num;

  if (Serial.available()) {
    inputNUM = Serial.read();
    num = (int)inputNUM - 48;
    Serial.println("NUM");
    Serial.println(inputNUM);
    if ( i == 0 ) theta = num * 100;
    if ( i == 1 ) theta += num * 10;
    if ( i == 2 ) theta += num;
    Serial.println("theta");
    Serial.println(theta);
    i++;

    if (i == 3) {
      if (theta >= oldx){
        Serial.print(theta); Serial.print('\t'); Serial.println(oldx);
        for (int k= oldx; k <= theta; k++){
         Serial.println(k);
         X_Servo.write(60);
         delay(2);
        }
      }
//Serial.println("I'm going up");
 //       oldx = theta;
        //delay(720);
     // }
      else if(theta <= oldx){
          for (int k= oldx; k >= theta; k--){
            X_Servo.write(120);
            delay(2);
          }
          //X_Servo.write(theta);
          //Serial.println("I'm coming down");
        oldx = theta;
      }
      i = 0;
    }
  }
}
