#!/usr/bin/env python3

import random

def roll(count, sides):
    for i in range(0,count):
        print(random.randint(1,sides))
    return 0

def menu():
    exit = False
    while exit == False:
        roll(int(input('How Many to Roll?: ')), int(input('how many sides?: ')))
        again = input('Roll Again? (Y/n): ')

        if again != 'y':
           exit = True
    
    return 0

if __name__ == '__main__':
    menu()

