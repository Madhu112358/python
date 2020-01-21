'''Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)'''
#Fibonacci Function
def fibonacci(len):
  fib =[1,1]
  for ele in range(1,len-1):
    a= fib[ele] + fib[ele-1]
    fib.append(a)
  return (fib)
##Validate Length and Print Fib   
def validateLen(len):
  if len.isdigit() and len!="1":
    fib = fibonacci(int(len))
    print("List of Fibonacci : ",fib)
  else :
    print("Please enter a Number greater than 1")

print(" Welcome to Fibonacci Numbers! \n  Please type EXIT to stop it! ")
while True:
  len = input("Enter the count of fibonacci Numbers :")
  if len.lower() == "exit":
    print("Thanks!")
    break
  validateLen(len)
