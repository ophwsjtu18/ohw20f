#include <Servo.h>
Servo servo1;

char input = "";         // 缓存字符串
boolean stringComplete = false;  // 是否string已经完成缓存

void setup() {
  // put your setup code here, to run once:
  servo1.attach(9);
  Serial.begin(9600);
}

void loop() {

  if(Serial.available()>0)
  {
    input = char(Serial.read());
    delay(2);
  }
  
  switch(input){
    case '1':
        servo1.write(180); 
        break;
    case '2':
        servo1.write(0); 
        break;
    case '3':
        servo1.write(90); 
        break;
  }
  
  //servo1.write(int(input)*20); 
  delay(1000);
  
}
