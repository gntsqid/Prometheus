#define LED_BUILTIN 2  // Onboard LED pin number for ESP32 is usually 2. Verify from your board specifications if different.

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);  // Initialize the onboard LED as an output
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);  // Turn on the LED
  delay(1000);                      // Wait for one second
  digitalWrite(LED_BUILTIN, LOW);   // Turn off the LED
  delay(1000);                      // Wait for one second
}
