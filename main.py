temp = 0
luminosite = 0
humidity = 0
random = 0

def on_button_pressed_a():
    global temp
    temp = input.temperature()
    basic.show_number(temp)
    while temp < 10:
        basic.show_string("Place the plant in a warmer environment")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global luminosite
    luminosite = input.light_level()
    basic.show_number(luminosite)
    while luminosite < 120:
        basic.show_string("Plants needs more light")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    while True:
        if humidity < 60:
            basic.show_string("Watering the plants")
        break
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_forever():
    pass
basic.forever(on_forever)

def on_every_interval():
    global random
    random = randint(0, 100)
    while True:
        if humidity < 60:
            basic.show_string("No humidity")
        break
loops.every_interval(120000, on_every_interval)
