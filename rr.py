import random
import time
import os
os.system("cls")
# defining variables and functions
x = 1
shoot = input("41 72 65 20 79 6f 75 20 67 6f 69 6e 67 20 74 6f 20 73 68 6f 6f 74 3f 20 54 79 70 65 20 27 79 27 20 66 6f 72 20 59 65 73 2c 20 54 79 70 65 20 61 6e 79 74 68 69 6e 67 20 65 6c 73 65 20 66 6f 72 20 6e 6f 20 ")
# code
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
        print("  v 59 41 59 21 21 21 20 49 20 44 49 44 4e 54 20 44 49 45 21 21 21")
        print("> O<-<")
        time.sleep(1)
        exit()
else:
    exit()
