import random
"""
0 for rock
1 for paper
2 for scissors
"""
#use if-else
"""computer = random.randint(0, 2)
user_choice = input("Enter your choice : ")
dict = {"r": 0, "p": 1, "s": 2}
you = dict[user_choice]

if(computer == you):
    print("Draw")
else:
    if(computer == 0 and you == 1):
        print("You Win!")
    elif(computer == 0 and you == 2):
       print("You Loss!")
    elif(computer == 1 and you == 0):
       print("You Loss!")
    elif(computer == 1 and you == 2):
       print("You Win!")
    elif(computer == 2 and you == 0):
       print("You Win")
    elif(computer == 2 and you == 1):
      print("You Loss!")
    else:
      print("Somethig went wrong") """


#use loop
choices = ["rock", "paper", "scissors"] 
user_score = 0
computer_score = 0
while True:
    computer = random.choice(choices)

    user = input("Enter your choice : ").lower()
    if user not in choices:
        print("Invalid choice Try Again...")
        continue
    if(computer == user):
        print("Tie!")
    elif((user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper")):
            print("You Win!") 
            user_score += 1 
    else:
        print("Computer Win!")
        computer_score += 1
