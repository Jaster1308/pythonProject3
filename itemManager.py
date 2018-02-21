# import databases and the date time for support
import sqlite3, datetime, ui

db_name = 'Stuff.db'
with sqlite3.connect(db_name) as db:
    cur = db.cursor()

# get current date for the venues and not have to type it
Current_Date = datetime.datetime.now()

def handle_choice(choice):

    if choice == '1':
    elif choice == '2':
    elif choice == '3':
    elif choice == '4':
    elif choice == '5':
    elif choice == '6':
    elif choice == 'stop':
        quit()

    else:
        ui.message("That's not a valid selection or type stop to exit.....")

# Time to make the tables. Separate venue, make/item, and sold/item dbs.

def venue_table():
    global db
    global cur
    #create the venue table with id, name, and date
    cur.execute('CREATE TABLE IF NOT EXISTS venues (ven_id INTEGER PRIMARY KEY,'
                'ven_name char(50), ven_date date)')

# lets make an venue here
def new_venue():
    global db
    global cur

    ven_name = input("Whats the venue called? ")
    ven_date = "%d/%d/%d" %(Current_Date.month, Current_Date.day, Current_Date.year)
    # add the table im using
    venue_table()
    #add query
    cur.execute('INSERT INTO venues VALUES (?, ?, ?)', (None, ven_name, ven_date ))


def items_table():
    global db
    global cur
    #create the table for the items that are in store
    cur.execute('CREATE TABLE IF NOT EXISTS itemStore (id_item INTEGER PRIMARY KEY,'
                'ven_id INTEGER REFERENCES venues(ven_id), name_item char(50), price_item INTEGER)')

# now lets make a new item
def new_item():
    global db
    global cur

    name_item = input("What item would you like to add? ")
    price_item = input("What's the price of the item? ")
    ven_id = input("What's the venue ID? ")
    #add table to use this in
    items_table()
    #make sure that foreign keys are set using pragma
    cur.execute('PRAGMA foreign_keys = ON')
    cur.execute('INSERT INTO itemStore VALUES (?, ?, ?, ?)', (None, ven_id, name_item, price_item))

#sold is a little different since its taking away from the items table