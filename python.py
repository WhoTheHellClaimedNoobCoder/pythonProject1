import math
import random
import time

def main():
    sqrt = input("Do you want to test the square root of a number?\n")
    if sqrt == "yes":
        num = int(input("Enter a number: \n"))
        print(math.sqrt(num))
    elif sqrt == "no":
        round = input("Do want to round a number?\n")
        if round == "yes":
         try: 
            num = float(input("Enter a number: \n"))
            print(math.floor(num))
         except ValueError:
            print("Invalid input (You have to enter a number instead of a string!)")
        elif round == "no":
            countDown = input("Do you want to count down\n")
            if countDown == "yes":
                try:
                    amountNum = int(input("Enter the amount you want to count down from: \n"))
                    for i in range(amountNum, 0, -1):
                        print(i)
                        time.sleep(1)
                except ValueError:
                    print("Invalid input (You have to enter a number instead of a string!)")
    else:
        print("Invalid input")

main()