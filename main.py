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
    print("{:^100}".format("🌹 Welcome to Charming Thyme Trattoria! 🌹"))

    print(" [1] Book a reservation   🍽️ ")
    print(" [2] Delete a reservation 🗑️ ")
    print(" [3] Edit a reservation   ✍️ ")
    print(" [4] Display Reservations 🗒️")
    print(" [5] Recommend me a dish! 🍴")
    print(" [6] Close Transaction    ✅")

    while True:
        try:
            navigateUserInput = int(input(("Please select a number : ")))
        except Exception:
            print("Please input a number from 1 to 6!")
            continue

        if (navigateUserInput < 7) and (navigateUserInput > 0):
            break

        print("Please input a number from 1 to 6!")

    if(navigateUserInput == 1):
        WriteReservationList()
    elif(navigateUserInput == 2):
        DeleteReservationList()
    elif(navigateUserInput == 3):
        EditReservationList()
    elif(navigateUserInput == 4):
        ReadReservationDatabase()
    elif(navigateUserInput == 5):
        GenerateMealRecommendation()
    elif(navigateUserInput == 6):
        os.system('cls')
    else: #not sure if this [else] is needed but wokay
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

    currentUserReservation = []

    #Date
    minDateInAdvanced = datetime.date.today() + datetime.timedelta(days=6)
    os.system('cls')
    print("{:^100}".format(f"Book a reservation! Earliest date for booking : {minDateInAdvanced}"))
    while True:
        reservationDate = input("Please insert date (yyyy-mm-dd): ")
        try:
            datetime.date.fromisoformat(reservationDate)
        except ValueError:
            print("Please insert date in the iso format (yyyy-mm-dd)!")
            continue

        daysDifference = datetime.datetime.strptime(reservationDate,date_format)-datetime.datetime.today()
        if (daysDifference.days >= 5):
            currentUserReservation.append(reservationDate)
            print(currentUserReservation) #TODO: 'Slot added to
            break
        print(f"Earliest date for booking : {minDateInAdvanced}")
        print(daysDifference.days) 
        ''' ↑ Slightly confusing for the user as to a random number 
        if unknown to the fact it is the day difference between today and the day enter '''

    #Slots
    while True:
        os.system('cls')
        print("{:^100}".format(" Please select a slot "))
        ''' There are 4 slot and not 8 "The restaurant only serves 4 sessions(slot) each day"
        The 8 reservation per session means in each session only 8 reservation is allowed
        So like slot 1 can accommodate 8 max, slot 2 accomodate 8 max, slot 3 accomodate 8 max, slot 4 accomodate 8 max
        hence in one day the maximum reservation allowed in 4 * 8 = 32 reservation. '''
        print(" [1] 12:00 pm - 02:00 pm")
        print(" [2] 02:00 pm - 04:00 pm")
        print(" [3] 06:00 pm - 08:00 pm")
        print(" [4] 08:00 pm - 10:00 pm")


        try:
            slotReservationInput = int(input(("Please select a number : ")))
        except Exception:
            print("Please input a number from 1 to 4!")
            continue

        if (slotReservationInput < 5) and (slotReservationInput > 0):
            currentUserReservation.append(f"Slot {slotReservationInput}")
            print(currentUserReservation) #TODO: 'Slot added to
            break

        print("Please input a number from 1 to 8!")

    #Name
    os.system('cls')
    print(" Please type your name : ")
    nameReservationInput = input("Name : ").upper()
    currentUserReservation.append(nameReservationInput)
    print(currentUserReservation)

    #Email TODO:Add redundancy
    os.system('cls')
    print(" Please type your email : ")
    emailReservationInput = input("email : ")
    currentUserReservation.append(emailReservationInput)
    print(currentUserReservation)

    #Contact number TODO:add redundancy
    os.system('cls')
    print(" Please type your contact number ")
    numberReservationInput = input("contact number : ")
    currentUserReservation.append(numberReservationInput)
    print(currentUserReservation)

    #PAX TODO:add redundancy
    os.system('cls')
    print(" How many people ")
    numberReservationInput = input("PAX : ")
    currentUserReservation.append(numberReservationInput)
    print(currentUserReservation)

    #Confirmation
    #TODO: add confirm or cancel option + add to txt file
    os.system('cls')
    print(f""" Confirm booking :  
    Name : {currentUserReservation[2]}
    Date : {currentUserReservation[0]}
    Slot : {currentUserReservation[1]}
    PAX : {currentUserReservation[5]}
    Number : {currentUserReservation[4]}
    Email : {currentUserReservation[3]}
    """)

    customerReservations.append(currentUserReservation)

def DisplayReservationList():
    for customerReservation in customerReservations:
        print(customerReservation)

def DeleteReservationList(): #TODO ideas
    os.system('cls')
    DisplayReservationList()
    pass

def EditReservationList(): #TODO ideas
    os.system('cls')
    DisplayReservationList()
    pass


def GenerateMealRecommendation():
    print(f"🔥 Recommendation : {random.choice(menuItems)} 🔥")


if __name__ == '__main__':
    ReadReservationDatabase()
    ReadMenuDatabase()
    NavigateMenu()