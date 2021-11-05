
// C++ code
//
#include <SoftwareSerial.h>

SoftwareSerial BTSerial(0,1); // RX | TX
int Left = 2;
int right = 3;
int up = 4;
int down = 5;
int LED_BUILTIN_UNO;
int LED_BUILTIN_DOS;
int LED_BUILTIN_TRES;
int LED_BUILTIN_CUATRO;

//Se configuran los pines como entradas y salidas
void setup()
{
  pinMode(9, OUTPUT);  // Pin del bluetooth HC-05 
  digitalWrite(9, HIGH); 
  Serial.begin(9600);
  BTSerial.begin(30000);  // HC-05 default speed
  
  pinMode(A1, INPUT); 
  pinMode(LED_BUILTIN_UNO, OUTPUT);
  Serial.begin(9600);
  pinMode(A2, INPUT);
  pinMode(LED_BUILTIN_DOS, OUTPUT);
  Serial.begin(9600);
  pinMode(A3, INPUT);
  pinMode(LED_BUILTIN_TRES, OUTPUT);
  Serial.begin(9600);
  pinMode(A4, INPUT);
  pinMode(LED_BUILTIN_CUATRO, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
    if (BTSerial.available()){
    	Serial.write(BTSerial.read());

  	analogRead(A1);

  	digitalWrite(LED_BUILTIN, HIGH); //Si la opcion de entrada "Left" esta HIGH, la salida del pin "LED_BUILTIN_UNO" quedara en arriba
 	delay(1000); // Wait for 1000 millisecond(s)
 	digitalWrite(LED_BUILTIN, LOW); //La salida del pin estara en bajo
 	delay(1000); // Wait for 1000 millisecond(s)
 	Serial.println("Left");

  	analogRead(A2);

  	digitalWrite(LED_BUILTIN, HIGH);
  	delay(1000); // Wait for 1000 millisecond(s)
   	analogRead(A4);
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
	ial.println("Down");
  
    if (Serial.available()){
    	BlueSerial.write(Serial.read());
    }

    }
}

