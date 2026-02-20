class BusPass:
    transit_name = "Tashkent Metro"
    min_fare = 3
    total_passes = 0
    def __init__(self, holder, balance=0, rides=None):
        self.holder = holder
        self.balance = balance
        if rides is None:
            self.rides = []
        else:
            self.rides = rides
        BusPass.total_passes += 1
    def load_pass(self, amount):
        if amount > 0:
            self.balance += amount
            self.rides.append("+" + str(amount))
            print("Loaded", amount, ". Balance:", self.balance, sep="")
    def take_ride(self, fare):
        if self.balance - fare >= BusPass.min_fare:
            self.balance -= fare
            self.rides.append("-" + str(fare))
            print("Charged", fare, ". Balance:", self.balance, sep="")
        else:
            print("Insufficient balance for ride")
    def display_pass(self):
        print("Holder:", self.holder + ",",
              "Balance:", self.balance + 0, ",",
              "Transit:", BusPass.transit_name)
    def show_rides(self):
        for r in self.rides:
            print(r)

p1 = BusPass("Jamshid", 10)
p1.display_pass()
p1.load_pass(20)
p1.take_ride(5)
p1.take_ride(8)
p1.show_rides()
print("Total passes:", BusPass.total_passes)



