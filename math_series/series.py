# Define the Fibonacci function in recursive method
def fibonacci(n): 
 if n < 0: 
  print("Incorrect input") 
# First Fibonacci number is 0 
 elif n==0: 
    return 0
# Second Fibonacci number is 1 
 elif n==1: 
   return 1
 else: 
   return fibonacci(n-1)+fibonacci(n-2) 
# Driver function 
print(fibonacci(7))

# Define the Lukas function in recursive method
def lukas(n): 
 if n < 0: 
  print("Incorrect input") 
# First Fibonacci number is 0 
 elif n==0: 
    return 2
# Second Fibonacci number is 1 
 elif n==1: 
   return 1
 else: 
   return lukas(n-1)+lukas(n-2) 
# Driver function 
print(lukas(7))
# Define third function sum_series to print both fibonacci or lukas based on input
def sum_series(y,z=0,w=0):
 if z ==2 and w ==1:
   print('The element' , y) 
   print("From Lukas function") 
   print(lukas(y))   
# First Fibonacci number is 0 
 else: 
  print('The element' , y) 
  print("From Fabinacci function is : ") 
  print(fibonacci(y)) 
sum_series(7,z=2,w=1)
#Sum_series(7)

    




