from multiprocessing import Process
from pitftgpio import PiTFT_GPIO
from time import sleep

class Button_input():
    def __init__(self, button_map):
        self.button_map = button_map
        self.proc = Process(target=self.grabber_wrapper,
                            args=(button_map, ))
        self.pitft = PiTFT_GPIO()
        self.proc.start()

    def change_screen(self, new_button_map):
        self.proc.kill()
        self.proc = Process(self.grabber_wrapper, args=(new_button_map))
        self.prc.start()

    def grabber_wrapper(self, command_map):
        while True:
            self.button_grabber(command_map, vals=[False, False, False, False])

    def button_grabber(self, command_map, vals=[False, False, False, False]):
            sleep(.01)
            keylist = [
                       self.pitft.Button3,
                       self.pitft.Button1,
                       self.pitft.Button2,
                       self.pitft.Button4
                       ]
            if sum(keylist) == 0:
                command_map[int("".join(
                    map(lambda x: str(int(x)), vals)),2)]()
                return keylist
            else:
                return [x[0] or x[1] for x in zip(keylist,
                                                  self.button_grabber(command_map, vals=keylist))]


