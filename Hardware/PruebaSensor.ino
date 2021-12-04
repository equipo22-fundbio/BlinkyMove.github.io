
#include <PololuQTRSensors.h>
#define NUM_SENSORS             4  // number of sensors used
#define NUM_SAMPLES_PER_SENSOR  2  // averaging
#define EMITTER_PIN             QTR_NO_EMITTER_PIN

int iniSensorValL, sensorValL;
int iniSensorValR, sensorValR;
int iniSensorValLL, sensorValLL;
int iniSensorValRR, sensorValRR;

PololuQTRSensorsAnalog qtra((unsigned char[]) {0, 1,2,3}, NUM_SENSORS, NUM_SAMPLES_PER_SENSOR, EMITTER_PIN);
unsigned int sensorValues[NUM_SENSORS];
void setup() {
 Serial.begin(115200);
 qtra.read(sensorValues);
 iniSensorValL = sensorValues[0];
 iniSensorValR = sensorValues[1];
 iniSensorValLL = sensorValues[2];
 iniSensorValRR = sensorValues[3];
}

void loop() {
 //QTR - 1A sensor value
 qtra.read(sensorValues);
 sensorValL = sensorValues[0]*100;
 sensorValR = sensorValues[1]*100;
 sensorValLL = sensorValues[2];
 sensorValRR = sensorValues[3];

 Serial.print(sensorValL);
 Serial.print(" ,");
 Serial.println(sensorValR);
 Serial.print(sensorValLL);
 Serial.print(" ,");
 Serial.println(sensorValRR);

}
