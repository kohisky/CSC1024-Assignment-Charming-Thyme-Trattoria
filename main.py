import datetime
import random
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
    #TODO: evaluate matchcase vs elif
    if(navigateUserInput == 1):
        WriteReservationList()
    elif(navigateUserInput == 2):
        DeleteReservationList()
    elif(navigateUserInput == 3):
        EditReservationList()
    elif(navigateUserInput == 4):
        DisplayReservationList()
    elif(navigateUserInput == 5):
        GenerateMealRecommendation()
    elif(navigateUserInput == 6):
        os.system('cls')
    else: #not sure if this [else] is needed but wokay
        print("Expect The Unexpected")

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

def WriteReservationDatabase():
    pass

def GetReservationDate():
    """Ask user for date, checks if custom date is 5 days ahead of today, returns the date in iso format"""
    # TODO:Consider giving users to choose first 5 of the days available? if date have 32 bookings, X
    # Custom Date
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

        daysDifference = datetime.datetime.strptime(reservationDate, date_format) - datetime.datetime.today()
        if (daysDifference.days >= 5):
            return reservationDate

            break
        print(f"Earliest date for booking : {minDateInAdvanced}")
        print(daysDifference.days)
        # TODO:↑ Slightly confusing for the user as to a random number if unknown to the fact it is the day difference between today and the day enter ''

def CheckAvailableSessionAndSlot(date):
    """Given a date checks for available sessions and slots, return 2d list of available session and slots"""
    sessionSlots = [[],[],[],[]]
    for customerReservation in customerReservations:
        if customerReservation[0] == date:
            sessionSlots[int(customerReservation[1])-1].append(customerReservation[2])
    return sessionSlots

def GetReservationSession(sessionSlots):

    sessions = [
        [1, "12:00 pm - 02:00 pm"],
        [2, "02:00 pm - 04:00 pm"],
        [3, "06:00 pm - 08:00 pm"],
        [4, "08:00 pm - 10:00 pm"]
        ]
    for session in range(len(sessions)):
        if len(sessionSlots[session]) >= 8:
            sessions[session][0] = "X"

    while True:
        os.system('cls')  # TODO: make it not erase error messages
        print("{:^100}".format(" Please select a session "))
        for session in range(len(sessions)):
            print(f"[{sessions[session][0]}] {sessions[session][1]}")

        try:
            sessionReservationInput = int(input(("Please select a number : ")))
        except Exception:
            print("Please input a number from 1 to 4!")
            continue

        if (sessionReservationInput < 5) and (sessionReservationInput > 0):
            if sessions[sessionReservationInput-1][0] != "X":
                return sessionReservationInput
            else :
                print("Chosen Session is already full, please pick another!")
                continue
        print("Please input a number from 1 to 4!")

def GetReservationSlot(sessionSlots):

    slots = [
        [1, "Slot 1"],
        [2, "Slot 2"],
        [3, "Slot 3"],
        [4, "Slot 4"],
        [5, "Slot 5"],
        [6, "Slot 6"],
        [7, "Slot 7"],
        [8, "Slot 8"],
    ]
    print(sessionSlots)
    for slot in sessionSlots:
        slots[int(slot)-1][0] = "X"
    print(slots)

    while True:
        os.system('cls')
        print("{:^100}".format(" Please select a slot "))
        for slot in range(len(slots)):
            print(f"[{slots[int(slot)][0]}] {slots[int(slot)][1]}")

        try:
            slotReservationInput = int(input(("Please select a number : ")))
        except Exception:
            print("Please input a number from 1 to 8!")
            continue

        if (slotReservationInput < 9) and (slotReservationInput > 0):
            if slots[int(slotReservationInput)-1][0] != "X":
                return slotReservationInput
            else:
                print("Chosen slot is already full, please pick another!")
                continue
        print("Please input a number from 1 to 8!")

def GetUserName():
    os.system('cls')
    print(" Please type your name : ")
    nameReservationInput = input("Name : ").upper()
    return nameReservationInput

def GetUserEmail():
    #TODO:Add redundancy
    os.system('cls')
    print(" Please type your email : ")
    emailReservationInput = input("email : ")
    return emailReservationInput

def GetUserNumber():
    #TODO:add redundancy
    os.system('cls')
    print(" Please type your contact number ")
    numberReservationInput = input("contact number : ")
    return numberReservationInput

def GetUserPAX():
    #TODO:add redundancy
    os.system('cls')
    print(" How many people ")
    numberReservationInput = input("PAX : ")
    return numberReservationInput

def WriteReservationList():
    currentUserReservation = []
    #TODO: make these more readable
    currentUserReservation.append(GetReservationDate())
    currentUserReservation.append(str(GetReservationSession(CheckAvailableSessionAndSlot(currentUserReservation[0]))))
    currentUserReservation.append(str(GetReservationSlot(CheckAvailableSessionAndSlot(currentUserReservation[0])[int(currentUserReservation[1])-1])))
    currentUserReservation.append(GetUserName())
    currentUserReservation.append(GetUserEmail())
    currentUserReservation.append(GetUserNumber())
    currentUserReservation.append(GetUserPAX())
    print(currentUserReservation)


    #Confirmation
    #TODO: add confirm or cancel option + add to txt file
    os.system('cls')
    print(f""" Confirm booking :  
    Name : {currentUserReservation[3]}
    Date : {currentUserReservation[0]}
    Session : {currentUserReservation[2]}
    Slot : {currentUserReservation[1]}
    PAX : {currentUserReservation[6]}
    Number : {currentUserReservation[5]}
    Email : {currentUserReservation[4]}
    """)

    customerReservations.append(currentUserReservation)

def DisplayReservationList():
    os.system('cls')
    for customerReservation in customerReservations:
        print(customerReservation)

def DeleteReservationList(): #TODO ideas
    os.system('cls')
    DisplayReservationList()

def EditReservationList(): #TODO ideas
    file = open("reservation_StudentID.txt")

    #List to contain all initial information from "reservation_StudentID.txt"
    list = []
    #Reading the data from "reservation_StudentID.txt"
    data = file.read()
    #Putting the data into a list
    list = data.replace("\n", "|").split("|")
    list.pop(-1)

    start = True
    while start:
        try:
            #Using their phone number to find their reservation to edit
            pncheck = input("Please enter your number to find your Reservation.")
            mobilelocation = 5
            #Find/Check the location of the phone number in the list
            while pncheck != list[mobilelocation]:
                mobilelocation += 6
                if IndexError:
                    print("Number does not exist within the database.")
                    pncheck = input("Please enter your number to find your Reservation.")
                    mobilelocation = 5
                    continue
                else:
                    break

            datelocation = mobilelocation - 4
            slotlocation = mobilelocation - 3
            namelocation = mobilelocation - 2
            emaillocation = mobilelocation - 1
            paxlocation = mobilelocation + 1

            def customerdetails():
                print(f"""
Reservation Details:
Date  : {list[datelocation]}
Slot  : {list[slotlocation]}
PAX   : {list[paxlocation]}
Guest Details:
Name  : {list[namelocation]}
Mobile: {list[mobilelocation]}
Email : {list[emaillocation]}
""")
            customerdetails()

            correct = input("Is this your Reservation? [Yes/No] ").lower()

            while correct != 'yes' and correct != 'no':
                correct = input("Is this your Reservation? [Yes/No]").lower()
            if correct == 'no':
                start = False

            changeselection = input("""
Reservation Changes:
[1] Reschedule Reservation
[2] Change Your Personal Details
[3] No Changes
Select: """).lower()

            while changeselection != '1' and changeselection != '2' and changeselection != '3':
                changeselection = input("""
Reservation Changes:
[1] Reschedule Reservation
[2] Change Your Personal Details
[3] No Changes
Select: """).lower()
            
            if changeselection == '1':
                while True:
                    reservationdate = input("Please insert date (yyyy-mm-dd): ")
                    try:
                        reservationdate = datetime.date.fromisoformat(reservationdate)
                        reservationdate = datetime.datetime.date(reservationdate)
                        
                        daycheck = datetime.date(datetime.datetime.now() + datetime.timedelta(days=5))
                
                        if daycheck <= reservationdate:
                            list[datelocation] = str(reservationdate)
                            break
                        else:
                            print("Booking must be 5 days in advance")
                            continue
                        
                    except ValueError:
                        continue            
                
                list[slotlocation] = ("Slot " + str(input("""
Please select a slot
[1] 12:00 pm - 02:00 pm
[2] 02:00 pm - 04:00 pm
[3] 06:00 pm - 08:00 pm
[4] 08:00 pm - 10:00 pm
Select: """)))
                list[paxlocation] = input("PAX (1-4): ")
                customerdetails()

                confirm1 = input("Confirm changes? [Yes/No] ").lower()

                while confirm1 != 'yes' and confirm1 != 'no':
                    confirm1 = input("Confirm changes? [Yes/No]").lower()
                if confirm1 == 'no':
                    start = False

                numitem = len(list)
                one = 0 
                two = 6
                clear = open("reservation_StudentID.txt", "w")
                clear.write("")
                with open("reservation_StudentID.txt", "w") as edit:
                    while one != numitem:
                        edit.write("|".join(list[one:two]) + "\n")
                        one += 6; two += 6
                start = False
                
                

            elif changeselection == '2':
                list[namelocation] = input("Name: ")
                list[mobilelocation] = input("New Phone Number: ")
                list[emaillocation] = input("New E-mail Address: ")
                customerdetails()

                confirm2 = input("Confirm changes? [Yes/No] ").lower()

                while confirm2 != 'yes' and confirm2 != 'no':
                    confirm2 = input("Confirm changes? [Yes/No]").lower()
                if confirm2 == 'no':
                    start = False

                numitem = len(list)
                one = 0 
                two = 6
                clear = open("reservation_StudentID.txt", "w")
                clear.write("")
                with open("reservation_StudentID.txt", "w") as edit:
                    while one != numitem:
                        edit.write("|".join(list[one:two]) + "\n")
                        one += 6; two += 6
                    
                start = False

            elif changeselection == '3':
                start = False

        finally:
            again = input("Would you like to edit your reservation? [Yes/No] ").lower()

            while again != 'yes' and again != 'no':
                again = input("Would you like to edit your reservation? [Yes/No]").lower()

            if again == 'no':
                start = False
    file.close()


def GenerateMealRecommendation():
    print(f"🔥 Recommendation : {random.choice(menuItems)} 🔥")


if __name__ == '__main__':
    ReadReservationDatabase()
    ReadMenuDatabase()
    NavigateMenu()