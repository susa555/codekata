number = int(input(5))
total = 0

for value in range(1, number + 1):
    total = total + value

print("The Sum of Natural Numbers from 1 to {0} =  {1}".format(number, total))
