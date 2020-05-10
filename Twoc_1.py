''' 1st question'''
Name=input("Enter your name\n")
Branch=input("Enter your branch\n")
Gender=input("Enter your Gender\n")
College=input("Enter your College\n")
Age=input("Enter your Age\n")
print("My name is",Name,"\n""My age is",Age,"\nI am a student of",College)

'''2nd question'''
import numpy as np
def square_root(num):
    a=np.sqrt(num)
    return a
num=int(input("enter the no\n"))
print("\nsquare root of",num," is:",square_root(num))

'''3rd question'''
a=int(input("enter 1st no\n"))
b=int(input("enter 2nd no\n"))
a=a+b
b=a-b
a=a-b
print("first no is ",a)
print("\nsecond no is ",b)

'''4th question'''
cp=int(input("enter cost price"))
sp=int(input("enter selling price"))
profit=sp-cp
print("Profit is:",profit)
profit_new=(profit + (5/100)*profit)
new_sp=cp +profit_new
print("New selling price of product after 5% increase in profit is:",new_sp)

'''5th question'''
run_a=int(input("runs scored by player 1 on 60 balls"))
run_b=int(input("runs scored by player 2 on 60 balls"))
run_c=int(input("runs scored by player 2 on 60 balls"))

print("strike rate of player 1 is",(run_a/60)*100)
print("strike rate of player 2 is",(run_b/60)*100)
print("strike rate of player 3 is",(run_c/60)*100)

print("runs scored after playing 60 more balls by player 1 is",2*run_a)
print("runs scored after playing 60 more balls by player 2 is",2*run_b)
print("runs scored after playing 60 more balls by player 3 is",2*run_c)

print("maximum sixes hit by player 1",int(run_a/6))
print("maximum sixes hit by player 2",int(run_b/6))
print("maximum sixes hit by player 3",int(run_b/6))

