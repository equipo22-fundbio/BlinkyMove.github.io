#include <QTRSensors.h> //Se van a utilizar sensores QTR - 1RC
#include <Adafruit_NeoPixel.h>
#define NUM_SENSORES             4  // número de sensores
#define NUM_SAMPLES_POR_SENSOR  
#define EMITTER_PIN 
#define PIN A3           
int iniSensorValL, sensorValL;
int iniSensorValR, sensorValR;
int iniSensorValU, sensorValU;
int iniSensorValD, sensorValD;

int blackNum = 20;
int pupilNum = 15;
uint32_t color;
int brightness = 50;
byte eyeColor;
int LR =7;
int UD =6;
boolean lid = false;
int contador = 0;

//Animacion del parpadeo
int eyelid = 0;
QTRSensorsAnalog qtra((unsigned char[]) {0, 1}, NUM_SENSORES, NUM_SAMPLES_POR_SENSOR, EMITTER_PIN);
unsigned int sensorValues[NUM_SENSORES];

void blink(int eyelid, int LR) {
 if (eyelid != 8){
   //Black eye
   for(uint16_t i=0; i<blackNum; i++) {
     led.setPixelColor(blackLED[LR][i], color);
   }
   //pupila
   for(uint16_t i=0; i<pupilaNum; i++) {
     led.setPixelColor(pupilaLED[LR][i], led.Color(0, 0, 66));
   }
   //eyelid
   for(int i=0; i < eyelidNum[eyelid]; i++) {
     led.setPixelColor(eyelidLED[i], 0);
   }
 } else if (eyelid == 8){
   led.clear();
 }
 led.show();
}
void setup() {
 Serial.begin(115200);
 led.begin();
 led.setBrightness(brightness); // Brillo inicial 50
 led.show(); // Se inicializa el pixel con 'off'
 color = led.Color(0, 177, 55); //Color de Pupila
 delay(100);
 qtra.read(sensorValues);
 iniSensorValL = sensorValues[0];
 iniSensorValR = sensorValues[1];
 iniSensorValU = sensorValues[2];
 iniSensorValD = sensorValues[3];
 blink(eyelid, LR);
 blink(eyelid, UD);
}
void loop() {
   //QTR - 1RC valores del sensor
 	qtra.read(sensorValues);
 	sensorValL = sensorValues[0];
 	sensorValR = sensorValues[1]; 
 	sensorValU = sensorValues[2];
 	sensorValD = sensorValues[3];

 	double radioL = (double)sensorValL / iniSensorValL;
	double radioR = (double)sensorValR / iniSensorValR;
 	double radioU = (double)sensorValU / iniSensorValU;
 	double radioD = (double)sensorValD / iniSensorValD;

 	Serial.print(radioL);
 	Serial.print("  ");
 	Serial.println(radioR);
 	Serial.println(radioU);
 	Serial.print("  ");
 	Serial.println(radioD);
	
	//Se agregar las coordenadas necesarias para captar la direccion de ojo
 	if(radioL > 0.998 && radioR < 0.998){ //right
   	for(int i = LR; i < 12; i++){
     	   blink(0, i);
           LR = i;
   	  }
 	}else if(radioL < 0.998 && radioR > 0.998){ //left
   	for(int i=LR; i>2; i--){
          blink(0, i);
     	  LR = i;
   	}
  	if(radioD > 0.998 && radioU < 0.998){ //up
   	for(int i = UD; i < 12; i++){
     	  blink(0, i);
          UD = i;
   	  }
 	}else if(rasioU < 0.998 && rasioD > 0.998){ //Down
   	for(int i=UB; i>2; i--){
    	  blink(0, i);
     	  UD = i;
   	  }

	//Para definir un parpadeo, se realiza la siguiente condicion
 	}else if(lid == false && rasioL < 0.94 && rasioR < 0.94){ //Parpadeo - cerrar
   	for(int i = 1; i < 9; i++){
     	  blink(i, LR);
     	  lid = true;
   	  }
 	}else if(lid == true && rasioL > 0.94 && rasioR > 0.94){ //Parpadeo - abrir
  	for(int i = 8; i > 0; i--){
    	  blink(i, LR);
     	  lid = false;
  	 }
 	}else if(lid == false && rasioL > 0.94 && rasioR > 0.94) {   //normal


   	//contador++;
   	//eyelid = 0;
   	if(LR <= 7){
     	for(int i=LR; i<=7; i++){
       	  blink(0, i);
          LR = i;
     	 }
   	}else {
     	for(int i=LR; i>=7; i--){
       	  blink(0, i);
          LR = i;
     	 }
   	if(UD <= 6){
     	for(int i=UD; i<=6; i++){
       	  blink(0, i);
          UD = i;
         }
        }else {
     	for(int i=UD; i>=6; i--){
       	  blink(0, i);
       	  UD = i;
     	}
     }
   }
 }
 //refresh - valores iniciales
 if (contador > 10){
   iniSensorValL = sensorValL;
   iniSensorValR = sensorValR;
   iniSensorValU = sensorValU;
   iniSensorValD = sensorValD;
   contador = 0;
 }
}
