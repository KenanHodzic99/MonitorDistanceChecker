#define echoPin 50 
#define trigPin 52 

long trajanje; 
int daljina; 

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(300);
}
void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  trajanje = pulseIn(echoPin, HIGH);
  daljina = (trajanje - 10) * 0.034 / 2;
  Serial.println(daljina);
  
}
