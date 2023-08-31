import time
import sys
def portal():
    print(" 1. Student \n 2. exit the system")
    time.sleep(2)
    decision = input(">>> ")
    if decision == "1":
        from operation import std
        std()
    elif decision == "2":
        sys.exit()
    else:
        print("You seems to have entered wrong code, Retry!")
        portal()
portal()
