# -*- coding: utf-8 -*-
"""
Created on Sun May  2 22:48:06 2021
finalproject.py
@author: felip
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 22:14:00 2021
dir_list.py
@author: felip
"""
import os

DISPLAY = 1
PRINT = 2
CREATE = 3
CHANGE = 4
DELETE = 5
QUIT = 6

def main():
    dir_list = {}
    
    choice = 0
    
    while choice != QUIT:
        choice = get_menu_choice()
        
        if choice == DISPLAY:
            display(dir_list)
        elif choice == PRINT:
            print_dir(dir_list)
        elif choice == CREATE:
            create_dir(dir_list)
        elif choice == CHANGE:
            change(dir_list)
        elif choice == DELETE:
            delete(dir_list)
    print("Goodbye and thanks for using the toolkit.")
        
def get_menu_choice():
        
        
        print()
        print('Directory Toolkit Menu')
        print('1. Display the Current Working Directory')
        print('2. Print a Directory List')
        print('3. Create a Directory')
        print('4. Change to a Directory')
        print('5. Delete a Directory')
        print('6. Quit')
        
        choice = int(input('Enter your choice: '))
        while choice < DISPLAY or  choice > QUIT:
            choice = int(input('Please enter a valid number from 1-6'))
        return choice

           
def display(dir_list):
            print(os.getcwd())
            
def print_dir(dir_list):
    for di in dir_list:
        print(di, ":", dir_list[di])
        
def create_dir(dir_list):
            os.chdir('Users\felip\Desktop\class\Spring 2021\Python cybersec\FinalProject')
            name = input('Please enter a new directory name with letters and numbers and no spaces:')
            if name not in dir_list:
                os.mkdir(name)
            else:
                print('The', name, 'directory already exists.')

def change(dir_list):
            os.chdir('Users\felip\Desktop\class\Spring 2021\Python cybersec\FinalProject')
            name = input('Please enter the directory you want to change to: ')
            if name in dir_list:
                new_dir = input('Enter the new dir_list: ')
                os.chdir('Users\felip\Desktop\class\Spring 2021\Python cybersec\FinalProject'+new_dir)
            else:
                print('That directory does not exist in this path.')

def delete(dir_list):
            os.chdir('Users\felip\Desktop\class\Spring 2021\Python cybersec\FinalProject')
            name = input('Enter the directory you want to delete: ')
            if name in dir_list:
                del dir_list[name]
                print(name, " is deleted")
            else:
                print('That directory does not exist in this path.')
                
main()