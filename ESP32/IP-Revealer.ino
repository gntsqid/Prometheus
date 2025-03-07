#include <WiFi.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SDA_PIN 21  // Replace with your SDA pin number
#define SCL_PIN 22  // Replace with your SCL pin number

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

#define OLED_RESET    -1  // No reset pin
#define SCREEN_ADDRESS 0x3C  // Change this if needed

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// Wi-Fi credentials
const char* ssid = "LOONEYTUNES";
const char* password = "SJL#home";

void setup() {
  // Initialize Serial
  Serial.begin(115200);
  
  // Initialize I2C with SDA and SCL pins
  Wire.begin(SDA_PIN, SCL_PIN);  
  
  // Initialize OLED display
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;);
  }
  display.display();
  delay(2000);
  display.clearDisplay();
  
  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  // Display IP address on OLED
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.print("IP Address: ");
  display.println(WiFi.localIP());
  display.display();
  
  delay(5000); // Update every 5 seconds
}
