# https://en.wikipedia.org/wiki/Collatz_conjecture
# Code based on lecture by Dr Ian McLoughlin
# Week 3 exercise - program which applies Collatz to an integer chosen by the user.
# Student: Cormac Holleran, GMIT - Module: 52167

#input is taken from the user and stored as n.
n = int(input('Please enter and integer:'))

# Uses Boolean statements to apply the rules of Collatz conjecture.
# The 'while' keyword ensures the program runs until the number reaches 1.
while n != 1:
    if n % 2 == 0:
        n = n / 2
        print (n)
    elif n % 2 > 0:
        n = (n * 3) + 1
        print (n)
