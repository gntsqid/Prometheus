// This file type is specifically for Arduino IDE for my ESP32 board
// It scans for WiFi signals every 5 seconds and outputs them to my i2c screen
#include <WiFi.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SDA_PIN 21  // Replace with your SDA pin number
#define SCL_PIN 22  // Replace with your SCL pin number

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET    -1
#define SCREEN_ADDRESS 0x3C // Change this if needed

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void setup() {
  Wire.begin(SDA_PIN, SCL_PIN);  // Initialize I2C with SDA and SCL pins
  Serial.begin(115200);

  if (!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println("SSD1306 initialization failed");
    while (1);
  }
  
  display.display();
  delay(2000);
  
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);
  
  Serial.println("Scanning Wifi networks");
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println("Scanning Wifi...");
  display.display();
}

void loop() {
  display.clearDisplay();
  display.setCursor(0, 0);
  
  int n = WiFi.scanNetworks();
  if (n == 0) {
    display.println("No networks found");
  } else {
    display.print(n);
    display.println(" networks found");
    for (int i = 0; i < n; ++i) {
      display.setCursor(0, (i + 1) * 10);
      display.print(WiFi.SSID(i));
      display.print(" (");
      display.print(WiFi.RSSI(i));
      display.print(")");
      delay(10);
    }
  }
  display.display();
  delay(5000);  // Scan every 5 seconds
}
