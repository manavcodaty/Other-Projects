class booking():
    def __init__(self, name, date, time, duration, location, price):
        self.name = name
        self.date = date
        self.time = time
        self.duration = duration
        self.location = location
        self.price = price
    def get_booking(self):
        self.name = input("Enter your name: ")
        self.date = input("Enter the date (YYYY:MM:DD): ")
        self.time = input("Enter the time (HH:MM): ")
        self.duration = input("Enter the duration (in hours): ")
        self.location = input("Enter the location: ")
        self.price = input("Enter the price:")
    def print_booking(self):
        print(self.name)
        print(self.date)
        print(self.time)
        print(self.duration)
        print(self.location)
        print(self.price)
    
    

    
    
