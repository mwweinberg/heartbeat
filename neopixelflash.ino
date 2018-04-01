//heartbeat sensor libraries
#define USE_ARDUINO_INTERRUPTS true
#include <PulseSensorPlayground.h>

//for the serial plotter
const int OUTPUT_TYPE = SERIAL_PLOTTER;

//sensor variables
const int PIN_INPUT = A0;
const int THRESHOLD = 650;   // Adjust this number to avoid noise when idle
//just for testing - can be deleted
const int PIN_BLINK = 13;    // Pin 13 is the on-board LED
const int PIN_FADE = 5;

//led counter

int LIGHT = -1;
int COUNTER = 0;

//initialize the sensor
PulseSensorPlayground pulseSensor;

//neopixel setup
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIN 6
Adafruit_NeoPixel strip = Adafruit_NeoPixel(10, PIN, NEO_RGBW + NEO_KHZ800);

void setup() {
  //to print the plotter
  Serial.begin(115200);

  // configure the pulse sensor manager
  pulseSensor.analogInput(PIN_INPUT);
  pulseSensor.blinkOnPulse(PIN_BLINK);
  pulseSensor.fadeOnPulse(PIN_FADE);
  
  pulseSensor.setSerial(Serial);
  pulseSensor.setOutputType(OUTPUT_TYPE);
  pulseSensor.setThreshold(THRESHOLD);

  // Now that everything is ready, start reading the PulseSensor signal.
  if (!pulseSensor.begin()) {
    /*
       PulseSensor initialization failed,
       likely because our particular Arduino platform interrupts
       aren't supported yet.

       If your Sketch hangs here, try ProcessEverySample.ino,
       which doesn't use interrupts.
    */
    for(;;) {
      // Flash the led to show things didn't work.
      digitalWrite(PIN_BLINK, LOW);
      delay(50);
      digitalWrite(PIN_BLINK, HIGH);
      delay(50);
    }
  }

  //neopixel setup
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
}

void loop() {

  //reset lights to off
  strip.show();

  //sensor section
   /*
     Wait a bit.
     We don't output every sample, because our baud rate
     won't support that much I/O.
  */
  delay(20);

  // write the latest sample to Serial.
 pulseSensor.outputSample();

  /*
     If a beat has happened since we last checked,
     write the per-beat information to Serial.
   */
  if (pulseSensor.sawStartOfBeat()) {
   pulseSensor.outputBeat();
     //neopixel section     
    flash();
  }


  /*Counts every time there is a loop. This is reset 
   * whenever the pulse is detected
   * if there is long enough between deteted pulses (30)
   * everything resets to zero
  */
  COUNTER = COUNTER + 1;
  if (COUNTER > 30) {
    LIGHT = -1;
  }
}


void flash() {
  //resets the counter
  COUNTER = 0;
    //adds one to the light
    LIGHT = (LIGHT + 1);
    //for each light that should be on, start high
    //and fade to low
    for (int x=255; x > 0; x--) {
      for (int y = 0; y < (LIGHT + 1); y++){
       
          strip.setPixelColor(y, x);
          strip.show();   
      }
    
     
  }


}

