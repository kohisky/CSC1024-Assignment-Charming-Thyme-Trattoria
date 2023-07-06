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
    ReadReservationDatabase()
    ReadMenuDatabase()
    outputMessage = ''
    while True:
        os.system('cls')
        print("""
  __                                         _____                       _____                              
 / () |)    _,   ,_          o        _,    () ||)                 _    () | ,_   _, _|__|_  _   ,_  o  _,  
|     |/\  / |  /  | /|/|/|  | /|/|  / |       ||/\  |  | /|/|/|  |/       |/  | / |  |  |  / \_/  | | / |  
 \___/|  |/\/|_/   |/ | | |_/|/ | |_/\/|/    (/ |  |/ \/|/ | | |_/|_/    (/    |/\/|_/|_/|_/\_/    |/|/\/|_/
                                      (|               (|                     
           """)
        print("{:=^108}".format(" Welcome to Charming Thyme Trattoria! "))

        print(" [1] Book a reservation ")
        print(" [2] Cancel a reservation ")
        print(" [3] Edit a reservation ")
        print(" [4] Display Reservation ")
        print(" [5] Recommend me a dish! ")
        print(" [6] Close Transaction ")
        print("\n")
        print(outputMessage)
        try:
            navigateUserInput = int(input((" Please select a number : ")))
        except Exception:
            outputMessage = " Please input a number!"
            continue
        if (navigateUserInput > 7) or (navigateUserInput < 0):
            outputMessage = " Please input a number from 1 to 6!"
            continue

        #TODO: evaluate matchcase vs elif
        if(navigateUserInput == 1):
            outputMessage = WriteReservationList()
        elif(navigateUserInput == 2):
            outputMessage = DeleteReservationList()
        elif(navigateUserInput == 3):
            outputMessage = EditReservationList()
        elif(navigateUserInput == 4):
            userPhoneNumber = input(" Please insert your phone number : ")
            outputMessage = DisplayReservationList(GetUserReservationList(userPhoneNumber))
        elif(navigateUserInput == 5):
            outputMessage = GenerateMealRecommendation()
        elif(navigateUserInput == 6):
            print(" Closing Application")
            start_time = datetime.datetime.now()
            end_time = start_time + datetime.timedelta(seconds = 1)
            while datetime.datetime.now() < end_time:
                continue
            os.system('cls')
            break
        else: #not sure if this [else] is needed but wokay
            print("Expect The Unexpected")
        continue

def ReadReservationDatabase():
    '''Reads initial reservations from provided .txt file and write into customerReservations'''
    customerReservations.clear()
    with open(initialReservationsTxt,"r") as reservationFile:
        initialReservationsList = reservationFile.read()
        for initialReservation in initialReservationsList.split('\n'):
            customerReservations.append(initialReservation.split('|'))

def ReadMenuDatabase():
    '''Reads initial menu items from provided .txt file and write into menuItems'''
    with open(menuItemsTxt, "r") as menuFile:
        menuItemsList = menuFile.read()
        for menuItem in menuItemsList.split('\n'):
            menuItems.append(menuItem)

def WriteReservationDatabase():
    """update provided .txt file with the customerReservation"""
    string = ""
    for customerReservation in customerReservations:
        for detail in customerReservation:
            string += detail
            string += "|"
        string = string[:-1]
        string += "\n"
    string = string[:-1]
    with open(initialReservationsTxt,"w") as reservationFile:
        reservationFile.write(string)


def GetReservationDate(bookedout = False):
    """Ask user for date, checks if custom date is 5 days ahead of today, returns the date in iso format"""
    # Custom Date
    minDateInAdvanced = datetime.date.today() + datetime.timedelta(days=5)
    errorMessage = " "

    while True:
        os.system('cls')
        print("{:=^108}".format(f" Booking Reservation "))
        print(f"Earliest date for booking : {minDateInAdvanced} ")
        if bookedout:
            print("Chosen Date is fully booked out, please choose another date.")
            bookedout = False  
        else:
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
        errorMessage = ""

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
    
    if sessions[0][0] == "X" and sessions[1][0] == "X" and sessions[2][0] == "X" and sessions[3][0] == "X":
        return None
             
    else:    
        while True:
            os.system('cls')
            print("{:=^108}".format(f" Session Selection "))
            if sessions[0][0] == "X" or sessions[1][0] == "X" or sessions[2][0] == "X" or sessions[3][0] == "X":
                print("{:^108}".format(" 'X' means Booked & Unavailable "))
            print("Please select a session")
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
        print("{:=^108}".format(f" Slot Selection "))
        if slots[0][0] == "X" or slots[1][0] == "X" or slots[2][0] == "X" or slots[3][0] == "X" or slots[4][0] == "X" or slots[5][0] == "X" or slots[6][0] == "X" or slots[7][0] == "X":
            print("{:^108}".format(" 'X' means Booked & Unavailable "))
        print("Please select a slot ")
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
        print("{:=^108}".format(f" Booking Reservation "))
        print("Please enter your name")
        print(errorMessage)
        nameReservationInput = input("Name : ").upper()
        if all(char.isalpha() or char.isspace() for char in nameReservationInput):
            return nameReservationInput
        else:
            errorMessage = "Please enter without symbols or number."

def GetUserEmail():
    errorMessage = " "
    while True:
        os.system('cls')
        print("{:=^108}".format(f" Booking Reservation "))
        print("Please enter your e-mail address")
        print(errorMessage)
        emailReservationInput = input("E-mail : ")
        if len(emailReservationInput) > 6:
            break
        else:
            errorMessage = "Please enter a proper e-mail address!"
    return emailReservationInput

def GetUserNumber():
    errorMessage = " "
    while True:
        os.system('cls')
        print("{:=^108}".format(f" Booking Reservation "))
        print("Please enter your contact number")
        print(errorMessage)
        numberReservationInput = input("Contact number : ")
        if numberReservationInput.isnumeric():
            break
        else:
            errorMessage = "Please enter your phone number without any space/hyphens."
    return numberReservationInput

def GetUserPAX():
    errorMessage = " "
    while True:
        os.system('cls')
        print("{:=^108}".format(f" Booking Reservation "))
        print("Please enter the number of people attending")
        print(errorMessage)
        PAXReservationInput = input("PAX : ")
        try:
            if (int(PAXReservationInput) > 0) and (int(PAXReservationInput) < 5):
                break
            else :
                errorMessage = "Restaurant seating can only accommodate 1 to 4 people only!"
        except Exception:
            errorMessage = "Please enter a number!"
    return PAXReservationInput

def WriteReservationList():
    currentUserReservation = []
    reservation_date = GetReservationDate()
    currentUserReservation.append(reservation_date)
    session_slots = CheckAvailableSessionAndSlot(reservation_date)
    reservation_session = GetReservationSession(session_slots)
    while reservation_session is None:
        # All sessions are fully booked, prompt the user to choose a new date
        reservation_date = GetReservationDate(True)
        currentUserReservation[0] = reservation_date
        session_slots = CheckAvailableSessionAndSlot(reservation_date)
        reservation_session = GetReservationSession(session_slots)
        continue
    currentUserReservation.append(str(reservation_session))
    currentUserReservation.append(str(GetReservationSlot(session_slots[int(reservation_session)-1])))
    currentUserReservation.append(GetUserName())
    currentUserReservation.append(GetUserEmail())
    currentUserReservation.append(GetUserNumber())
    currentUserReservation.append(GetUserPAX())

    #Confirmation
    while True:
        os.system('cls')
        print("{:=^108}".format(f" Confirm Reservation "))
        print(f""" 
Guest Details:
Name : {currentUserReservation[3]}
Number : {currentUserReservation[5]}
Email : {currentUserReservation[4]}

Reservation Details:
Date : {currentUserReservation[0]}
Session : {currentUserReservation[1]}
Slot : {currentUserReservation[2]}
PAX : {currentUserReservation[6]}
            """)

        confirmation = input("Confirm? [y/n] : ").upper()
        if confirmation == "Y":
            customerReservations.append(currentUserReservation)
            WriteReservationDatabase()
            break
        elif confirmation == "N":
            NavigateMenu()
            break
        else:
            continue
    return " 1 Reservation Added! Thank you very much!"

def GetUserReservationList(phoneNumber):
    """Given a phone number, return a list containing all reservation of said person"""
    userReservations = []

    for customerReservation in customerReservations:
        try:
            if (customerReservation[5]) == phoneNumber:
                userReservations.append(customerReservation)
        except Exception as e:
            pass
    return userReservations

def DisplayReservationList(userReservations):
    """Given an array of reservations list, print all details of all reservations in strings"""
    reservationsString =""
    counter = 1
    if len(userReservations) == 0:
        return " There are no reservations under this number!"
    for userReservation in userReservations:

        reservationsString += f"\nReservation {counter}"
        reservationsString += "\n"
        reservationsString += (f"""
Guest Details:
Name : {userReservation[3]}
Number : {userReservation[5]}
Email : {userReservation[4]}

Reservation Details:
Date : {userReservation[0]}
Session : {userReservation[1]}
Slot : {userReservation[2]}
PAX : {userReservation[6]}
            """)
        reservationsString += "\n"
        counter+= 1
    return reservationsString

def GetReservationListToDelete(userReservations):
    """Given a reservations list, prompts user to choose one reservation to delete, return a reservation array"""
    while True:
        try:
            reservationToDelete = int(input("Which reservation would you like to cancel? : Reservation ")) - 1
            if (reservationToDelete < len(userReservations)) and (reservationToDelete >= 0):
                print(DisplayReservationList([userReservations[reservationToDelete]]))
                os.system('cls')
                while True:
                    print("{:=^108}".format(" Confirm Reservation "))
                    print(DisplayReservationList([userReservations[reservationToDelete]]))
                    confirmation = input("Confirm? (y/n) :").upper()
                    if confirmation == "Y":
                        return userReservations[reservationToDelete]
                    elif confirmation == "N":
                        return []
                    else:
                        continue
            else:
                print("Pick a reservation number you would like to cancel.")
        except Exception as e:
            print(e)
            print("Pick a number!")

    return []

def DeleteReservationList():
    while True:
        os.system('cls')
        print("{:=^108}".format(f" Cancelling Reservation "))
        userPhoneNumber = input("Please enter your phone number : ")
        if userPhoneNumber.isnumeric():
            break
    userReservationList = GetUserReservationList(userPhoneNumber)
    print(DisplayReservationList(userReservationList))
    if len(userReservationList) <= 0:
        return " No reservation cancelled : no reservations were made under the given number"
    reservationListToDelete = GetReservationListToDelete(userReservationList)
    if len(reservationListToDelete) <= 0:
        return " No reservation cancelled"
    customerReservations.remove(reservationListToDelete)
    WriteReservationDatabase()
    return " 1 reservation cancelled"

def EditReservationList():
    errorMessage = ""
    while True:
        os.system('cls')
        print("{:=^108}".format(f" Editing Reservation "))
        userPhoneNumber = input(" Please insert your phone number : ")
        if userPhoneNumber.isnumeric():
            break
    userReservationList = GetUserReservationList(userPhoneNumber)
    print(DisplayReservationList(userReservationList))
    if len(userReservationList) <= 0:
        return " No reservation edited : no reservations were made under the given number"
    reservationListToDelete = GetReservationListToDelete(userReservationList)
    reservationListToAdd = reservationListToDelete
    if len(reservationListToDelete) <= 0:
        return " No reservation edited"
    customerReservations.remove(reservationListToDelete)
    WriteReservationDatabase()
    ReadReservationDatabase()
    while True:
        os.system('cls')
        print("{:=^108}".format(f" Editing Reservation "))
        print(DisplayReservationList([reservationListToDelete]))
        print(f"{errorMessage}")
        try:
            editSelection = (input
("""Reservation Changes:
[1] Reschedule Reservation
[2] Change Your Personal Details
[3] No Changes
Please select a number : """))
        except Exception:
            errorMessage = "Please choose a number!"

        if editSelection == "1":
            reservationListToAdd[0] = str(GetReservationDate())
            reservationListToAdd[1] = str(GetReservationSession(CheckAvailableSessionAndSlot(reservationListToAdd[0])))
            reservationListToAdd[2] = str(GetReservationSlot((CheckAvailableSessionAndSlot(reservationListToAdd[0])[int(reservationListToAdd[1])-1])))
            break
        elif editSelection == "2":
            reservationListToAdd[3] = GetUserName()
            reservationListToAdd[4] = GetUserEmail()
            reservationListToAdd[5] = GetUserNumber()
            reservationListToAdd[6] = GetUserPAX()
            break
        elif editSelection == "3":
            customerReservations.append(reservationListToDelete) #Append again the reservation when no changes are done
            return " "
        else:
            errorMessage = "Please choose a number from below."
        continue

    customerReservations.append(reservationListToAdd)
    WriteReservationDatabase()
    return " 1 reservation edited"

def GenerateMealRecommendation():
    string = ''
    for menuItem in menuItems:
        string += menuItem
        string += "\n"
    return f"{string}\n Recommendation : {random.choice(menuItems)} "


if __name__ == '__main__':
    NavigateMenu()