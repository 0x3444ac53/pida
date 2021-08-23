import keyboard
from time import sleep

class ncmpcpp():
    def __init__(self):
        self.command_map = [
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
        lambda : self.exit(),         # F
        ]
        self.start()

    def start(self):
        keyboard.write("ncmpcpp")
        sleep(.1)
        return self.command_map

    def exit(self):
        keyboard.send('q')
        sleep(.1)
