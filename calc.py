print("Enter 2 numbers and desired operation to find result")
  
no1=float(input("enter 1st number"))
no2=float(input("enter 2nd number"))
operation=input("enter operation")

if(operation=="+"):
  print(no1+no2)
  
elif(operation=="-"):
  print(no1-no2)
  
elif(operation=="*"):
  print(no1*no2)
  
elif(operation=="/"):
  if (no2==0):
    print("error cannont divide by 0")
  else:
    print(no1/no2)
    
elif(operation=="%"):
  if (no2==0):
    print("error cannont modulus by 0")
  else:
    print(no1%no2)
    
else:
  print("invalid operation")
