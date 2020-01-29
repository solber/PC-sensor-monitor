import globalVars
import inputManager
from time import sleep

draw = None

# ProgressBar Values
MARGIN_X = 13
MARGIN_Y = 15

selection = 0
first_group = 192
second_group = 168
third_group = 0
fourth_group = 10

render = True

def render_window():
    global first_group
    global second_group
    global third_group
    global fourth_group
    global selection
    global draw
    global render

    while render is True:
        with globalVars.canvas(globalVars.device) as draw:
            globalVars.libAdvDisplay.draw_centered_text('Enter IP :', globalVars.top, 255, draw)
            draw.rectangle((MARGIN_X, MARGIN_Y, globalVars.width - MARGIN_X, globalVars.height - MARGIN_Y), outline=255, fill=0)

            if selection == 0:
                xa = 27.5
                xb = 20
                xc = 35
                points = ((xa, globalVars.height - 43), (xb, globalVars.height - 40), (xc, globalVars.height - 40))
                draw.polygon((points), fill=200)
                points = ((xa, globalVars.height - 20), (xb, globalVars.height - 23), (xc, globalVars.height - 23))
                draw.polygon((points), fill=200)
            if selection == 1:
                xa = 57.5
                xb = 50
                xc = 65
                points = ((xa, globalVars.height - 43), (xb, globalVars.height - 40), (xc, globalVars.height - 40))
                draw.polygon((points), fill=200)
                points = ((xa, globalVars.height - 20), (xb, globalVars.height - 23), (xc, globalVars.height - 23))
                draw.polygon((points), fill=200)
            if selection == 2:
                xa = 77.5
                xb = 70
                xc = 85
                points = ((xa, globalVars.height - 43), (xb, globalVars.height - 40), (xc, globalVars.height - 40))
                draw.polygon((points), fill=200)
                points = ((xa, globalVars.height - 20), (xb, globalVars.height - 23), (xc, globalVars.height - 23))
                draw.polygon((points), fill=200)
            if selection == 3:
                xa = 87.5
                xb = 80
                xc = 95
                points = ((xa, globalVars.height - 43), (xb, globalVars.height - 40), (xc, globalVars.height - 40))
                draw.polygon((points), fill=200)
                points = ((xa, globalVars.height - 20), (xb, globalVars.height - 23), (xc, globalVars.height - 23))
                draw.polygon((points), fill=200)

            globalVars.libAdvDisplay.draw_centered_text(str(first_group) + '.' + str(second_group) + '.' + str(third_group) + '.' + str(fourth_group), globalVars.height - 37, 255, draw)

            if inputManager.key_right_pressed():
                if selection + 1 == 4:
                    selection = 0
                else:
                    selection = selection + 1
                sleep(0.2)

            if inputManager.key_left_pressed():
                if selection - 1 == -1:
                    selection = 3
                else:
                    selection = selection - 1
                sleep(0.2)

            if (selection == 0):
                if inputManager.key_up_pressed():
                    if (int(first_group) + 1 == 256):
                        first_group = 0
                    else:
                        first_group = int(first_group) + 1
                    sleep(0.2)

                if inputManager.key_down_pressed():
                    if (int(first_group) - 1 == -1):
                        first_group = 255
                    else:
                        first_group = int(first_group) - 1
                    sleep(0.2)
            if (selection == 1):
                if inputManager.key_up_pressed():
                    if (int(second_group) + 1 == 256):
                        second_group = 0
                    else:
                        second_group = int(second_group) + 1
                    sleep(0.2)

                if inputManager.key_down_pressed():
                    if (int(second_group) - 1 == -1):
                        second_group = 255
                    else:
                        second_group = int(second_group) - 1
                    sleep(0.2)
            if (selection == 2):
                if inputManager.key_up_pressed():
                    if (int(third_group) + 1 == 256):
                        third_group = 0
                    else:
                        third_group = int(third_group) + 1
                    sleep(0.2)

                if inputManager.key_down_pressed():
                    if (int(third_group) - 1 == -1):
                        third_group = 255
                    else:
                        third_group = int(third_group) - 1
                    sleep(0.2)
            if (selection == 3):
                if inputManager.key_up_pressed():
                    if (int(fourth_group) + 1 == 256):
                        fourth_group = 0
                    else:
                        fourth_group = int(fourth_group) + 1
                    sleep(0.2)

                if inputManager.key_down_pressed():
                    if (int(fourth_group) - 1 == -1):
                        fourth_group = 255
                    else:
                        fourth_group = int(fourth_group) - 1
                    sleep(0.2)

            if inputManager.key_press_pressed():
                print(str(first_group) + '.' + str(second_group) + '.' + str(third_group) + '.' + str(fourth_group))
                from cpuBars import render_bars
                render_bars(str(first_group) + '.' + str(second_group) + '.' + str(third_group) + '.' + str(fourth_group))
                render = False

render_window()