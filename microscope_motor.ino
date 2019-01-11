

/*
  This is a test sketch for the Adafruit assembled Motor Shield for Arduino v2
  It won't work with v1.x motor shields! Only for the v2's with built in PWM
  control

  For use with the Adafruit Motor Shield v2
  ---->  http://www.adafruit.com/products/1438
*/


#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_MotorShield LightController = Adafruit_MotorShield(0x61);

//L -> R
//Yellow, Orange, NC, Brown, Redaaaaa
Adafruit_StepperMotor * myMotor1 = AFMS.getStepper(200,  1);
Adafruit_StepperMotor *myMotor2 = AFMS.getStepper(200,  2);
Adafruit_DCMotor *light = LightController.getMotor(1);

char inData[80];
byte index = 0;
int step_count[2] = {0, 0};
int brightness = 100;
long step_time;
int delay_time = 20000;
int curMotorPosition = 0;
int newMotorPosition = 0;
int stepsToTake = 0;


void setup() {
  Serial.begin(115200);           // set up Serial library at 9600 bps
  //  Serial.println("Microscope Stepper controller");
  //  Serial.println("q to move up 100 steps and w to move down 100 steps");
  //  Serial.println("a to move up 10 steps and s to move down 10 steps");
  //  Serial.println("z to move up 1 steps and x to move down 1 steps");
  //  Serial.println("1 to increase brightness and 2 to decrease brightness");

  AFMS.begin();  // create with the default frequency 1.6KHz
  LightController.begin();

  //AFMS.begin(1000);  // OR with a different frequency, say 1KHz
  pinMode(3, OUTPUT);
  analogWrite(3, brightness);
  myMotor1->setSpeed(200);  // 10 rpm
  myMotor2->setSpeed(200);
  step_time = millis();

  //for lights
  light->setSpeed(100);
  light->run(FORWARD);
  // turn on motor
  light->run(RELEASE);
}
int val = -1;
char a = 'n';
char b = 'n';
void loop() {
  if (Serial.available() >= 2) {
    a = Serial.read();
    b = Serial.read();
    val = Serial.parseInt();
  }
  //  Serial.println(a);
  //  Serial.println(b);
  //  Serial.println(val, DEC);

  if ( a == 'm') {
    if ((val > -1000) && (val < 1000))
      newMotorPosition = val;
  }
  stepsToTake = newMotorPosition - curMotorPosition;
  if ( stepsToTake > 0) {
    myMotor1->step(1, FORWARD, SINGLE);
    myMotor2->step(1, FORWARD, SINGLE);
    curMotorPosition++;
  }
  else if ( stepsToTake < 0) {
    myMotor1->step(1, BACKWARD, SINGLE);
    myMotor2->step(1, BACKWARD, SINGLE);
    curMotorPosition--;
  }
  else {
    myMotor1->release();
    myMotor2->release();
  }
  if (a == 'l') {
    if (val > 0 && val <= 255) {
      light->setSpeed(val);
      light->run(FORWARD);
    }
    else{
      light->setSpeed(0);
      light->run(RELEASE);
    }
  }

}
