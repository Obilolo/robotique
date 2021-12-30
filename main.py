# cette fonction fait tourner le MOVE:mini de "degres"
def tourneGauche(degres: number):
    global tempsAttente
    tempsAttente = degres * MICROSEC_PAR_SEC / DEGRES_PAR_SEC
    pins.servo_write_pin(AnalogPin.P1, 45)
    pins.servo_write_pin(AnalogPin.P2, 45)
    control.wait_micros(tempsAttente)
    pins.servo_write_pin(AnalogPin.P1, 90)
    pins.servo_write_pin(AnalogPin.P2, 90)

# cette fonction fait avancer le MOVE:mini de "distance"
def avance(distance: number):
    global tempsAttente2
    tempsAttente2 = distance * MICROSEC_PAR_SEC / DISTANCE_PAR_SEC
    pins.servo_write_pin(AnalogPin.P1, 0)
    pins.servo_write_pin(AnalogPin.P2, 180)
    control.wait_micros(tempsAttente2)
    pins.servo_write_pin(AnalogPin.P1, 90)
    pins.servo_write_pin(AnalogPin.P2, 90)

def on_button_pressed_b():
    basic.pause(500)
    avance(100)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_a():
    basic.pause(500)
    tourneGauche(90)
input.on_button_pressed(Button.A, on_button_pressed_a)

tempsAttente = 0
tempsAttente2 = 0
DEGRES_PAR_SEC = 0
MICROSEC_PAR_SEC = 0
MICROSEC_PAR_SEC = 1000000
DISTANCE_PAR_SEC = 100
DEGRES_PAR_SEC = 200