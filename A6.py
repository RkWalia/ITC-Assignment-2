#Ques6

a=int(input("Enter first length: "))
b=int(input("Enter second length: "))
c=int(input("Enter third length: "))

if (a+b)<c or (a+c)<b or (b+c)<a:
    print("No")
else:
    print("Yes")
