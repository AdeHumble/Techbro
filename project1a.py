#variables initialisation
quiz={"Planet":"Saturn","Dodecahedron":12,"Greek_alpha":"Delta","Company_name":"Cadabra","minutes":10080}
score=0

#accepts the user name
#print()
user_name=input("\nHello dear!, How should I address you? ")

#ask for the user choice. If he/she would like to play a quiz or not
print("\nIt's nice meeting you", user_name.title())
interest=input("\nWould you like to play a quiz?\n\nPlease let me know with a YES or NO: ")
if interest.upper()=="YES":

    #this block of codes evaluates user gives the user 3 quizes, evaluates their correctness and assigns points
    ans1=input("\nQUESTION 1\nWhich planet has the most moons?  ")
    if ans1.title()==quiz["Planet"]:
        print("You are a Genius! You just earned 5 points\n")
        score=score+5
    else:
        print("Oh, sorry! You missed that\n")
        score+=0
    
    while True:
        try:
            ans2=int(input("\nQUESTION 2\nHow many faces does a Dodecahedron have?  "))
        except ValueError:
            print("That was a wrong input. You must enter a number")
            continue
    
        if ans2==quiz["Dodecahedron"]:
            print("You are a Genius! You just earned 5 points\n")
            score+=5
            #break
        else:
            print("Oh, sorry! You missed that\n")
            break
    
    ans3=input("\nQUESTION 3\nWhat is the 4th letter of the Greek alphabet?  ")
    if ans3.title()==quiz["Greek_alpha"]:
        print("You are a Genius! You just earned 5 points\n")
        score+=5
    else:
        print("Oh, sorry! You missed that\n")
    
    
    print(user_name.title(),",Your total score for this quiz is: ",(score/15)*100,"%","points")
    
elif interest.upper()=="NO":
    print("\nOkay, Good bye then!\nMeet you some other time\n")
    
else:
    print("You have supplied a wrong input",user_name,"\nPlease make sure to enter YES or NO\nPlease, try again!")