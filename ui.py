# Gotta start off with the design of the interface

def make_choice():
    print('''
    1. Venue
    2. New item
    3. Delete an item
    4. Items you have
    5. Items sold
    6. Total items sold at venue
    ''')

    choice = input('What would you like to do? ')
    return choice

def message(msg):
    print(msg)
