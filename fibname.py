# Student: Cormac Holleran, GMIT - Module: 52167
# Fibonacci sequence program - source code from Dr Ian McLoughlin

# A program that displays Fibonacci numbers using people's names.

# Week 1 solution: My name is Cormac, so the first and last letter of my name (C + C = 3 + 3) give the number 6. The 6th Fibonacci number is 8.

# Week 2 solution: My surname is Holleran
# The first letter H is number 72
# The last letter n is number 110
# Fibonacci number 182 is 48558529144435440119720805669229197641

# The ord() function in Python converts a character we see on the screen into its corresponding Unicode value.  Unicode is like a 'reference map' of how each character is stored/used as eight 1's and 0's at hardware level.

def fib(n):

  """This function returns the nth Fibonacci number."""

  i = 0

  j = 1

  n = n - 1



  while n >= 0:

    i, j = j, i + j

    n = n - 1

  

  return i



name = "Holleran"

first = name[0]

last = name[-1]

firstno = ord(first)

lastno = ord(last)

x = firstno + lastno



ans = fib(x)

print("My surname is", name)

print("The first letter", first, "is number", firstno)

print("The last letter", last, "is number", lastno)

print("Fibonacci number", x, "is", ans)
