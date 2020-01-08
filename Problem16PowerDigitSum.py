n = int(input("Enter N: "))
y = 2**n

digsum = 0;

while y>0:
    digsum += y%10
    y  = y//10

print(digsum)
