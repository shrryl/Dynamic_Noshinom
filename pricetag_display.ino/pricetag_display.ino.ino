#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

// void setup() {
//   lcd.begin(8, 1);
//   lcd.print("hello");
// }

// void loop() {
//  if (Serial.available() > 0) {
//    String command = Serial.readString();
//    if (command == "clear") {
//      lcd.clear();
//    } else if (command.startsWith("cursor")) {
//      int spaceIndex = command.indexOf(' ');
//      int column = command.substring(spaceIndex + 1).toInt();
//      spaceIndex = command.indexOf(' ', spaceIndex + 1);
//      int row = command.substring(spaceIndex + 1).toInt();
//      lcd.setCursor(column, row);
//    } else if (command.startsWith("text")) {
//      int spaceIndex = command.indexOf(' ');
//      String text = command.substring(spaceIndex + 1);
//      lcd.print(text);
//    }
//  }
void setup() {
  lcd.begin(16,2);
  lcd.print("Hello world!");
}
void loop() {
  lcd.setCursor(0, 1);
  lcd.print(millis() /1000);
  // lcd.print("Discount");
  // delay(3000);

  // lcd.setCursor(2,1);
  // lcd.print("Normal");
  // delay(3000);

  // lcd.clear();
  // lcd.blink();

  // lcd.setCursor(2,1);
  // lcd.clear();

}
