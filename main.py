import random
import datetime
import os

#                                      -------------    Guidelines   --------------
# Use camelCase for variables and PascalCase for functions
# Universal variables assign on top, otherwise assign in function itself
# Use python 3.11

#Environment Settings
initialReservationsTxt = 'reservation_StudentID.txt'
menuItemsTxt = 'menuItems_StudentID.txt'

#Variables
customerReservations = []
menuItems = []

def NavigateMenu():
    #TODO: format with format()? to make the spacing more consistent and possible use a box ASCII GUI
    os.system('cls')
    print("""
     __                                         _____                       _____                              
    / () |)    _,   ,_          o        _,    () ||)                 _    () | ,_   _, _|__|_  _   ,_  o  _,  
   |     |/\  / |  /  | /|/|/|  | /|/|  / |       ||/\  |  | /|/|/|  |/       |/  | / |  |  |  / \_/  | | / |  
    \___/|  |/\/|_/   |/ | | |_/|/ | |_/\/|/    (/ |  |/ \/|/ | | |_/|_/    (/    |/\/|_/|_/|_/\_/    |/|/\/|_/
                                         (|               (|                     
                                                                       
    """)
    print("                🌹 Welcome to Charming Thyme Trattoria! 🌹                  ")
    print(" [1] Book a reservation 🍽️ ")
    print(" [2] Delete a reservation 🗑️ ")
    print(" [3] Edit a reservation ✍️ ")
    print(" [4] Recommend me a dish! 🍴")

def ReadReservationDatabase():
    '''Reads initial reservations from provided .txt file and write into customerReservations'''
    with open(initialReservationsTxt,"r") as reservationFile:
        initialReservationsList = reservationFile.read()
        for initialReservation in  initialReservationsList.split('\n'):
            customerReservations.append(initialReservation.split('|'))

def ReadMenuDatabase():
    '''Reads initial menu items from provided .txt file and write into menuItems'''
    with open(menuItemsTxt, "r") as menuFile:
        menuItemsList = menuFile.read()
        for menuItem in menuItemsList.split('\n'):
            menuItems.append(menuItem)

def WriteReservationList():
    pass

def DeleteReservationList():
    pass

def EditReservationList():
    pass


def GenerateMealRecommendation():
    print(f"🔥 Recommendation : {random.choice(menuItems)} 🔥")


if __name__ == '__main__':
    ReadReservationDatabase()
    ReadMenuDatabase()
    NavigateMenu()