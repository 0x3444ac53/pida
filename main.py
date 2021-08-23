#!/bin/python3
from pitftgpio import PiTFT_GPIO
from time import sleep
import os
import keyboard
from screens.ncmpcpp import ncmpcpp
import git
from button_grabber import Button_input

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

class mainMenu:
    def __init__(self):
        self.command_map = [
            lambda : None,                   # 0
            lambda : start_ncmpcpp(),        # 1
            lambda : start_todoList(),       # 2
            lambda : None,                   # 3
            lambda : None,                   # 4
            lambda : print("6734673467364"),                   # 5
            lambda : self.update_this_script(),   # 6
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
        for i in range(100):
            print("HELLO")
        print("""Main Menu:
            1. ncmpcpp
            2. TodoList
            3. ScreenSaver
            4. Update TodoList
            5. Update Music
            6. Update This Program
            7 Full Update
            5. Shut it Down (I haven't implemented this yet)
            """)

    def update_this_script(self):
        print("Updating repo")
        repo = git.Repo("/home/pi/bin/pida")
        repo.repo.remotes.origin.pull()
        print("Done! Rebooting now...")
        os.system('shutdown -r now')


def clearplaylist():
    keyboard.send("c")
    sleep(.1)
    keyboard.send("y")

if __name__ == '__main__':
    controller = Button_input([lambda *_: None])
    menu = mainMenu()
    controller.change_screen(menu.command_map)
