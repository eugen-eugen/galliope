# Beim Start den Kompass kalibrieren
input.calibrate_compass()
# Hauptprogramm in Dauerschleife

def on_forever():
    # Kompasswert in Grad auslesen (0-359)
    heading = 360 - input.compass_heading()
    # Display löschen
    basic.clear_screen()
    # Kompassrichtung als Strich anzeigen - in entgegengesetzte Richtung
    if heading >= 338 or heading < 23:
        # Kompass zeigt nach Norden -> Strich zeigt nach Süden
        led.plot(2, 2)
        led.plot(2, 3)
        led.plot(2, 4)
    elif heading >= 23 and heading < 68:
        # Kompass zeigt nach Nordost -> Strich zeigt nach Südwest
        # Mittleres LED und zwei LEDs zur unteren linken Ecke
        led.plot(2, 2)
        led.plot(1, 3)
        led.plot(0, 4)
    elif heading >= 68 and heading < 113:
        # Kompass zeigt nach Osten -> Strich zeigt nach Westen
        led.plot(0, 2)
        led.plot(1, 2)
        led.plot(2, 2)
    elif heading >= 113 and heading < 158:
        # Kompass zeigt nach Südost -> Strich zeigt nach Nordwest
        # Mittleres LED und zwei LEDs zur oberen linken Ecke
        led.plot(2, 2)
        led.plot(1, 1)
        led.plot(0, 0)
    elif heading >= 158 and heading < 203:
        # Kompass zeigt nach Süden -> Strich zeigt nach Norden
        led.plot(2, 0)
        led.plot(2, 1)
        led.plot(2, 2)
    elif heading >= 203 and heading < 248:
        # Kompass zeigt nach Südwest -> Strich zeigt nach Nordost
        # Mittleres LED und zwei LEDs zur oberen rechten Ecke
        led.plot(2, 2)
        led.plot(3, 1)
        led.plot(4, 0)
    elif heading >= 248 and heading < 293:
        # Kompass zeigt nach Westen -> Strich zeigt nach Osten
        led.plot(2, 2)
        led.plot(3, 2)
        led.plot(4, 2)
    else:
        # heading >= 293 und heading < 338
        # Kompass zeigt nach Nordwest -> Strich zeigt nach Südost
        # Mittleres LED und zwei LEDs zur unteren rechten Ecke
        led.plot(2, 2)
        led.plot(3, 3)
        led.plot(4, 4)
    # Pause, um CPU-Last zu reduzieren
    basic.pause(100)
basic.forever(on_forever)

# Wenn Knopf A gedrückt wird, Gradwert anzeigen
# Kurze Pause, damit der Wert lesbar ist

def on_button_pressed_a():
    basic.show_number(input.compass_heading())
    basic.pause(1000)
input.on_button_pressed(Button.A, on_button_pressed_a)
