import random
import time

class Slime:
    def __init__(self, footprint, marker):
        self.__position = 0
        self.__footprint = footprint
        self.__marker = marker
        
    def run(self):
        move = random.randint(-1, 3)
        self.__position = max(0, self.__position + move)
    
    # 足跡の表示
    def display(self):
        output = self.__footprint * self.__position + self.__marker
        for char in output:
            print(char, end='', flush=True)
            time.sleep(0.1)
        print()

    @property
    def marker(self):
        return self.__marker
    @property
    def position(self):
        return self.__position
    
        
        

