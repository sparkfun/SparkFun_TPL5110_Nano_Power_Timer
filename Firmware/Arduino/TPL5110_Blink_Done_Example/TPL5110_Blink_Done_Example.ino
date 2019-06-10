/*
  TPL5110_Blink_Demo_example.ino

  Simple Example Code for the TPL5110 Nano Power Timer Hookup Guide. This code
  simply blinks the pin 13 LED and writes pin 4 (donePin pin) high. This shift from
  LOW to HIGH of the donePin pin, signals to the Nano Power Timer to turn off the
  microcontroller.
  SparkFun Electronics
  Date: May, 2019
  Author: Elias Santistevan
*/

int led = 13; // Pin 13 LED
int donePin = 4; // Done pin - can be any pin.  

void setup(){

  pinMode(led, OUTPUT); 
  pinMode(donePin, OUTPUT); 

}

void loop(){
  // Blink. 
  digitalWrite(led, HIGH); 
  delay(1000); 
  digitalWrite(led, LOW); 
  delay(1000); 

  // We're done!
  // It's important that the donePin is written LOW and THEN HIGH. This shift
  // from low to HIGH is how the Nano Power Timer knows to turn off the
  // microcontroller. 
  digitalWrite(donePin, LOW); 
  digitalWrite(donePin, HIGH); 
  delay(10);
}
