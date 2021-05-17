import random
import time
import os
def clear():
    try:
        os.system("cls")
    except:
        os.system("clear")
# defining variables and functions
while True:
    x = 1
    shoot = input("Are you going to shoot? Type 'y' for Yes, Type anything else for no ")
    # code
    clear()
    x = random.randint(1,6)
    if shoot == "y":
        print(x)
        if x == 6:
            os.system("cls")
            print(">O<-<")
            time.sleep(1)
            os.system("cls")
            print("> O/-<")
            time.sleep(1)
            exit()   
        else:
            os.system("cls")
            print(">O<-<")
            time.sleep(1)
            os.system("cls")
            print("  v YAY!!! I DIDNT DIE!!!")
            print("> O<-<")
            time.sleep(1)
            #exit()
    #else:
     #   exit()
