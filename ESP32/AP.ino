#include <WiFi.h>

// Replace these with your desired credentials.
const char *ssid = "NETSEC";
const char *password = ""; // Choose a password for your network

void setup() {
  Serial.begin(115200);

  // Setting the ESP32 as an Access Point
  WiFi.softAP(ssid, password);

  Serial.println("Access Point Started");
  Serial.print("IP Address: ");
  Serial.println(WiFi.softAPIP()); // The IP address of the ESP32 will be printed to the serial monitor
}

void loop() {
  // You don't need to put anything in the loop for an AP
}
