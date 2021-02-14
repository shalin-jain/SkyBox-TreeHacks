#include "Air_Quality_Sensor.h"

//Dust Sensor Values
int measurePin = 0; //Connect dust sensor to Arduino A0 pin
int ledPower = 2;   //Connect led driver pins of dust sensor to Arduino D2

int samplingTime = 280;
int deltaTime = 40;
int sleepTime = 9680;

float voMeasured = 0;
float calcVoltage = 0;
float dustDensity = 0;

//Air Quality Sensor Values
AirQualitySensor sensor(A1);

void setup(){
  Serial.begin(9600);
  pinMode(ledPower,OUTPUT);
  //Serial.println("Dust Sensor Found");
  while (!Serial);

    // Serial.println("Waiting Air Quality sensor to init...");
    delay(20000);

    if (sensor.init()) {
        // Serial.println("Air Quality Sensor ready.");
    } else {
        // Serial.println("Air Quality Sensor ERROR!");
    }
}

void loop(){
  digitalWrite(ledPower,LOW); // power on the LED
  delayMicroseconds(samplingTime);
  voMeasured = analogRead(measurePin); // read the dust value
  delayMicroseconds(deltaTime);
  digitalWrite(ledPower,HIGH); // turn the LED off
  delayMicroseconds(sleepTime);
  // 0 - 5V mapped to 0 - 1023 integer values
  // recover voltage
  calcVoltage = voMeasured * (5.0 / 1024.0);
  dustDensity = 17 * calcVoltage - 0.1;
  
  String dustLevel = "";
  if(dustDensity <= 30) {
    dustLevel = "0";
  } else if (dustDensity <= 60) {
    dustLevel = "1";
  } else if (dustDensity <= 90) {
    dustLevel = "2";
  } else if (dustDensity <= 120) {
    dustLevel = "3";  
  } else if (dustDensity <= 250) {
    dustLevel = "4";  
  } else {
    dustLevel = "5";  
  }
  
  Serial.print(dustLevel);

  int quality = sensor.slope();

  String pollutionLevel = "";

  if (quality == AirQualitySensor::FORCE_SIGNAL) {
      //Serial.println("High pollution! Force signal active.");
  } else if (quality == AirQualitySensor::HIGH_POLLUTION) {
      pollutionLevel = "2";
  } else if (quality == AirQualitySensor::LOW_POLLUTION) {
      pollutionLevel = "1";
  } else if (quality == AirQualitySensor::FRESH_AIR) {
      pollutionLevel = "0";
  }

  String msg = dustLevel + "," + pollutionLevel;

  Serial.print(msg);

  delay(30000);
}
