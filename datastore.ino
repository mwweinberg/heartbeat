// sets the input pin 
int potPin = 0;

//variable for time between events
volatile unsigned long elapsedTimeInMicroseconds = 0;
static unsigned long previousTimeInMicroseconds = 0;

//variables to store the time intervals
// value to determine the size of the readings array.
const int numReadings = 6;
int readingArray[numReadings];  // holds the readings
int readIndex = 0;              // the index of the current reading
int total = 0;                  // the running total
int average = 0;                // the average

int delayTime = 500;



 
void setup() 
{
  Serial.begin(9600);
}
 
void loop() 
{
  int reading  = analogRead(potPin);
  Serial.println("reading");
  Serial.println(reading);
  
  // if the reading is in a range do something
  if (reading > 400 && reading < 500)
  {
    // print a 1
    Serial.println(1);

    //figure out how long it has been since the last one
    unsigned long time = micros();
    elapsedTimeInMicroseconds = time - previousTimeInMicroseconds;
    previousTimeInMicroseconds = time;
    
    //add this amount of time to the array if it is probably
    //a live reading
    //lower bound is essentially if it is pinging one after the other
    //upper bound is about two seconds
    if (elapsedTimeInMicroseconds > ((delayTime * 1000) + 100000) && elapsedTimeInMicroseconds < 2000000)
    {
      // this value is the running total. First subtract the value you are
      // about to remove
      total = total - readingArray[readIndex];
      //replace the value with a new reading
      readingArray[readIndex] =  (elapsedTimeInMicroseconds / 1000);
      //add the new reading with what is left of the total
      total = total + readingArray[readIndex];
      // move to the next position in the array
      readIndex = readIndex + 1;
      
      //if it turns out you are at the end of the array
      if (readIndex >= numReadings) {
        // . . . start over
        readIndex = 0;
      }
          
    }
  }

  // if the reading is not in the interesting range, just carry on
  
  else
  {
    // print a 0
    Serial.println(0);
  }

  //calculate the average of the readingArray
  //regardless of if there was a useful reading this time around
  average = total / numReadings;

  Serial.println("average");
  Serial.println(average);
  Serial.println();

  // delay half a second
  delay(delayTime);
}
