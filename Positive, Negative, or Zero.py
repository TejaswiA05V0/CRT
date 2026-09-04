#Write a Python program that takes one integer as input and checks whether the number is:
#Positive if the number is greater than 0
#Negative if the number is less than 0
#Zero if the number is equal to 0
#SOLUTION:
n=int(input())
if(n<0):
    print("Negative")
elif n==0:
    print("Zero")
else:
    print("Positive")
