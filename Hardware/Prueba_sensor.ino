#include <PololuQTRSensors.h>
#define NUM_SENSORS             2  // number of sensors used
#define NUM_SAMPLES_PER_SENSOR  4  // average 4 analog samples per sensor reading
          
// sensors 0 through 5 are connected to analog inputs 0 through 5, respectively
PololuQTRSensorsAnalog qtra((unsigned char[]) {14,15}, NUM_SENSORS, NUM_SAMPLES_PER_SENSOR);
unsigned int sensorValues[NUM_SENSORS];


void setup()
{
  delay(500);
  int i;
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);    // turn on LED to indicate we are in calibration mode
  for (i = 0; i < 400; i++)  // make the calibration take about 10 seconds
  {
    qtra.calibrate();       // reads all sensors 10 times at 2.5 ms per six sensors (i.e. ~25 ms per call)
  }
  digitalWrite(13, LOW);     // turn off LED to indicate we are through with calibration

  // print the calibration minimum values measured when emitters were on
  Serial.begin(9600);
  for (i = 0; i < NUM_SENSORS; i++)
  {
    Serial.print(qtra.calibratedMinimumOn[i]);
    Serial.print(' ');
  }
  Serial.println();
  
  // print the calibration maximum values measured when emitters were on
  for (i = 0; i < NUM_SENSORS; i++)
  {
    Serial.print(qtra.calibratedMaximumOn[i]);
    Serial.print(' ');
  }
  Serial.println();
  Serial.println();
  delay(1000);
}


void loop()
{
  unsigned int position = qtra.readLine(sensorValues);

  unsigned char i;
  for (i = 0; i < NUM_SENSORS; i++)
  {
    Serial.print(sensorValues[i] * 10 / 1001);
    Serial.print(' ');
  }
  Serial.print("    ");
  Serial.println(position);
  
  delay(250);
}
