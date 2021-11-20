#include <SoftwareSerial.h>
#include <PololuQTRSensors.h>

#define NUM_SENSORS             2  // number of sensors used
#define NUM_SAMPLES_PER_SENSOR  10  // average 4 analog samples per sensor reading

int iniSensorValL, sensorValL;
int iniSensorValR, sensorValR;
// sensors 0 through 5 are connected to analog inputs 0 through 5, respectively
PololuQTRSensorsAnalog qtra((unsigned char[]) {0, 1}, 
  NUM_SENSORS, NUM_SAMPLES_PER_SENSOR);
unsigned int sensorValues[NUM_SENSORS];

int LR = 7;
boolean lid = false;
int cnt = 0;

void setup() {
 Serial.begin(115200);
 qtra.read(sensorValues);
 iniSensorValL = sensorValues[0];
 iniSensorValR = sensorValues[1];
}

void loop() {
 //QTR - 1A sensor value
 qtra.read(sensorValues);
 sensorValL = sensorValues[0];
 sensorValR = sensorValues[1];

 double rasioL = (double)sensorValL / iniSensorValL;
 double rasioR = (double)sensorValR / iniSensorValR;

 Serial.print(rasioL);
 Serial.print("  ");
 Serial.println(rasioR);

 if(rasioL > 0.985 && rasioR < 0.985){ //right
   for(int i = LR; i < 12; i++){
     delay(40);
     LR = i;
   }
 }else if(rasioL < 0.985 && rasioR > 0.985){ //left
   for(int i=LR; i>2; i--){
     delay(40);
     LR = i;
   }
 }else if(lid == false && rasioL < 0.96 && rasioR < 0.96){ //Blinking close
   for(int i = 1; i < 9; i++){
     delay(40);
     lid = true;
   }
 }else if(lid == true && rasioL > 0.96 && rasioR > 0.96){ //Blinking open
   for(int i = 8; i > 0; i--){
     delay(40);
     lid = false;
   }
 }else if(lid == false && rasioL > 0.96 && rasioR > 0.96) {   //normal
   //cnt++;
   //eyelid = 0;
   if(LR <= 7){
     for(int i=LR; i<=7; i++){
       delay(40);
       LR = i;
     }
   }else {
     for(int i=LR; i>=7; i--){
       delay(40);
       LR = i;
     }
   }
 }


 //Initial value refresh
 if (cnt > 10){
   iniSensorValL = sensorValL;
   iniSensorValR = sensorValR;
   cnt = 0;
 }
}
