m1 = int(input("Enter the marks of first subject: "))
m2 = int(input("Enter the marks of second subject: "))
m3 = int(input("Enter the marks of third subject: "))

total = m1 + m2 + m3

if(total >= 0.4*300 and m1 >= 0.3*100 and m2 >= 0.3*100 and m3 >= 0.3*100):
    print("You are pass")
else:
    print("You are fail")