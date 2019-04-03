/*
 * Main climato file
 */


#include "Arduino.h"
#include "Plotter.h"

// Plotted variables must be declared as globals 
double x;
double y;

// Also declare plotter as global
Plotter p;

void setup() {
    // Start plotter
    p.Begin();
    p.AddTimeGraph( "Time graph w/ 500 points", 500, "x label", x );
}

void loop() {
    // Update variables with arbitrary sine/cosine data
    x = 10*sin( 2.0*PI*( millis() / 5000.0 ) );
    y = 10*cos( 2.0*PI*( millis() / 5000.0 ) );

    // Plot
    p.Plot();
}

// void setup() {
//     pinMode(LED_BUILTIN, OUTPUT);
// }

// void loop() {
//     digitalWrite(LED_BUILTIN, HIGH);
//     delay(500);
//     digitalWrite(LED_BUILTIN, LOW);
//     delay(2000);
// }
