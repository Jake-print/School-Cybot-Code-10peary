input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . # . # .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        `)
    Kitronik_Robotics_Board.allOff()
})
input.onPinPressed(TouchPin.P2, function () {
    Kitronik_Robotics_Board.motorOn(Kitronik_Robotics_Board.Motors.Motor1, Kitronik_Robotics_Board.MotorDirection.Forward, 45)
    Kitronik_Robotics_Board.motorOn(Kitronik_Robotics_Board.Motors.Motor2, Kitronik_Robotics_Board.MotorDirection.Reverse, 45)
    basic.showLeds(`
        . # # # .
        . # . # .
        . # # # .
        . # # . .
        . # . # .
        `)
    basic.pause(200)
    Kitronik_Robotics_Board.allOff()
    basic.clearScreen()
})
input.onPinPressed(TouchPin.P1, function () {
    Kitronik_Robotics_Board.motorOn(Kitronik_Robotics_Board.Motors.Motor1, Kitronik_Robotics_Board.MotorDirection.Reverse, 45)
    Kitronik_Robotics_Board.motorOn(Kitronik_Robotics_Board.Motors.Motor2, Kitronik_Robotics_Board.MotorDirection.Forward, 45)
    basic.showLeds(`
        . # . . .
        . # . . .
        . # . . .
        . # . . .
        . # # # .
        `)
    basic.pause(200)
    Kitronik_Robotics_Board.allOff()
    basic.clearScreen()
})
basic.forever(function () {
    if (!(input.pinIsPressed(TouchPin.P1) && input.pinIsPressed(TouchPin.P2))) {
        Kitronik_Robotics_Board.motorOn(Kitronik_Robotics_Board.Motors.Motor1, Kitronik_Robotics_Board.MotorDirection.Forward, 50)
        Kitronik_Robotics_Board.motorOn(Kitronik_Robotics_Board.Motors.Motor2, Kitronik_Robotics_Board.MotorDirection.Forward, 50)
        basic.showLeds(`
            . # # # .
            . # . . .
            . # # # .
            . # . . .
            . # . . .
            `)
        basic.pause(200)
        Kitronik_Robotics_Board.allOff()
    }
})
