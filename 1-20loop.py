#Adapted from:https://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution
# This program uses a 'for' loop to find the lowest number evenly divisible by all numbers from 1-20.
# Student: Cormac Holleran //GMIT - Module: 52167

one_to_twenty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16, 17, 18, 19, 20]

for num in range(20, 10**10, 20):
  if all(num % n == 0 for n in one_to_twenty):
    break 
  else:
    continue
print("The smallest number divisible by all numbers in list is", num)
    
     
    
