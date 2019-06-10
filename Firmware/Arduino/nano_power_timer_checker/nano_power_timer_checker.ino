/*
  Example Code for the TPL5110 Nano Power Switch Hookup Guide. This code
  checks to see the exact time that is set by the switched resistor. This time
  varies by the EXACT resistance of the resistor which has a 1% tolerance. In
  addition, the datasheet clarifies that each resistance has its own margin of
  error when producing the given time at a given resistance. What does this
  mean? If you are in need of HIGH precision timing, this may not be the choice
  for you. If you're looking to decrease power consumption to increase battery
  life in remote applications, applications that don't require high sampling
  rates (less than 100ms), or some Internet of Things application, then you're in the right
  place. If you're using a 3.3V microcontroller then use a 3.3V power source,
  if you're using a 5V microcontroller then use a 5V souce. Take care to not
  BURN OUT your digital I/O. 
  SparkFun Electronics
  Date: May, 2019
  Author: Elias Santistevan
*/

/*  Hardware Setup on Redboard (Arduino): 
   - VDD_OUT -> 3 
   - GND -> GND 
   - VDD -> 3.3V 
*/

// REMEMBER - You must cycle power set new timer!
// ALSO - Press onboard button to begin cycle for long timers!
unsigned long endTimer = 0; 
unsigned long beginTimer = 0; 
float timerLength = 0; 

bool start = false; 
bool interrupted = false; 
// VDD-OUT goes is on pinCheck
int pinCheck = 3; 

void setup(){

  Serial.begin(115200); 
  Serial.println("Nano Power Switch - Timer Check!"); 
  Serial.println("Press the onboard button to begin the check.");
  pinMode(INPUT, pinCheck);
  // A interrupt may be overkill but it ensures we won't miss anything. 
  attachInterrupt(digitalPinToInterrupt(pinCheck), checkTimer, FALLING);

}

void loop(){

  // Check that timer is on! 
  if( (digitalRead(pinCheck) == HIGH) && (start == false)){ 
    Serial.print("Started: ");
    beginTimer = millis(); 
    Serial.println(beginTimer); 
    start = true; // Power is high, first flag is set. 
  }

  // If done signal is not sent back to Nano Power Switch, the Nano Power
  // Switch turns off power at the end of the timer anyway. After 50 ms the
  // Nano Power Switch will then turn the power back on. We're looking for that
  // small window when the power is turned off to calculate the exact time. 
  // Code will enter this block when timer has started (Power from VDD_out is
  // ON) and when we've seen it go low (Power from VDD_OUT is off).
  if((interrupted == true) && (start == true)){
    Serial.print("Ended: "); 
    Serial.println(endTimer);
    timerLength = endTimer - beginTimer; // Total time
    timerLength = timerLength + 50; // 50 ms off before back onto interval 
    Serial.print("Timer Length: "); 
    Serial.print(timerLength / 1000); // Convert to seconds... 
    Serial.println("-------");
    Serial.println();
    interrupted = false; 
    start = false; 
  }

}

// When power is low, we get our endTimer value, and set the second flag. 
void checkTimer(){
  endTimer = millis(); 
  interrupted = true; 
}
