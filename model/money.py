class Money:
    def __init__(self, timestamp, money):
        self.timestamp = timestamp
        self.money = money

    def get_tuple(self):
        return (self.timestamp,
                self.money)
