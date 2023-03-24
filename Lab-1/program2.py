# Python program to convert list of dictionary to tuple list

#Creating initial list of dictionaries
myList = [
        {'Name':'Aravind Bolar', 'Age' : 54},
        {'Name':'Arjun Kapikad', 'Age' : 32},
        {'Name':'Bhojaraj Vamanjoor', 'Age' : 53},
        {'Name':'Naveen D Padeel', 'Age' : 49}
        ]
print("List of dictionaries: ",myList, "\n")

#Converting and storing list of dictionries to list of tuples
tupleList = [(d['Name'],d['Age']) for d in myList]
print("List of tuples: ", tupleList)