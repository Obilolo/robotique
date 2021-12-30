// cette fonction fait tourner le MOVE:mini de "degres"
function tourneGauche (degres: number) {
    tempsAttente = degres * MICROSEC_PAR_SEC / DEGRES_PAR_SEC
    pins.servoWritePin(AnalogPin.P1, 45)
    pins.servoWritePin(AnalogPin.P2, 45)
    control.waitMicros(tempsAttente)
    pins.servoWritePin(AnalogPin.P1, 90)
    pins.servoWritePin(AnalogPin.P2, 90)
}
input.onButtonPressed(Button.A, function () {
    basic.pause(500)
    tourneGauche(90)
})
input.onButtonPressed(Button.B, function () {
    basic.pause(500)
    avance(100)
})
// cette fonction fait avancer le MOVE:mini de "distance"
function avance (distance: number) {
    tempsAttente2 = distance * MICROSEC_PAR_SEC / DISTANCE_PAR_SEC
    pins.servoWritePin(AnalogPin.P1, 0)
    pins.servoWritePin(AnalogPin.P2, 180)
    control.waitMicros(tempsAttente2)
    pins.servoWritePin(AnalogPin.P1, 90)
    pins.servoWritePin(AnalogPin.P2, 90)
}
let tempsAttente2 = 0
let tempsAttente = 0
let DEGRES_PAR_SEC = 0
let DISTANCE_PAR_SEC = 0
let MICROSEC_PAR_SEC = 0
MICROSEC_PAR_SEC = 1000000
DISTANCE_PAR_SEC = 100
DEGRES_PAR_SEC = 200
