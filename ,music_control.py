#!/bin/python3
from pitftgpio import PiTFT_GPIO
from time import sleep
import os
import keyboard
from screens.ncmpcpp import ncmpcpp
from button_grabber import Button_input

screen_detector = 0
pitft = PiTFT_GPIO()
command_sets = {
    'vimwiki_Todo' : [
        lambda : None,                   # 0
        lambda : keyboard.send('j'),     # 1
        lambda : keyboard.send('ctrl+space'), # 2
        lambda : None,                   # 3
        lambda : None,                   # 4
        lambda : None,                   # 5
        lambda : None,                   # 6
        lambda : None,                   # 7
        lambda : keyboard.send("k"),     # 8
        lambda : None,                   # 9
        lambda : None,                   # A
        lambda : None,                   # B
        lambda : None,                   # C
        lambda : None,                   # D
        lambda : None,                   # E
        lambda : exit_todoList(),        # F
    ],
    'ncmpcpp' : [
        lambda : None,                   # 0
        lambda : keyboard.send('tab'),    # 1
        lambda : keyboard.send("n"),     # 2
        lambda : keyboard.send('up'),    # 3
        lambda : keyboard.send("p"),     # 4
        lambda : keyboard.send('enter'),    # 5
        lambda : None,                   # 6
        lambda : None,                   # 7
        lambda : keyboard.send("b"),     # 8
        lambda : keyboard.send("space"), # 9
        lambda : keyboard.send('backspace'),    # A
        lambda : None,                   # B
        lambda : keyboard.send("down"),  # C
        lambda : None,                   # D
        lambda : clearplaylist(),        # E
        lambda : exit_ncmpcpp(),         # F
    ],
    'mainMenu' : [
        lambda : None,                   # 0
        lambda : start_ncmpcpp(),        # 1
        lambda : start_todoList(),       # 2
        lambda : None,                   # 3
        lambda : None,                   # 4
        lambda : None,                   # 5
        lambda : update_this_script(),   # 6
        lambda : None,                   # 7
        lambda : None,                   # 8
        lambda : None,                   # 9
        lambda : None,                   # A
        lambda : None,                   # B
        lambda : None,                   # C
        lambda : None,                   # D
        lambda : None,                   # E
        lambda : restart_this_script(),  # F
    ]
}

def start_todoList():
    keyboard.write('nvim')
    keyboard.send('enter')
    sleep(.15)
    keyboard.write("\\ww")
    global current_state
    current_state = 'vimwiki_Todo'

def exit_todoList():
    keyboard.write("\\x")
    keyboard.send('enter')
    sleep(.1)
    mainMenu()

def start_ncmpcpp():
    keyboard.write('ncmpcpp')
    keyboard.send('enter')
    global current_state
    current_state = 'ncmpcpp'

def exit_ncmpcpp():
    keyboard.send('q')
    sleep(.1)
    mainMenu()

def mainMenu():
    global current_state
    current_state = 'mainMenu'
    keyboard.write('clear')
    keyboard.send('enter')
    sleep(3)
    print("""
    Main Menu:
        1. ncmpcpp
        2. TodoList
        3. ScreenSaver
        4. Update TodoList
        5. Update Music
        6. Update This Script
        7 Full Update
        15. Shut it Down (I haven't implemented this yet)
    """)

def clearplaylist():
    keyboard.send("c")
    sleep(.1)
    keyboard.send("y")

controller = Button_input(command_sets['mainMenu'])
