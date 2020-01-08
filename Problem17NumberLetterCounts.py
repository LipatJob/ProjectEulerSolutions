toTwenty = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens = ["twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]

powtens = ["hundred", "thousand"]


n = input("Enter a number: ")

digits = []


for digit in reversed(n):
    digits.append(digit);

print(digits)




