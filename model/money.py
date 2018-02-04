class Money:
    def __init__(self, timestamp, money):
        self.timestamp = timestamp
        self.money = int(money)

    def get_tuple(self, money):
        return (self.timestamp,
                money - int(self.money))
