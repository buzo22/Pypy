# Run a program advises on school according to age

age = input("Enter your age: ")

if age < 5:
    print("Too young for school")

elif age == 5:
    print("Go to kindegarten")

elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to grade {}".format(grade))

else:
    print("Off to college")