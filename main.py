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
date_format = "%Y-%m-%d"
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
    print("{:^100}".format("🌹 Welcome to Charming Thyme Trattoria! 🌹")                  )

    print(" [1] Book a reservation 🍽️ ")
    print(" [2] Delete a reservation 🗑️ ")
    print(" [3] Edit a reservation ✍️ ")
    print(" [4] Recommend me a dish! 🍴")

    while True:
        try:
            navigateUserInput = int(input(("Please select a number : ")))
        except Exception:
            print("Please input a number from 1 to 4!")
            continue

        if (navigateUserInput < 5) and (navigateUserInput > 0):
            break

        print("Please input a number from 1 to 4!")

    if(navigateUserInput == 1):
        WriteReservationList()
    elif(navigateUserInput == 2):
        DeleteReservationList()
    elif(navigateUserInput == 3):
        EditReservationList()
    elif(navigateUserInput == 4):
        GenerateMealRecommendation()
    else:
        print("what the fuck did you fuck up")

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
    #TODO:Consider choosing days 5 days in advanced?
    minDateInAdvanced = datetime.date.today() + datetime.timedelta(days=5)
    print("{:^100}".format(f"Book a reservation! Earliest date for booking : {minDateInAdvanced}"))
    while True:
        reservationDate = input("Please insert date (yyyy-mm-dd): ")
        try:
            datetime.date.fromisoformat(reservationDate)
        except ValueError:
            print("Please insert date in the iso format (yyyy-mm-dd)!")
            continue
        
        if (datetime.datetime.strptime(reservationDate,date_format)-datetime.datetime.today()).days > 5:
            break
        print(f"Earliest date for booking : {minDateInAdvanced}")
    


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