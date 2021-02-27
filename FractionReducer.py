from math import *

def EuclidsAlgorithmithm (int1,int2):
  # 'intA' goes to the bigger integer; and 'intB' to the smaller integer:
  if int1>int2:
    intA = int1
    intB = int2
  else:
    intA = int2
    intB = int1
 
  #Finding the remainder of the two:
  remainder=intA%intB
 
  while remainder!=0:
    intA=intB
    intB=remainder
    remainder=intA%intB
 
  return intB
 
#WELCOME MESSAGE:
print("Welcome to the Fraction Reducer! ")
 
#HOW MUCH FRACTIONS THAT THE USER WANTS TO REDUCE (IN CASE HE WANTS TO REDUCE MORE THAN ONE AND TO KEEP TRACK OF THE FRACTIONS)
numfractions=int(input("How many fractions are you going to enter?: "))
 
#N IS THE DESIRED AMOUNT OF FRACTIONS ENTERED
n=0
 
#HOW MUCH TIMES THE LOOP IS REPEATED
while n<numfractions:
  #ENTER NUMERATOR AND DENOMINATOR
  a=int(input("Enter the numerator: "))
  b=int(input("Enter the denominator: "))
 
  #IF A OR B IS EQUAL TO 0
  if b==0:
    print("Your fraction divides by zero. This fraction is undefined. ")
 
  elif a==0:
    print(str(a)+"/" + str(b)+" = 0")
 
  else:
    gcd = EuclidsAlgorithmithm(a,b)
    finala = a/gcd
    finalb = b/gcd
 
    if finala==a and finalb!=1:
      print("The fraction",str(a) + "/" + str(b),"is already reduced.")
    else:
      if finala%finalb==0:
        finalty=str(int(a/b))
      else:
        finalty=str(int(finala)) + "/" + str(int(finalb))
      print(str(a) + "/" + str(b) + " = ", finalty)
