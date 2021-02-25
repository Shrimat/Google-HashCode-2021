class Street:

    def __init__(self, name, begin_node, end_node, travel_time):
        self.name = name
        self.begin_intersection = begin_node
        self.end_intersection = end_node
        self.travel_time = travel_time
        self.waiting_cars = []
        self.travelling_cars = [] #list of tuples (car, start time)

    def update_travelling_cars(self): #TODO
        return

    def get_waiting_car(self):
        return self.waiting_cars.pop()