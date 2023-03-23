class Gambler:

    all_gamblers = []

    def __init__(self, name):
        self.name = name
        self.bids = []
        Gambler.all_gamblers.append(self)

    def get_name(self):
        return self.name

    def get_bids(self):
        return [bid for bid in Bid.bids if bid.gambler == self]
        
    def get_dealers(self):
        return [bid.dealer for bid in self.get_bids()]

    def highest_bid(self):
        max_bid = self.get_bids()[0]
        for bid in self.get_bids():
            if bid.amount > max_bid.amount:
                max_bid = bid
        return max_bid

    def average_bid_amount(self):
        total = 0 
        counter = 0
        if not self.get_bids():
            raise Exception("No bid detected")
        else: 
            for bid in self.get_bids():
                total += bid.amount
                counter += 1
            return total/counter

    def has_bidded(self, dealer):
        l = [bid for bid in self.get_bids() if bid.dealer == dealer]
        return bool(l)

    def make_bid(self, dealer, amount):
       new_bid = Bid(self, dealer, amount)
       self.bids.append(new_bid)

    @classmethod
    def highest_average_gambler(cls):
        high_roller = cls.all_gamblers[0]
        for gambler in cls.all_gamblers:
            if gambler.average_bid_amount() > high_roller.average_bid_amount():
                high_roller = gambler
        return high_roller

    def __repr__(self):
        return f"{self.name}"


class Dealer:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_bids(self):
        return [bid for bid in Bid.bids if bid.dealer == self]

    def get_gamblers(self):
        return [bid.gambler for bid in self.get_bids()]
    
    def __repr__(self):
        return f"{self.name}"


class Bid:

    bids = []

    def __init__(self, gambler, dealer, amount):
       self.gambler = gambler
       self.dealer = dealer
       self.amount = amount
       Bid.bids.append(self)

    def get_amount(self):
        return self.amount

    def get_gambler(self):
        return self.gambler

    def get_dealer(self):
        return self.dealer
    
    def __repr__(self):
        return f"{self.gambler} {self.dealer} {self.amount}"
    