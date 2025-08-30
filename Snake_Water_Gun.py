import random

'''''
-1 = Snake
1 = Water
0 = Gun
'''''

Computer = random.choice ([1, -1, 0])
Youstr = input("Enter your choice : ")
YouDict = {"s": -1, "w": 1, "g": 0}
reverseDict = {-1 : "Snake", 1 : "Water", 0 : "Gun"}

You = YouDict[Youstr]

print(f"You choose {reverseDict[You]} \n Computer choose {reverseDict[Computer]}")

if (Computer == You):
    print("Its a draw")

else:
    if (Computer == -1 and You == 1):
        print("You loose!")
    
    elif (Computer == -1 and You == 0):
        print("You win!")

    elif (Computer == 1 and You == -1):
        print("You win!")

    elif (Computer == 1 and You == 0):
        print("You loose!")

    elif (Computer == 0 and You == -1):
        print("You loose!")

    elif (Computer == 0 and You == 1):
        print("You win!")

    else :
        print("Something went wrong!") 






