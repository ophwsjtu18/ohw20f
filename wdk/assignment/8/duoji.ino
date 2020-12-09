#include <Servo.h>

long item;
Servo servo_6;
long ini;

void setup()
{
  item = 0;
  Serial.begin(9600);
  servo_6.attach(6);
  ini = servo_6.read();
}

void loop()
{
  ini = servo_6.read();
  if (Serial.available() > 0) {
    item = String(Serial.readStringUntil('a')).toInt();
    servo_6.write((ini + item));
    delay(1000);
  }
}
