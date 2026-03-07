import random 
choice = ("r", "p", "s")
user_s = 0
comp_s = 0
while True:
    user_ch = input("Rock, Paper, Scissor? (r/p/s):")
    comp_ch = random.choice(choice)
    if comp_ch == user_ch:
        print(f"You choose {user_ch}")
        print(f"Computer choose {comp_ch}")
        print(f"Its a draw")
    
    elif user_ch == "p" and comp_ch == "r" or user_ch == "s" and comp_ch == "p" or user_ch == "r" and comp_ch == "s":
        print(f"You choose {user_ch}")
        print(f"Computer choose {comp_ch}")
        print(f"You Win")
        user_s+=1

    elif user_ch == "r" and comp_ch == "p" or user_ch == "p" and comp_ch == "s" or user_ch == "s" and comp_ch == "r":
        print(f"You choose {user_ch}")
        print(f"Computer choose {comp_ch}")
        print(f"You Lose")
        comp_s+=1    

    elif user_ch not in choice :
        print("Invalid input. Please enter a valid input")
               
    print(f"your score: {user_s}")
    print(f"Comp score: {comp_s}")