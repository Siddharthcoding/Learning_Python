from random import randint  # Importing randint from random module

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def bookTicket(self, fro, to):
        print(f"Ticket is booked for train {self.trainNo} from {fro} to {to}.")

    def getStatus(self):
        print(f"Train {self.trainNo} is running on time.")

    def getFair(self, fro, to):
        print(f"Ticket fare in train {self.trainNo} from {fro} to {to} is {randint(300, 5000)} rupees.")

t = Train("12345")
t.bookTicket("Delhi", "Mumbai")
t.getStatus()
t.getFair("Delhi", "Mumbai")