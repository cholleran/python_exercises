
# GMIT Module 52167 - Exercise 5 - Student: Cormac Holleran
#https://stackoverflow.com/questions/275018/how-can-i-remove-chomp-a-trailing-newline-in-python
with open ("Data\iris.csv") as f:
    for line in f:
      col_1 = (line.split(',')[0])
      col_2 = (line.split(',')[1])
      col_3 = (line.split(',')[2])
      col_4 = (line.split(',')[3])
      col_5 = (line.split(',')[4])
      Table = ("{:^6} {:^6} {:^6} {:^6} {:>20}".format(col_1, col_2, col_3, col_4, col_5))
      print(Table.rstrip('\n'))