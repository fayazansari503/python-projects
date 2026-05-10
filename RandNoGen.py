import random

target = random.randint(1, 10)

"""while True:
    userChoice = input("Guess the target or Quit : ")
    if(userChoice == "Quit"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Gueass!!")
        break
    elif(userChoice < target):
        print("Your no. was to small. Take a bigger Guess..")
    else:
        print("Your no. was too big. Take a smaller guess")

print("____GAME OVER ____")"""   


com = random.randint(1, 20)
hum = int(input("ENTER NO. BETWEEN 1 TO 20 : "))
attemp = 1
while com != hum:
    if hum > com:
        hum = int(input("Your no. was too big. Take a smaller Guess : "))
    elif hum < com:
        hum = int(input("Your no. was too small. Take a begger Guess : "))
    attemp += 1  
print("Correct Guess",attemp,"attemp")      
