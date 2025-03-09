void setup() {
  pinMode(LED_BUILTIN, OUTPUT); // Set built-in LED as an output
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH); // Turn LED ON
  delay(500);                      // Wait 500ms
  digitalWrite(LED_BUILTIN, LOW);  // Turn LED OFF
  delay(500);                      // Wait 500ms
}
