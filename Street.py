class Street:

    def __init__(self, travel_time):
        self.travel_time = travel_time
        self.waiting_cars = []
        self.travelling_cars = [] #list of tuples (car, start time)

    def update_travelling_cars(self): #TODO
        return

    def get_waiting_car(self):
        return self.waiting_cars.pop()