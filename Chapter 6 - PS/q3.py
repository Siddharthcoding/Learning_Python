# message = "This is the best python course, buy now or never!"

# if(message.find("Make a lot of money") != -1 or message.find("buy now") != -1 or message.find("click this") != -1 or message.find("subscribe this") != -1):
#     print("Spam message")
# else:
#     print("Not a spam message")

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "click this"
p4 = "subscribe this"

message = input("Enter the message: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):  # 'in' is used to check if a substring exists in a string
    print("Spam message")
else:
    print("Not a spam message")