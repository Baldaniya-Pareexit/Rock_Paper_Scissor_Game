import random

item_list = ["Rock","Paper","Scissor"]

user_choice = input("Enter your move = 'Rock','Paper','Scissor' : ")
comp_choice = random.choice(item_list)

print(f"User_choice = {user_choice}")
print(f"Computer_choice = {comp_choice}")

if user_choice == comp_choice:
    print("Result = Both choices are same : Match Tie")
    
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Result = Paper covers Rock : Computer win")
    else:
        print("Result = Rock smashes Scissor : You win")
        
elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("Result = Paper covers Rock : You win")
    else:
        print("Result = Scissor cuts Paper : Computer win")
        
elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Result = Rock smashes Scissor : Computer win")
    else:
        print("Result = Scissor cuts Paper : You win")