# """
# Assignment

# Write a simple python program that will ask user to login, after login, user
# should be able to choose operation to perform.
# If user decides to do calculations, open calculation for the user,
# if it is set, open sets
# if it is cbt, open cbt for the user.
# NOTE: 
# User's username should be in database before they can login;
# User's username must match with the password to login,
# User should be able to perform Addition, Subtraction, Multiplication and Division operations under Calculation
# User should be able to do cbt under cbt operation
# User should be able to supply sets and perform all sets operation under sets.
# FURTHER:
# When user is done with any operation, user should be able to perform another operation
# user can also decides to logout
# """
#                                          SOLUTION

import sys
import time
import re
import mysql.connector as connection
myconn = connection.connect(host = "127.0.0.1", user = " ", passwd = " ", database = "projects")
cursor = myconn.cursor()

def std():
    acct = input("""
    1. Log in
    2. Create account
    """)
    if acct == "1":
        log_in()
    elif acct == "2":
        create()

def create():
    userinfo = []
    details = ("First_name", "Middle_name", "Last_name", "Email", "Gender", "Level", "Course", "Pswd")
    querry = "INSERT INTO std (First_name, Middle_name, Last_name, Email, Gender, Level, Course, Pswd) VALUES (%s,%s, %s, %s, %s, %s, %s, %s)"
    for i in range (8):
        decision = input(f"Enter your {details[i]}: ")
        userinfo.append(decision)
        time.sleep(1)
    val = (userinfo)
    cursor.execute(querry, val)
    myconn.commit()
    time.sleep(2)
    print(f"Registration successful.")
    time.sleep(1)
    log_in()

def checkpassword():
    global password
    print(f"Enter your password")
    password = input(">>> ")
    if password == password:
        return
    else:
        print(f"Invalid password! Try Again")
        checkpassword()

def checkEmail():
    global email
    email = input("Enter your email ")
    check_email = re.findall(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", email)
    if not check_email:
        print("Invalid email. Try again")
        time.sleep(1)
        checkEmail()  
    else:
        return



def log_in():
    global password
    global username
    username = input("enter your email: ")
    time.sleep(2)
    password = input("enter your password: ")
    val = (username, password)
    querry = "select * from std where Email = %s and Pswd = %s"
    cursor.execute(querry, val)
    result = cursor.fetchone()
    if result:
        time.sleep(2)
        print("you have successfully log in ")
        time.sleep(2)
        decide = input("Hello student! Enter 1 to perform the operation and 2 to go quit: ")
        if decide == "1":
            operation()
        elif decide == "2":
            sys.exit()
    else:
        print("invalid input, try to log in again ")
        log_in()

def operation():
    print("""
    These are the operations you can perform:
    1. CBT
    2. CALCULATIONS
    3. SET
    4. LOGOUT
    5. CLOSE APPLICATION
    """)
    task = input("Enter a number to perform operation: ")
    if task == "1":
        exam()
    elif task == "2":
        calculations()
    elif task == "3":
        set_operation()
    elif task == "4":
        time.sleep(2)
        log_in()
    elif task == "5":
        time.sleep(2)
        sys.exit()

    else:
        print("Invalid input")
        time.sleep(2)
        operation()

def exam():
    global score 
    score = 0
    nt = 0
    questions = ["1. which of the following is not a programming language?", "2. SQI is which type of school?", "3. Who is the BTS leader?",
                 "4. Nigeria tribe is classified into ____", "5. ____ is a python in built function?", "6. if 'Ade' is string, what is 10j and 20 ?",
                 "7. Python is a ____ language?", "8.Nigeria is in ____?", "9. ___ and ___ is an example  of datatype",
                 "10. If photoshop is for Graphic design, Python is  for ____ department?"]
    options = ["a. Javascript \n b. Graphic \n c. Python", "a. Business School \n b. Coding School \n c. Fashion School",
               "a. Kim Namjoon \n b. Kim Taehyung \n c. Jeon Jungkook", "a. 4 \n b. 2 \n c. 3",
               "a. out() \n b. basic() \n c. input()", "a. complex & integer \n b. float & integer \n c. integer & complex",
               "a. progamming language \n b. design language \n c. second language", "a. United State \n b. Africa \n c. Norther Ireland", 
               "a. string and float \n b. data and float \n c. input and print", "a. UI/UX \n b. Javascript \n c. Data Science"]
    answer = ["b", "b", "a", "c", "c", "a", "a", "b", "a", "c"]
    for que in questions:
        print(que)
        time.sleep(2)
        print(options[nt])
        time.sleep(1)
        ans = input("input your answer >>> ")
        an = answer[nt].lower()
        if ans == an:
            print("Correct")
            score +=10
        else:
            print("You are wrong")
            score -= 5
        nt +=1
    print("Your total Score is " + str(score))
    print("Enter 1 to perform another operation..\n Enter 2 to logout..\n Enter 3 to exit..")
    another = input(">>> ")
    if another == "1":
        operation()
    elif another == "2":
        log_in()
    elif another == "3":
        sys.exit()
def calculations():
    print("Which calculation will you like to perform?")
    time.sleep(1)
    decide = input("1. Addition \n 2. Subtraction \n 3. Mulitiplication \n 4. Division \n >>>  ")

    if decide == "1":
            print("Addition calculation")
            time.sleep(1)
            val = float(input("enter your first number: "))
            val2 = float(input("enter your second number: "))
            value = val + val2
            print(f"Your score is {value}")
    elif decide == "2":
        print("Subtraction calculation")
        time.sleep(1)
        val = float(input("enter your first number: "))
        val2 = float(input("enter your second number: "))
        value = val - val2
        print(f"Your score is {value}")
    elif decide == "3":
        print("Multiplication calculation")
        time.sleep(1)
        val = float(input("enter your first number: "))
        val2 = float(input("enter your second number: "))
        value = val * val2
        print(f"Your score is {value}")
    elif decide == "4":
        print("Division calculation")
        time.sleep(1)
        val = float(input("enter your first number: "))
        val2 = float(input("enter your second number: "))
        value = val / val2
        print(f"Your score is {value}")
    else:
        print("invalid input")
        time.sleep(2)
        calculations()
    print("Enter 1 to perform another operation..\n Enter 2 to logout..\n Enter 3 to exit..")
    another = input(">>> ")
    if another == "1":
        operation()
    elif another == "2":
        log_in()
    elif another == "3":
        sys.exit()
def set_operation():
    print("This is for set operation")
    time.sleep(1)
    print("Registered python student: Junaid, Popson")
    python_students =  {'Junaid', 'Popson'} 
    ans = input("Enter your name to be added to the list of registered Python Students name: ")
    python_students.add(ans)        # add is used to update a set
    print( python_students)         # a set output
    time.sleep(1)
    print("The name aboved is the new list of the registered python students")
    # decide = input("Hello student! Enter 1 to attempt exam and 2 to go quit: ")
    # if decide == "1":
    #     from question import select
    #     select()
    # elif decide == "2":
    #     sys.exit()
  
