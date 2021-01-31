def on_pin_pressed_p2():
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR1,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        50)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR2,
        Kitronik_Robotics_Board.MotorDirection.REVERSE,
        50)
    basic.show_leds("""
        . # # # .
        . # . # .
        . # # # .
        . # # . .
        . # . # .
        """)
    basic.pause(200)
    Kitronik_Robotics_Board.all_off()
    basic.clear_screen()
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_pin_pressed_p1():
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR1,
        Kitronik_Robotics_Board.MotorDirection.REVERSE,
        50)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR2,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        50)
    basic.show_leds("""
        . # . . .
        . # . . .
        . # . . .
        . # . . .
        . # # # .
        """)
    basic.pause(200)
    Kitronik_Robotics_Board.all_off()
    basic.clear_screen()
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_forever():
    if not (input.pin_is_pressed(TouchPin.P1) or input.pin_is_pressed(TouchPin.P2)):
        Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR1,
            Kitronik_Robotics_Board.MotorDirection.REVERSE,
            50)
        Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR2,
            Kitronik_Robotics_Board.MotorDirection.FORWARD,
            50)
        basic.show_leds("""
            . # # # .
            . # . . .
            . # # # .
            . # . . .
            . # . . .
            """)
        basic.pause(200)
        Kitronik_Robotics_Board.all_off()
        basic.clear_screen()
basic.forever(on_forever)
