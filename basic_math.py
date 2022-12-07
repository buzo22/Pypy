# declare the integers
num1, num2 = input("Enter two numbers: ").split()

# assign the integers
num1 = int(num1)
num2 = int(num2)

# sum integers
sum = num1 + num2

# subtract integers
difference = num1 - num2

# multiply integers
product = num1 * num2

# divide integers
quotient = num1 / num2

# find the remainder
remainder = num1 % num2

print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))