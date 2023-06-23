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

def ReadReservationDatabase():
    '''Reads initial reservations from provided .txt file and write into customerReservations'''
    with open(initialReservationsTxt,"r") as reservationFile:
        initialReservationsList = reservationFile.read()
        for initialReservation in  initialReservationsList.split('\n'):
            customerReservations.append(initialReservation.split('|'))

def WriteReservationList():
    pass

def DeleteReservationList():
    pass

def EditReservationList():
    pass

def ReadMenuDatabase():
    with open(menuItemsTxt, "r") as menuFile:
        menuItemsList = menuFile.read()
        for menuItem in menuItemsList.split('\n'):
            menuItems.append(menuItem)

def GenerateMealRecommendation():
    print(f"🔥 Recommendation : {random.choice(menuItems)} 🔥")




if __name__ == '__main__':
    ReadReservationDatabase()
    ReadMenuDatabase()