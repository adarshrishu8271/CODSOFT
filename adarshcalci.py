# simple calculator using "PYTHON"
# using concept of "IF ,ELIF"


print("for addition press \" 1\"\n")
print("for substraction press \" 2\" \n ")
print ("for multiplication press \"3\" \n")
print("for division press \"4 \"\n\n")
#operation code
num1=float(input("first number = "))
print ("\n")

num2=float(input("second number= "))
print("\n")
x=int(input(" enter code for specific operation="))
print("\n\n")
if x==1:
  print  ("\t addition")
  print ("\n")
  sum=num1+num2
 
  print ("addition result=",sum)
  
elif  x==2:
    print ("\t substraction")
    print ("\n")
    sub=num1- num2
    
    print ("substraction result =",sub)
    
elif x==3:
    print ("\t multiplication")
    print ("\n")
    mul=num1*num2
    print (" \t product result=",mul)

elif x==4:
    print ("\t division ")
    print ("\n")
    div=num1/num2
    print ("\t division result=",div)

else:
    print("invalid  code for operation ")