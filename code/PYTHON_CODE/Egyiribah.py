print("Hello World!")
print("welcome to Egyiriba_gh website")
print("Authentic African Brand")
print("organic products")


def sum (first, second):
  addition = first + second
  return addition

print ( sum(10, 5))
print (sum(total, 20))
print(sum(total, 30))

total = sum(total, 50)
print("The total is: ", total)

def calculate (action, firstNum, secondNum):
  if action == "add" :
   result = firstNum + secondNum
   return result

 if action == "subtract" : 
  result = firstNum - secondNum
  return result

calcResult = calculate("subtract", 10, 5)
calcResult = calculate("add", calcResult, 5)

print("The result is: ", calcResult)

print("The result is: ", calcResult) 


number = 1 

while number <= 20 :
  print("Number: ", number)
  
  number = number + 1

 print("Our loop is done!")
  