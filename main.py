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
    print("{:^100}".format(" Welcome to Charming Thyme Trattoria! "))

    print(" [1] Book a reservation   ")
    print(" [2] Delete a reservation  ")
    print(" [3] Edit a reservation    ")
    print(" [4] Display Reservations ")
    print(" [5] Recommend me a dish! ")
    print(" [6] Close Transaction   ")

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

def WriteReservationDatabase(userReservation):
    """Given a list of userReservation, write into provided .txt file, NOTE: DO NOT input a 2d list of userReservations"""
    string = ""
    for detail in userReservation:
        string += detail
        string += "|"
    string += "\n"

    with open(initialReservationsTxt,"w") as reservationFile:
        reservationFile.write(string)

def GetReservationDate():
    """Ask user for date, checks if custom date is 5 days ahead of today, returns the date in iso format"""
    # TODO:Consider giving users to choose first 5 of the days available? if date have 32 bookings, X
    # Custom Date
    minDateInAdvanced = datetime.date.today() + datetime.timedelta(days=6)
    errorMessage = " "

    while True:
        os.system('cls')
        print("{:^100}".format(f"Book a reservation! Earliest date for booking : {minDateInAdvanced}"))
        print(errorMessage)
        reservationDate = input("Please insert date (yyyy-mm-dd): ")
        try:
            datetime.date.fromisoformat(reservationDate)
        except ValueError:
            errorMessage = "Please insert date in the iso format (yyyy-mm-dd)!"
            continue

        daysDifference = datetime.datetime.strptime(reservationDate, date_format) - datetime.datetime.today()
        if (daysDifference.days >= 5):
            return reservationDate
            break
        errorMessage = f"Earliest date for booking : {minDateInAdvanced}"

def CheckAvailableSessionAndSlot(date):
    """Given a date checks for available sessions and slots, return 2d list of available session and slots"""
    sessionSlots = [[],[],[],[]]
    for customerReservation in customerReservations:
        if customerReservation[0] == date:
            sessionSlots[int(customerReservation[1])-1].append(customerReservation[2])
    return sessionSlots

def GetReservationSession(sessionSlots):
    errorMessage = ""

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
        os.system('cls')
        print("{:^100}".format(" Please select a session "))
        for session in range(len(sessions)):
            print(f"[{sessions[session][0]}] {sessions[session][1]}")

        print(errorMessage)
        try:
            sessionReservationInput = int(input(("Please select a number : ")))
        except Exception:
            errorMessage = "Please input a number from 1 to 4!"
            continue

        if (sessionReservationInput < 5) and (sessionReservationInput > 0):
            if sessions[sessionReservationInput-1][0] != "X":
                return sessionReservationInput
            else :
                errorMessage = "Chosen Session is already full, please pick another!"
                continue
        errorMessage = "Please input a number from 1 to 4!"

def GetReservationSlot(sessionSlots):
    errorMessage = " "
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
    for slot in sessionSlots:
        slots[int(slot)-1][0] = "X"
    print(slots)

    while True:
        os.system('cls')
        print("{:^100}".format(" Please select a slot "))
        for slot in range(len(slots)):
            print(f"[{slots[int(slot)][0]}] {slots[int(slot)][1]}")

        print(errorMessage)
        try:
            slotReservationInput = int(input(("Please select a number : ")))
        except Exception:
            errorMessage = "Please input a number from 1 to 8!"
            continue

        if (slotReservationInput < 9) and (slotReservationInput > 0):
            if slots[int(slotReservationInput)-1][0] != "X":
                return slotReservationInput
            else:
                errorMessage = "Chosen slot is already full, please pick another!"
                continue
        errorMessage = "Please input a number from 1 to 8!"

def GetUserName():
    errorMessage = ""
    while True:
        os.system('cls')
        print("{:^100}".format(" Please type your name"))
        print(errorMessage)
        nameReservationInput = input("Name : ").upper()
        if nameReservationInput.isalpha():
            break
        else:
            errorMessage = "Please type a proper name!"
    return nameReservationInput

def GetUserEmail():
    errorMessage = " "
    while True:
        os.system('cls')
        print("{:^100}".format(" Please type your e-mail address "))
        print(errorMessage)
        emailReservationInput = input("E-mail : ")
        if len(emailReservationInput) > 6:
            break
        else:
            errorMessage = "Please type a proper e-mail address!"
    return emailReservationInput

def GetUserNumber():
    errorMessage = " "
    while True:
        os.system('cls')
        print("{:^100}".format (" Please type your contact number "))
        print(errorMessage)
        numberReservationInput = input("Contact number : ")
        if numberReservationInput.isnumeric():
            break
        else:
            errorMessage = "Please type your phone number without any space/hyphens!"
    return numberReservationInput

def GetUserPAX():
    errorMessage = " "
    while True:
        os.system('cls')
        print("{:^100}".format(" Please type the number of people "))
        print(errorMessage)
        PAXReservationInput = input("PAX : ")
        try:
            if (int(PAXReservationInput) > 0) and (int(PAXReservationInput) < 5):
                break
            else :
                errorMessage = "Restaurant seating can only accommodate 1 to 4 people only!"
        except Exception:
            errorMessage = "Please insert a number!"
    return PAXReservationInput

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
    while True:
        os.system('cls')
        print(f""" Guest Details:
            Name : {currentUserReservation[3]}
            Number : {currentUserReservation[5]}
            Email : {currentUserReservation[4]}
    
            Reservation Details:
            Date : {currentUserReservation[0]}
            Session : {currentUserReservation[2]}
            Slot : {currentUserReservation[1]}
            PAX : {currentUserReservation[6]}
            """)

        confirmation = input("Confirm? [y/n] : ").upper()
        if confirmation == "Y":
            WriteReservationDatabase(currentUserReservation)
            customerReservations.append(currentUserReservation)
            break
        elif confirmation == "N":
            WriteReservationList()
            break
        else:
            continue
    NavigateMenu()

def GetUserReservationList(phoneNumber):
    """Given a phone number, return a list containing all reservation of said person"""
    userReservations = []

    for customerReservation in customerReservations:
        if customerReservation[5] == phoneNumber:
            userReservations.append(customerReservation)
    return userReservations

def DisplayReservationList(userReservations):
    """Given a reservation list, print all details of all reservations"""
    for userReservation in userReservations:
        print(f""" Guest Details:
            Name : {userReservation[3]}
            Number : {userReservation[5]}
            Email : {userReservation[4]}

            Reservation Details:
            Date : {userReservation[0]}
            Session : {userReservation[2]}
            Slot : {userReservation[1]}
            PAX : {userReservation[6]}
            """)

def DeleteReservationList(): #TODO ideas Ask for phone number
    os.system('cls')
    DisplayReservationList()

def EditReservationList():
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