# *********************************************************
# Program: TL09_G08.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Tutorial Section: TL09 Group: G08
# Trimester: 2215
# Year: 2022/23 Trimester 1
# Member_1: 1211109536 | TAN ZEC VONE
# Member_2: 1211109413 | CHIOK KAH YANG
# Member_3: 1211110389 | ONG YI ZHI
# Member_4: 1211111490 | FARISYA NAZWA BINTI MOHD NAZRIHADI
# *********************************************************
# Task Distribution
# Member_1: login & signup, booking + edit booking feature, payment + edit prices feature, flowcharts
# Member_2: Coach selection feature, edit promocode feature, flowcharts
# Member_3: Training plan feature, progress report feature, flowcharts
# Member_4: Member details feature, gym review feature, flowcharts
# *********************************************************

import random
import string #so that we can use string.ascii_letters later to generate special code
import sys #so that we can use sys.exit() to exit the current python script later
from datetime import datetime
current_time = datetime.now().strftime('%I:%M %p') #%I:%M %p is a format string that can be passed to strftime() to represent the time in the format of hours (12-hour clock) : minutes : AM/PM
current_date = datetime.now().strftime('%d-%b-%Y') #%d-%b-%Y is a format string that can be passed to strftime() to represent the date in the format of day-month-year
available_slots = ["9:00-10:00", "10:00-11:00", "11:00-12:00", "12:00-13:00", "13:00-14:00", "14:00-15:00", "15:00-16:00", "16:00-17:00", "17:00-18:00"]
promocode1 = ["gym0001","gym0010","gym0011"]
promocode2 = ["gym0100","gym0101","gym0110"]
specializations = ["1", "2", "3", "4", "5"] #this list corresponds with the prices list
prices = [50, 80, 70, 85, 85]
coach_price = [] #create an empty list to append selected specializations' prices
coaches1 = ["Marcus", "Bob", "Jane", "Emily"] 
coaches2 = ["Max", "Jayden", "Angel", "Ivy"] 
coaches3 = ["Carter", "Mason", "Sophie", "Chloe"]
coaches4 = ["William", "James", "Alice", "Amelia"]
coaches5 = ["Ivan", "Gilbert", "Charlotte", "Amanda"]

#rewrite the users' info when restarting the program
with open("users.txt", "w") as f:
  f.write("")
with open("user_details.txt", "w") as f:
  f.write("")

#showing the big title of "Gym Management System" with a box
def show_title():
  title = "  GYM MANAGEMENT SYSTEM"
  width = len(title) + 4
  print("\n+" + "-" * width + "+")
  print("| " + title + "   |")
  print("+" + "-" * width + "+")

#showing the main menu
def main_menu():
  show_title()
  print("\nWelcome to our gym management system! Please select an option from the main menu:")
  print("1. New user")
  print("2. Registered member")
  print("3. Admin")
  while True: #use while loop so that the program will prompt the user to enter the choice repeatedly if the input is invalid
    choice = input("Enter your choice: ")
    if choice == "1":
      sign_up()
    elif choice == "2":
      with open ("users.txt", "r") as f: #read the info in users.txt
        content = f.readlines()
      if not content:
        while True:
          ask_registration = input("\nYou haven't registered as a member yet. Do you want to register now? (y/n) ")
          if ask_registration == "y":
            sign_up()
          elif ask_registration == "n":
            print("Okay! Returning to the main menu...")
            main_menu()
          else:
            print("Invalid choice. Please try again.")
      else:
        log_in_member()
    elif choice == "3":
      log_in_admin()
    else:
      print("\nInvalid choice. Please try again.")

#sign up for new member
def sign_up():
  print("\n--- Enter your details here ---")
  name = input("Enter your name: ")
  age = input("Enter your age: ")
  phone = input("Enter your phone number: ")
  address = input("Enter your address: ")
  code = input("Enter a password for your account: ")

  #write the users info in users.txt file
  with open("users.txt", "a") as f:
    f.write(f"{name},{age},{phone},{address},{code}")
  with open("user_details.txt", "a") as f:
    f.write(f"Name: {name}, Age: {age}, Phone: {phone}, Address: {address}\n")

  #generate a special code for new user
  def generate_code():
    code_characters = random.choices(string.ascii_letters + string.digits, k=4) #k=4 means a four digits code
    return "".join(code_characters)
  code = generate_code()
  print("Here's your code: ", code, "\nPlease enter the 4-digits code to prove that you are not a robot.")
  while True:
    user_code = input("Enter the code here: ")
    if user_code == code:
      print(f"\nCongratulations! You have successfully registered yourself as a new member at {current_date}, {current_time}.")
      break
    else:
      print("Incorrect code, please try again.") #can limit the number of tries
  while True:
    log_in_choice = input("\nDo you want to log in? (y/n) ")
    if log_in_choice == "y":
      log_in_member()
    elif log_in_choice == "n":
      while True:
        is_return = input("Do you want to return to the main menu? (y/n) ")
        if is_return == "y":
          main_menu()
        elif is_return == "n":
          print("Thank you for signing up! Exiting the program...")
          sys.exit() #to make sure the program exits instead of looping it again
        else:
          print("\nInvalid selection. Please try again.")
    else:
      print("Invalid selection. Please try again.")

#check if the username and password set during registration is the same during log in process
def check_credentials(username, password):
  with open("users.txt", "r") as f: 
    for line in f:
      context = line.strip().split(",") #this code split the user's info in a line into individual element
      if username == context[0] and password == context[4]: #take the 0 (username) and the 4th (password) elements to check
        return True
  return False

#show member details
def show_member_details(username):
  with open("users.txt", "r") as f:
    lines = f.readlines()
    first_line = lines[0]
    context = first_line.strip().split(",")
  if username == context[0]:
    return context[0], context[1], context[2], context[3] #return the first four info, excluding the password
  return "", "", "", ""

#rewrite the booking.txt file when the program restarts
with open("booking.txt", "w") as f: 
  f.write("")

#allow members to book desired slots
def book_slot(username):
  print("\n--- Available slots ---")
  for i, slot in enumerate(available_slots): #the enumerate function iterates over a sequence (in this case, it's a list) and return both the index and the value of each element.
    print(f"{i+1}. Slot {slot}")
  booking_choice = input("Enter the number of the slot you want to book: ")
  try:
    booking_choice = int(booking_choice)
    if booking_choice > 0 and booking_choice <= len(available_slots): #to make sure the choice is within the list
      selected_slot = available_slots.pop(booking_choice-1) #pop function can remove and return an element from a list, since the starting index is 0, we need to use choice-1 instead of choice
      print(f"You have successfully booked slot {selected_slot}!")
      with open("booking.txt", "a") as f: #write the selected slots accordingly into booking.txt, so that it can be used to calculate payment later on
        f.write(str(selected_slot)+"\n")
      while True:
        book_agn = input("\nDo you want to book another slot? (y/n) ")
        if book_agn == "y":
          book_slot(username)
        elif book_agn == "n":
          while True:
            is_return = input("\nDo you want to return to the member menu? (y/n) ")
            if is_return == "y":
              member_menu(username)
            elif is_return == "n":
              print("Okay, exiting the program...")
              sys.exit()
            else:
              print("Invalid choice. Please try again.")
        else:
          print("Invalid choice. Please try again.")
    else:
      print("Invalid choice. Please try again.")
  except ValueError:
    print("Invalid choice. Please try again.")

def show_payment_details(username): 
  #read booking.txt and multiply the num of slots by 50 (price of a slot = RM50)
  with open('booking.txt', 'r') as f: 
    lines = f.readlines()
  num_slots = len (lines)
  price = num_slots * 50
  print("\n--- Calculate your payment here ---")
  print(f"Number of slots booked: {num_slots}")
  print(f"Price of one slot: RM 50")
  print(f"Total price for booked slot(s): RM {price}")
  total_coach_price = 0
  for i in coach_price: #we've created a coach_price list, and each time when the user selects a specialization, it will append the corresponding price to the list, so we have to add up each element in that list to get the total_coach_price
    total_coach_price += int(i)
  if len(coach_price) != 0: #make sure it only shows up when someone selected a coach
    print(f"Total price for booked coach(es): RM {total_coach_price}")
  print("★ Type 1 Promocode ★") #shows the promocode in order from promocode1 and promocode2 lists above
  for i, code in enumerate(promocode1):
    print(f"{i+1}. Code {code}")
  print("★ Type 2 Promocode ★")
  for i, code in enumerate(promocode2):
    print(f"{i+1}. Code {code}")
  total_price = 0
  #diff discounts for promocode in diff lists
  while True:
    promocode = input("Enter your promotion code (if no promocode, enter none): ")
    if promocode in promocode1:
      total_price = (total_coach_price + price)*0.8
      print("You got a 20", "%", "discount!")
    elif promocode in promocode2:
      total_price = (total_coach_price + price)*0.7
      print("You got a 30", "%", "discount!")
    elif promocode == "none":
      total_price = total_coach_price + price
    else:
      print("Invalid input! Please try again.")
    if total_price != 0:
      break
  print(f"Total price: RM {total_price}")
  while True:
    is_return = input("\nDo you want to return to the member menu? (y/n) ")
    if is_return == "y":
      member_menu(username)
    elif is_return == "n":
      print("Okay, exiting the program...")
      sys.exit()
    else:
      print("Invalid choice. Please try again.")

#allow users to select desired coaches
def select_coach(username, coaches): #two arguments are passed, "username" is to identify the identity of a user, and "coaches" can be replaced by diff specializations coaches' list later on  
    print("\n--- Available coaches ---")
    for i, coach in enumerate(coaches):
        print(f"{i+1}. Coach {coach}")
    while True:
        choice = input("Enter the number of the coach you want to choose: ")
        choice = int(choice)
        if choice > 0 and choice <= len(coaches):
            selected_coach = coaches.pop(choice-1)
            print(f"You have successfully selected {selected_coach}!")
            while True:
                choose_agn = input("\nDo you want to choose another specialization? (y/n) ")
                if choose_agn == "y":
                  coach_menu(username)
                elif choose_agn == "n":
                    while True:
                        is_return = input("\nDo you want to return to the member menu? (y/n) ")
                        if is_return == "y":
                          member_menu(username)
                        elif is_return == "n":
                          print("Okay, exiting the program...")
                          sys.exit()
                        else:
                          print("Invalid choice. Please try again.")
                else:
                  print("Invalid choice. Please try again.")
        else:
          print("Invalid choice. Please try again.")

#show prices for each specialization orderly
def show_prices():
  print("\n--- Current Prices ---")
  for i, price in enumerate(prices):
    print(f"{i+1}. Specialization {i+1}: RM {price}")

#admin can edit price of each specialization accordingly
def edit_prices():
    show_prices()
    while True:
      specialization_choice = input("Enter the number of the specialization you want to edit: ")
      specialization_choice = int(specialization_choice)
      if specialization_choice > 0 and specialization_choice <= len(prices):
        new_price = input("Enter the new price: ")
        prices[specialization_choice-1] = new_price
        print(f"Specialization {specialization_choice} price is now RM {new_price}.")
        while True:
          choose_agn = input("\nDo you want to edit the price of another specialization? (y/n) ")
          if choose_agn == "y":
            edit_prices()
          elif choose_agn == "n":
              while True:
                  is_return = input("\nDo you want to return to the admin menu? (y/n) ")
                  if is_return == "y":
                    admin_menu()
                  elif is_return == "n":
                    print("Okay, exiting the program...")
                    sys.exit()
                  else:
                    print("Invalid choice. Please try again.")
      else:
        print("Invalid choice. Please try again.")

#show the coach selection menu
def coach_menu(username):
  print("\n--- Please select a specialization from the options below ---")
  print("1. Nutrition Specialization")
  print("2. Strength & Conditioning Specialization")
  print("3. Corrective Exercise Specialization")
  print("4. Yoga Specialization")
  print("5. Weight Management Specialization")
  while True:
    specialization_selection = input("Enter the number of specialization you would like to select: ")
    if specialization_selection in specializations:
      index = specializations.index(specialization_selection) #use .index() function to find the index of the first occurrence of a specific element in a list
      price = prices[index] #pass the index to the prices list, to obtain the price of that specific specialization
      print("★ The price for this specilization is RM" + str(price) + ". Added to the payment bill. ★")
      coach_price.append(price) #add it to the coach_price list for further payment calc. feature
    if specialization_selection == "1":
      select_coach(username, coaches1)
    elif specialization_selection == "2":
      select_coach(username, coaches2)
    elif specialization_selection == "3":
      select_coach(username, coaches3)
    elif specialization_selection == "4":
      select_coach(username, coaches4)
    elif specialization_selection == "5":
      select_coach(username, coaches5)
    else:
      print("\nInvalid selection. Please try again.")

#check if a user wants to return to the training plan menu
def is_return_training_plan(username):
    while True:
        is_return = input("Do you want to select another training plan? (y/n) ")
        if is_return == "y":
            training_plan(username)
        elif is_return == "n":
            while True:
                is_return_member = input("Do you want to return to the member menu? (y/n) ")
                if is_return_member == "y":
                  member_menu(username)
                elif is_return_member == "n":
                  print("Okay, exiting the program...")
                  sys.exit()
                else:
                  print("Invalid selection. Please try again.")
        else:
            print("\nInvalid selection. Please try again.")

#show the training plan menu for user
def training_plan(username):
    print("\n-- This is a 30 days training reference for you --")
    print("1. Full body")
    print("2. Arm")
    print("3. Chest")
    print("4. Leg")
    while True:
        num = int(input("Please select one from the menu: "))
        if num == 1:
            print("\n★ Let's start training your full body! ★")
            print("Jumping jacks    : 20 seconds")
            print("Push-ups         : 5 times")
            print("Knee push-ups    : 10 times")
            print("Incline push-ups : 12 times")
            print("Plank            : 30 seconds")
            print("Mountain climber : 20 times")
            print("Russian twist    : 10 times")
            print("Cobra stretch    : 20 seconds")
            print("Chest stretch    : 20 seconds")
            print("Here's your daily training plan, there are 9 workouts with 7 minutes, feel free to adjust according to your own needs!\n")
            is_return_training_plan(username)
        elif num == 2:
            print("\n★ Let's start training your arm! ★")
            print("Arm raises                   : 30 seconds")
            print("Side arm raise               : 30 seconds")
            print("Triceps dips                 : 10 times")
            print("Arm circles clockwise        : 30 seconds")
            print("Arm circles counterclockwise : 30 seconds")
            print("Diamond push-ups             : 5 times")
            print("Diagonal plank               : 10 times")
            print("Push-ups                     : 10 times")
            print("Here's your daily training plan, there are 8 workouts with 6 minutes, feel free to adjust according to your own needs!\n")
            is_return_training_plan(username)
        elif num == 3:
            print("\n★ Let's start training your chest! ★")
            print("Jumping jacks     : 30 seconds")
            print("Incline push-ups  : 10 times")
            print("Push-ups          : 8 times")
            print("Wide arm push-ups : 8 times")
            print("Triceps dips      : 1o times")
            print("Knee push-ups     : 8 times")
            print("Cobra stretch     : 20 seconds")
            print("Chest stretch     : 20 seconds")
            print("Here's your daily training plan, there are 8 workouts with 6 minutes, feel free to adjust according to your own needs!\n")
            is_return_training_plan(username)
        elif num == 4:
            print("\n★ Let's start training your leg! ★")
            print("Side hop                  : 30 seconds")
            print("Squats                    : 12 times")
            print("Side-lying leg lift left  : 12 times")
            print("Side-lying leg lift right : 12 times")
            print("Backward lunge            : 12 times")
            print("Donkey kicks left         : 15 times")
            print("Donkey kicks right        : 15 times")
            print("Wall calf raises          : 10 times")
            print("Calf stretch left         : 40 seconds")
            print("Calf stretch right        : 40 seconds")
            print("Here's your daily training plan, there are 10 workouts with 12 minutes, feel free to adjust according to your own needs!\n")
            is_return_training_plan(username)
        else:
            print("Invalid choice. Please try again.")

#get initial measurements from user to track the progress
def get_initial_measurements():
  #declares an empty dictionary
  initial_measurements = {}
  print("\n★ Initial Measurements ★")
  #when the user is prompted to enter their initial measurements, inputs are stored as a string in the diff keys of the initial_measurements dictionary
  initial_measurements["weight"] = input("Initial weight (kg): ")
  initial_measurements["chest"] = input("Initial chest measurement (cm): ")
  initial_measurements["waist"] = input("Initial waist measurement (cm): ")
  initial_measurements["thigh"] = input("Initial thigh measurement (cm): ")
  initial_measurements["bicep"] = input("Initial bicep measurement (cm): ")
  #returns the initial_measurements dictionary to allow the calling function to access the user's input and use it
  return initial_measurements

def get_current_measurements(username, initial_measurements):
  #declares an empty dictionary
  current_measurements = {}
  print("\n★ Current Measurements ★")
  current_measurements["weight"] = input("Current weight (kg): ")
  current_measurements["chest"] = input("Current chest measurement (cm): ")
  current_measurements["waist"] = input("Current waist measurement (cm): ")
  current_measurements["thigh"] = input("Current thigh measurement (cm): ")
  current_measurements["bicep"] = input("Current bicep measurement (cm): ")
  #declares an empty dictionary
  progress = {}
  #to show the difference in measurements by minusing current ones with initial ones
  progress["weight"] = float(current_measurements["weight"]) - float(initial_measurements["weight"])
  progress["chest"] = float(current_measurements["chest"]) - float(initial_measurements["chest"])
  progress["waist"] = float(current_measurements["waist"]) - float(initial_measurements["waist"])
  progress["thigh"] = float(current_measurements["thigh"]) - float(initial_measurements["thigh"])
  progress["bicep"] = float(current_measurements["bicep"]) - float(initial_measurements["bicep"])
  #generate the progress report by accessing to the dictionary using specific keys
  print("\n============ Progress ============")
  print(f"Weight (kg) : {progress['weight']}")
  print(f"Chest  (cm) : {progress['chest']}")
  print(f"Waist  (cm) : {progress['waist']}")
  print(f"Thigh  (cm) : {progress['thigh']}")
  print(f"Bicep  (cm) : {progress['bicep']}")
  print("==================================")
  while True:
    is_return = input("\nDo you want to return to the member menu? (y/n) ")
    if is_return == "y":
      member_menu(username)
    elif is_return == "n":
      print("Okay, exiting the program...")
      sys.exit()
    else:
      print("Invalid choice. Please try again.")

#allow user to add reviews on the gym
def add_review(username):
    review = input("Please enter your review of our gym: ")
    with open("gym_reviews.txt", "a") as f:
      f.write(review + "\n")
    print("Thanks for your review!")
    while True:
      add_agn = input("\nDo you want to add another review? (y/n) ")
      if add_agn == "y":
        add_review(username)
      elif add_agn == "n":
          while True:
              is_return = input("\nDo you want to return to the member menu? (y/n) ")
              if is_return == "y":
                member_menu(username)
              elif is_return == "n":
                print("Okay, exiting the program...")
                sys.exit()
              else:
                print("Invalid choice. Please try again.")
      else:
        print("Invalid choice. Please try again.")

#allow admin to view the reviews added by user
def view_reviews():
    with open("gym_reviews.txt", "r") as f:
        reviews = f.readlines()
        if len(reviews) > 0: #check if the txt file contains any reviews at the moment
          print("\n=========================")
          print("Here are all the reviews")
          print("=========================")
          for i, review in enumerate(reviews, 1):
            print(f"{i}. {review}")
        else:
          print("\n ===== No reviews to display =====\n")
        while True:
          is_return = input("Do you want to return to the admin menu? (y/n) ")
          if is_return == "y":
            admin_menu()
          elif is_return == "n":
            print("Okay, exiting the program...")
            sys.exit()
          else:
            print("Invalid choice. Please try again.")

#show the member menu
def member_menu(username):
  print("\nWelcome, member! Please select an option from the menu:")
  print("1. View member details")
  print("2. Book a slot for gym")
  print("3. Coach selection")
  print("4. Show payment details")
  print("5. View training plans")
  print("6. View progress report")
  print("7. Add review of the gym")
  print("8. Return to the main menu")
  while True:
    choice = input("Enter your choice: ")
    if choice == "1":
      name, age, phone, address = show_member_details(username)
      print("\n--- Here's your member details ---")
      print(f"Name: {name}")
      print(f"Age: {age}")
      print(f"Phone: {phone}")
      print(f"Address: {address}")
      while True:
        is_return = input("\nDo you want to return to the member menu? (y/n) ")
        if is_return == "y":
          member_menu(username)
        elif is_return == "n":
          print("Okay, exiting the program...")
          sys.exit()
        else:
          print("Invalid choice. Please try again.")
    elif choice == "2":
      book_slot(username)
    elif choice == "3":
      coach_menu(username)
    elif choice == "4":
      with open ("booking.txt", "r") as f: #read the booking.txt file
        content = f.readlines()
      if not content: #check if the txt file is blank or not, if yes, prompt the user to book a slot
        while True:
          ask_booking = input("You haven't booked any slot yet. Do you want to book a slot now? (y/n) ")
          if ask_booking == "y":
            book_slot(username)
          elif ask_booking == "n":
            print("Okay, returning to the member menu...")
            member_menu(username)
          else:
            print("\nInvalid selection. Please try again.")
      else:
        show_payment_details(username)
    elif choice == "5":
      training_plan(username)
    elif choice == "6":
      starting_measurements = get_initial_measurements()
      get_current_measurements(username, starting_measurements)
    elif choice == "7":
      add_review(username)
    elif choice == "8":
      main_menu()
    else:
      print("\nInvalid choice. Please try again.")

#allow admin to edit booking slots
def edit_slot_action():
  while True:
    command = input("Enter a command (add/remove): ")
    if command == "add":
        time_slot = input("Enter the time slot you want to add (ie 18:00-19:00): ")
        available_slots.append(time_slot) #append the specific time slot to the list available_slots
        print("Time slot added successfully!")
        while True:
          edit_agn = input("Do you want to edit another slot? (y/n) ")
          if edit_agn == "y":
            available_edit_slot()
          elif edit_agn == "n":
            while True:
              is_return = input("Do you want to return to the admin menu? (y/n) ")
              if is_return == "y":
                admin_menu()
              elif is_return == "n":
                print("Okay, exiting the program...")
                sys.exit()
              else:
                print("Invalid choice. Please try again.")
          else:
            print("Invalid choice. Please try again.")
    elif command == "remove":
      while True:
        time_slot = input("Enter any available time slot you want to remove (ie 13:00-14:00): ")
        if time_slot in available_slots:
          available_slots.remove(time_slot) #remove the selected slot in the available_slots list
          print("Time slot removed successfully!")
          while True:
            edit_agn = input("Do you want to edit another slot? (y/n) ")
            if edit_agn == "y":
              available_edit_slot()
            elif edit_agn == "n":
              while True:
                is_return = input("Do you want to return to the admin menu? (y/n) ")
                if is_return == "y":
                  admin_menu()
                elif is_return == "n":
                  print("Okay, exiting the program...")
                  sys.exit()
                else:
                  print("Invalid choice. Please try again.")
            else:
              print("Invalid choice. Please try again.")
        else:
            print("Time slot not found.")
    else:
        print("\nInvalid input! Please try again.")

#show the available slots for editing purpose
def available_edit_slot():
  print("\n--- Available slots ---")
  for i, slot in enumerate(available_slots):
    print(f"{i+1}. Slot {slot}")
  edit_slot_action()

#show all registered member details to admin
#will show more lines if multiple users have registered
def show_all_member_details(): 
  print("\n--- All members' details ---")
  print("*You will see more members' details if you register multiple times*")
  with open("user_details.txt", "r") as f:
    for line in f:
      name, age, phone, address = line.strip().split(", ")
      print(f"{name}\n{age}\n{phone}\n{address}\n")  

#show all registered member details to admin
def member_details_admin():
  with open ("user_details.txt", "r") as f:
    content = f.readlines()
  if not content:
    while True:
      ask_registration = input("No one has registered as a new member. Do you want to register now? (y/n) ")
      if ask_registration == "y":
        sign_up()
      elif ask_registration == "n":
        print("Okay, returning to the admin menu")
        admin_menu()
      else:
        print("\nInvalid input. Please try again.")
  else:
    show_all_member_details()
    while True:
      is_return = input("Do you want to return to the admin menu? (y/n) ")
      if is_return == "y":
        admin_menu()
      elif is_return == "n":
        print("Okay, exiting the program...")
        sys.exit()
      else:
        print("\nInvalid selection. Please try again.")

#allow admin to edit the existing promocode
def edit_promocode_action():
  while True:
    command = input("\nEnter a command (add/remove): ")
    if command == "add":
      while True:
        discount_type = input("Which discount type do you want to add (1/2): ") #choose which type of promocode you want to edit, either from promocode1 or promocode2 list
        if discount_type == "1":
          promocode = input("Enter the promocode you want to add (ie gym0111): ")
          promocode1.append(promocode) #append the new promocode to the selected discount type's list
          print("Promocode added successfully!")
          while True:
            is_return = input("Do you want to return to the admin menu? (y/n) ")
            if is_return == "y":
              admin_menu()
            elif is_return == "n":
              print("Okay, exiting the program...")
              sys.exit()
            else:
              print("\nInvalid selection. Please try again.")
        elif discount_type == "2":
          promocode = input("Enter the promocode you want to add (ie gym0111): ")
          promocode2.append(promocode) #append the new promocode to the selected discount type's list
          print("Promocode added successfully!")
          while True:
            is_return = input("Do you want to return to the admin menu? (y/n) ")
            if is_return == "y":
              admin_menu()
            elif is_return == "n":
              print("Okay, exiting the program...")
              sys.exit()
            else:
              print("\nInvalid selection. Please try again.")
        else:
          print("\nPromocode not found.")
    elif command == "remove":
      while True:
        discount_type = input("Which discount type do you want to remove (1/2): ")
        if discount_type == "1":
          while True:
            promocode = input("Enter the promocode you want to remove (type out the code): ")
            if promocode in promocode1:
              promocode1.remove(promocode) #remove the selected promocode to the selected discount type's list
              print("Promocode removed successfully!")
              while True:
                is_return = input("Do you want to return to the admin menu? (y/n) ")
                if is_return == "y":
                  admin_menu()
                elif is_return == "n":
                  print("Okay, exiting the program...")
                  sys.exit()
                else:
                  print("Invalid choice. Please try again.")
            else:
              print("Promocode not in discount type 1, please try again.")
        elif discount_type == "2":
          while True:
            promocode = input("Enter the promocode you want to remove (type out the code): ")
            if promocode in promocode2:
              promocode2.remove(promocode) #remove the selected promocode to the selected discount type's list
              print("Promocode removed successfully!")
              while True:
                is_return = input("Do you want to return to the admin menu? (y/n) ") #check if admin wants to return to the admin menu
                if is_return == "y":
                  admin_menu()
                elif is_return == "n":
                  print("Okay, exiting the program...")
                  sys.exit()
                else:
                  print("\nInvalid choice. Please try again.")
            else:
              print("Promocode not in discount type 2, please try again.")
        else:
            print("\nPromocode not found.")
    else:
        print("Invalid input! Please try again.")

#show available promocode for editing purpose
def edit_promocode():
  print("\n--- Available promocode for dicount type 1 ---")
  for i, promocode in enumerate(promocode1):
    print(f"{i+1}. Code {promocode}")
  print("\n--- Available promocode for dicount type 2 ---")
  for i, promocode in enumerate(promocode2):
    print(f"{i+1}. Code {promocode}")
  edit_promocode_action()

#show admin menu
def admin_menu():
  print("\nWelcome, admin! Please select an option from the menu:")
  print("1. View all member details")
  print("2. Edit booking slot")
  print("3. Edit promotion code")
  print("4. Edit prices for each specialization")
  print("5. View members' reviews of the gym")
  print("6. Return to the main menu")

  while True:
    choice = input("Enter your choice: ")
    if choice == "1":
      member_details_admin()
    elif choice == "2":
      available_edit_slot()
    elif choice == "3":
      edit_promocode()
    elif choice == "4":
      edit_prices()
    elif choice == "5":
      view_reviews()
    elif choice == "6":
      main_menu()
    else:
      print("Invalid choice. Please try again.")

#allow member to log in according to the credentials they've set upon signing up
def log_in_member():
  print("\n--- Enter the username and password you've set just now ---")
  while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if check_credentials(username, password):
      member_menu(username)
    else:
      print("Invalid username or password. Please try again.")

#allow admin to log in
def log_in_admin():
  print("\n--- Log in as an admin ---")
  input("Enter your username: ")
  input("Enter your password: ")
  admin_menu()

#call the main function to start the program
main_menu()