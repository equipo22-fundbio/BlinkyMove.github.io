// C++ code
//
#include <SoftwareSerial.h>

SoftwareSerial BlueSerial(0,1); // RX | TX

void setup()
{
  pinMode(9, OUTPUT);  // Pin del bluetooth HC-05 
  digitalWrite(9, HIGH);
  Serial.begin(9600);
  BlueSerial.begin(30000);  // HC-05 default speed
  
  pinMode(A1, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  pinMode(A2, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  pinMode(A3, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  pinMode(A4, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  if (BTSerial.available())
    Serial.write(BlueSerial.read());

  	analogRead(A1);

  	digitalWrite(LED_BUILTIN, HIGH);
 	delay(1000); // Wait for 1000 millisecond(s)
 	digitalWrite(LED_BUILTIN, LOW);
 	delay(1000); // Wait for 1000 millisecond(s)
 	Serial.println("Left");

  	analogRead(A2);

  	digitalWrite(LED_BUILTIN, HIGH);
  	delay(1000); // Wait for 1000 millisecond(s)
    digitalWrite(LED_BUILTIN, LOW);
    delay(1000); // Wait for 1000 millisecond(s)
    Serial.println("Right");

    analogRead(A3);

    digitalWrite(LED_BUILTIN, HIGH);
    delay(1000); // Wait for 1000 millisecond(s)
    digitalWrite(LED_BUILTIN, LOW);
    delay(1000); // Wait for 1000 millisecond(s)
    Serial.println("Up");

    analogRead(A4);

    digitalWrite(LED_BUILTIN, HIGH);
    delay(1000); // Wait for 1000 millisecond(s)
    digitalWrite(LED_BUILTIN, LOW);
    delay(1000); // Wait for 1000 millisecond(s)
    Serial.println("Down");
  
    if (Serial.available()){
    	BlueSerial.write(Serial.read());
	}
}

