import random
'''
1 for snake
0 for gun
-1 for water
'''
print("For snake enter 's'\nFor gun enter 'g'\nFor water enter 'w'")
computer = random.choice([1,0,-1])
youstr = input("Enter your choice:")
you_dict= {"s":1,"g":0,"w":-1}
reverse_dict ={1:"snake",0:"gun",-1:"water"}

you = you_dict[youstr]

print(f"You choose {reverse_dict[you]}")
print (f"Computer choose {reverse_dict[computer]}")

if(computer == you):
    print("IT'S A DRAW!!!\nYou both choose the same")
else:
    if(computer == 1 and you == 0):
        print("YOU WON!!!")
    elif(computer == 1 and you == -1):
        print("YOU LOST!!!")
    elif(computer == -1 and you == 1):
        print("YOU WON!!!")
    elif(computer == -1 and you == 0):
        print("YOU LOST!!!")
    elif(computer == 0 and you == 1):
        print("YOU LOST!!!")
    elif(computer == 0 and you == -1):
        print("YOU WON!!!")
    else:
        print("something went wrong:")

