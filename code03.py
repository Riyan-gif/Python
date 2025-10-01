# Q-1. Python program to check if the given number is Happy Number
# A number is said to be happy if it yields 1 when replaced by the sum of squares of its digits repeatedly.
# If this process results in an endless cycle of numbers containing 4, then the number will be an unhappy
# number.
# Let's understand by an example:
# Number = 32
# 3^2 + 2^2=13
#  1^2 + 3^2 = 10
#  1^2 + 0^0= 1 happy number

a= int(input("Enter number: "))
while a!=1 and a!=4:
  sum=0
  while a!=0:
    r=a%10
    sum+=r**2
    a=a//10
  a=sum
if a==1:
  print("Happy number")
else:
  print("Unhappy number")      
  
# ---------------------------------------------------------------------------------------------

#  Q=2 print all possiable number user enter and check a^2+b^2=c^2
limit= int(input("Enter number: "))
for i in range(1,limit+1):
  for j in range(i,limit+1):
    for k in range(j,limit+1):
      if(i**2 + j**2)==k**2:
        print(i,j,k)

# ---------------------------------------------------------------------------------------------

import math
math.factorial(10)
n=int(input("Enter no: "))
for i in range(n):
  for j in range(n-1):
    print(" ",end="")
  val=1
  print(val,end=" ")
  for k in range(a,i+1):
    val=val*(1-k+1)//k
    print(val,end=" ")
  print()      

