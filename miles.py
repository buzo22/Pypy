# a program that converts miles to kilomters

# enter miles
miles = input("Enter miles: ")

# convert to integers
miles = int(miles)

# conversion to kilomter
kilometers = miles * 1.60934

# print output
print("{} miles equals {} kilometers".format(miles, kilometers))