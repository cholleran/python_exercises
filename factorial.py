

# GMIT Module 52167 - Exercise 6 - Student: Cormac Holleran
# Adapted from https://www.programiz.com/python-programming/examples/factorial and
# https://stackoverflow.com/questions/5136447/function-for-factorial-in-python

def factorial_find(x):
  factfin = 1
  for i in range(1,x + 1):      
    factfin = factfin * i
  return(factfin)

# for each number in the range 1- 5(including 5) the program starts with factfin value 1 and multiplies by first number in range
#  Each iteration creates a new variable called 'factfin', and each num in range is only multiplied by 'factfin' once.


print("The factorial of 5 is ",factorial_find(5))
print("The factorial of 7 is ",factorial_find(7))
print("The factorial of 10 is ",factorial_find(10))


