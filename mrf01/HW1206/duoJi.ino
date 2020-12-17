#include <Servo.h>
long item;
long ini;
Servo servo_3;

void setup()
{
  item = 0;
  Serial.begin(9600);
  servo_3.attach(3);
  ini = servo_3.read();
}

void loop()
{
  ini = servo_3.read();
  if (Serial.available() > 0) 
  {
    item = String(Serial.readStringUntil('c')).toInt();
    servo_6.write((ini + item));
    delay(1200);
  }
}
