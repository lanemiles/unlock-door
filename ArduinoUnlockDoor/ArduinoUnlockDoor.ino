#define RELAY_PIN 6

void setup() {
  pinMode(RELAY_PIN, OUTPUT); // Set the relay pin as an output
  digitalWrite(RELAY_PIN, HIGH); // Start with the door locked
  Serial.begin(9600); // Start serial communication at 9600 baud
}

void loop() {
  if (Serial.available() > 0) { // Check if data is available
    String command = Serial.readStringUntil('\n'); // Read the command until a newline
    command.trim(); // Remove any extra whitespace
    if (command == "UNLOCK") {
      digitalWrite(RELAY_PIN, LOW); // Unlock the door
      Serial.println("Door is unlocked");
      delay(3000); // Keep door open for 3 seconds
      digitalWrite(RELAY_PIN, HIGH); // Lock the door
      Serial.println("Door is locked");
    } 
  }
  digitalWrite(RELAY_PIN, HIGH); // Lock the door at the end just to be safe
  Serial.println("Door is locked");
}