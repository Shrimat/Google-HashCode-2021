class Street:

    def __init__(self, travel_time):
        self.travel_time = travel_time
        self.waiting_cars = []
        self.travelling_cars = []  # list of tuples (car, start time)

    def update_travelling_cars(self, current_time):
        for i in range(len(self.travelling_cars)):
            (car, start_time) = self.travelling_cars[i]
            if self.travel_time + start_time == current_time:
                new_car = self.travelling_cars.pop(i)
                self.waiting_cars.append(new_car)

    def get_waiting_car(self):
        return self.waiting_cars.pop(0)
