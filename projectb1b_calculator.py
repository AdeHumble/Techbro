# -*- coding: utf-8 -*-
"""
Created on Sun May  7 13:09:27 2023

@author: msunmola
"""
"""
Areas i wish to improve on this program
    1. Include other mathematical operations like performing trigonometry functions
    2. GUI enabled
"""
#variables initialisation
x=int()
y=int()
answ=1

#dashboard
print("\nGROUP A CALCULATOR SOFTWARE")
user_name=input("\nWelcome user. How can i address you? ")
print(user_name.title(),"It's nice having you here\n\nKindly adhere to the set of instructions below to enable me assist you well")
print("1: ||Press '1' if you would like to perform addition")
print("2: ||Press '2' if you would like to perform subtraction")
print("3: ||Press '3' if you would like to perform division")
print("4: ||Press '4' if you would like to perform multiplication")
print("5: ||Press '5' if you would like to perform square root")
print("6: ||Press '6' if you would like to perform squares")

#function statements for each operation
def addition():
    while True:
        try:
            num=int(input("How many numbers do you want to add? "))
        except ValueError:
            print("\nI expects a number. Try again!")
            continue
        num_list1=[]
        for i in range(num):
            while True:
                try:
                    n=int(input("Enter numbers: "))
                except ValueError:
                    print("\nI expects a number. Try again!")
                    continue
                    
                num_list1.append(n)
                break
            
        print("The sum of the",num,"numbers is: ", sum(num_list1))
        break
        
def subtraction(x,y):
    while True:
        try:
            x=int(input("Enter the first number you wish to subtract: "))
            y=int(input("Enter the second number you wish to subtract: "))
        except ValueError:
            print("\nI expects a number. Try again!")
            continue
        ans=x-y
        print(x,"-",y,"=",ans)
        break

def division(x,y):
    while True:
        try:
            x=int(input("Enter the first number: "))
            y=int(input("Enter the second number: "))
        except ValueError:
            print("\nI expects a number. Try again!")
            continue
        ans=x/y
        print(x,"/",y,"=",ans)
        break

def multiply(x,y):
    while True:
        try:
            num=int(input("How many numbers do you want to multiply? "))
        except ValueError:
            print("\nI expects a number. Try again!")
            continue
        
        num_list2=[]
        for i in range(num):
            while True:
                try:
                    n=int(input("Enter numbers: "))
                except ValueError:
                    print("\nI expects a number. Try again!")
                    continue
                    
                num_list2.append(n)
                break
        ans=answ 
        for i in range(len(num_list2)):
            ans=ans*num_list2[i]    
            
        print("The product of the",num,"numbers is: ", ans)
        break
    
def sqr_root(x):
    while True:
        try:
           x=int(input("Enter the number you wish to find its square root: "))
        except ValueError:
            print("\nI expects a number. Try again!")
            continue
        ans=x**0.5
        print("The square root of ",x,"=", ans)
        break
     
def square(x):
    while True:
        try:
           x=int(input("Enter the number you wish to find its square: "))
        except ValueError:
            print("\nI expects a number. Try again!")
            continue
        ans=x**2
        print("The square of ",x,"=", ans)
        break
    
#ask the user which calculation he/she will like to do
while True:
    try:
        user_choicea=int(input("\nWhat would you like to do: "))
    except ValueError:
        print("That was a wrong input. You must enter a number\nPlease refer to the instructions above")
        continue

#test each of the user's input against the predetermined operations    
    if user_choicea==1:
        addition()
        user_choiceb=input("\nWould you like to perform another operation?\nAdvise me with your choice with a YES/NO: ")
        if user_choiceb.upper()=="YES":
            continue
        elif user_choiceb.upper()!="NO" and user_choiceb.upper()!="YES":
            print("You have supplied a wrong input.\nPlease, enter YES or NO")
            continue
        else:
            print("Okay then! Goodbye", user_name)
            break
            
    elif user_choicea==2:
        subtraction(x,y)
        user_choiceb=input("\nWould you like to perform another operation?\nAdvise me with your choice with a YES/NO: ")
        if user_choiceb.upper()=="YES":
            continue
        elif user_choiceb.upper()!="NO" and user_choiceb.upper()!="YES":
            print("You have supplied a wrong input.\nPlease, enter YES or NO")
            continue
        else:
            print("Okay then! Goodbye", user_name)
            break
        
    elif user_choicea==3:
        division(x, y)
        user_choiceb=input("\nWould you like to perform another operation?\nAdvise me with your choice with a YES/NO: ")
        if user_choiceb.upper()=="YES":
            continue
        elif user_choiceb.upper()!="NO" and user_choiceb.upper()!="YES":
            print("You have supplied a wrong input.\nPlease, enter YES or NO")
            continue
        else:
            print("Okay then! Goodbye", user_name)
            break
        
    elif user_choicea==4:
        multiply(x, y)
        user_choiceb=input("\nWould you like to perform another operation?\nAdvise me with your choice with a YES/NO: ")
        if user_choiceb.upper()=="YES":
            continue
        elif user_choiceb.upper()!="NO" and user_choiceb.upper()!="YES":
            print("You have supplied a wrong input.\nPlease, enter YES or NO")
            continue
        else:
            print("Okay then! Goodbye", user_name)
            break
        
    elif user_choicea==5:
        sqr_root(x)
        user_choiceb=input("\nWould you like to perform another operation?\nAdvise me with your choice with a YES/NO: ")
        if user_choiceb.upper()=="YES":
            continue
        elif user_choiceb.upper()!="NO" and user_choiceb.upper()!="YES":
            print("You have supplied a wrong input.\nPlease, enter YES or NO")
            continue
        else:
            print("Okay then! Goodbye", user_name)
            break
        
    elif user_choicea==6:
        square(x)
        user_choiceb=input("\nWould you like to perform another operation?\nAdvise me with your choice with a YES/NO: ")
        if user_choiceb.upper()=="YES":
            continue
        elif user_choiceb.upper()!="NO" and user_choiceb.upper()!="YES":
            print("You have supplied a wrong input.\nPlease, enter YES or NO")
            continue
        else:
            print("Okay then! Goodbye", user_name)
            break
        
    else:
        print("Sorry, I don't understand this command")
        user_choiceb=input("\nWould you like to try again?\nAdvise me with your choice with a YES/NO: ")
        if user_choiceb.upper()=="YES":
            continue
        elif user_choiceb.upper()!="NO" and user_choiceb.upper()!="YES":
            print("You have supplied a wrong input.\nPlease, enter YES or NO")
            continue
        else:
            print("Okay then! Goodbye", user_name)
            break
        


