name = input("Enter a name: ")

nameList = ["Siddharth", "Steve", "Tony", "Clark", "Bruce", "Peter", "Natasha", "Wade", "Thor", "Loki"]

# if(nameList.count(name) != 0):
#     print("Name found in the list")
# else:
#     print("Name not found in the list")

if(name in nameList):
    print("Name found in the list")
else:
    print("Name not found in the list")