# Declaring empty dictionary
d = dict()

#Taking input from the user
n = int(input("Enter number of students: "))
for i in range(0,n):
    key = input(f"Enter key-{i+1}:")
    value = input(f"Enter value for key-{i+1}:")
    d[key] = value

#Printing dictionary keys and values into the console
for key in d.keys():
    print(f"{key}---->{d[key]}")
