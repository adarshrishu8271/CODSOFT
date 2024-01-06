#password generator using python 

import random
letter=['a','b','c','d','e','f','g','h','i','j'
,'k','l','m','n','o','p','q']
num=['0','1','2','3','4','5','6','7','8','9']
sym=['§','¢','#','√','£','"','π','&','∆']
print (" PASSWORD GENERATOR ")
print ("\n")
n1=int(input("letter required="))
n2=int(input ("number required="))
n3=int(input ("symbol required="))
print ("\n\n")
password=" "
for s in range (1,n1+1):
    wo=random.choice(letter)
    password+=wo
for s in range(1,n2+1):
    wo=random .choice(num)
    password +=wo
for s in range (1,n3+1):
    wo=random . choice (sym)
    password+=wo
    
    print (password)