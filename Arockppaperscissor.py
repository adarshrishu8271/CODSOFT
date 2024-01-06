#stone paper sessisor game

import random
print ("welcome to rock ,paper , sessisor game")
print("\n")
print ("for\" ROCK \" press1")
print ("for \"SESSISOR \"press 2")
print ("for \" PAPER \" press 3")

print("\n")
inp=int(input ("enter code in game by user="))
sys=random.randint(1,3)
print ("system input=",sys)
print ("\n")

if inp==sys:
   print (" game is tie")
elif (inp ==True and sys==2) or(inp==2 and sys ==3) or(inp==3 and sys==1):
    print (" user won the game")
    if sys==2 and inp==1:
        print ("rock beat sessisor")
    elif sys==3 and inp==2:
        print ("sessisor win over paper")
     
    elif sys==1 and inp==3:
        print (" paper beat rock ")
elif  (inp==3 and sys==2) or(inp==2 and sys==1):
    print ("computer won the game")
    if sys==1 and inp==2:
        print ("rock beat sessisor ")
        
    elif sys==2 and inp==3:
        print ("sessisor beat paper")
        
    elif sys==3 and inp==1:
        print ("paper beat rock")
        
    elif sys==1 and inp==3:
        print(" paper beat rock")