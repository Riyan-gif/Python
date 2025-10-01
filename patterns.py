a= int(input("Enter number: "))

for i in range(a):
  for j in range(i+1):
    print("*", end=" ")
  print()

# ------------------------------------------------------------------------------------------------------

for i in range(a):
  for j in range(a-i):
    print("*",end=" ")
  print()  

# ------------------------------------------------------------------------------------------------------

for i in range(a):
  for j in range((a-1)-i):
    print(" ",end=" ")
  for k in range(i+1):
    print("*",end=" ")
  print()    

# ------------------------------------------------------------------------------------------------------

for i in range(a):
  for j in range(i):
    print(" ",end=" ")
  for k in range(a-i):
    print("*",end=" ")
  print()    

# ------------------------------------------------------------------------------------------------------

for i in range(5):
  for j in range(4-i):
    print(" ",end="")
  for k in range(i+1):
    if i%2==0:
      print("*",end=" ")
    else:
        print("#",end=" ")
  print()  

for i in range(4):
  for j in range(i+1):
    print(" ",end="")
  for k in range(4-i):
    if i%2==0:
      print("#",end=" ")
    else:
        print("*",end=" ")
  print()    

# -----------------------------------------------------------------------------------------------------

count=65
for i in range(5):
  # count=65
  for j in range(4-i):
    print(" ",end="")
  for k in range(i+1):
    print(chr(count),end=" ") 
    count+=1
  print()  

# -----------------------------------------------------------------------------------

for i in range(5):
  line=" "
  for k in range(5-i):
    line+="*"
  for j in range(i*2):
    line += " "
  for m in range(5-i):
    line+="*"
  print(line)  
for i in range(4,-1,-1):
  line=" "
  for k in range(5-i):
    line+="*"
  for j in range(i*2):
    line += " "
  for m in range(5-i):
    line+="*"
  print(line)   

# ------------------------------------------------------------------------------------------- 

