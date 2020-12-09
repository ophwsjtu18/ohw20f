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
    case '0':
        servo1.write(0); 
        break;
    case '1':
        servo1.write(20); 
        break;
    case '2':
        servo1.write(40); 
        break;
    case '3':
        servo1.write(60); 
        break;
    case '4':
        servo1.write(80); 
        break;
    case '5':
        servo1.write(100); 
        break;
    case '6':
        servo1.write(120); 
        break;
    case '7':
        servo1.write(140); 
        break;
    case '8':
        servo1.write(160); 
        break;
    case '9':
        servo1.write(180); 
        break;
  }
  
  //servo1.write(int(input)*20); 
  delay(1000);
  
}
