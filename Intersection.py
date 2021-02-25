
class Intersection:
    def __init__(self, streets, iid):
        self.incoming_streets = streets
        self.intersection_id = iid
        self.schedule = []

    def update_schedule(self, current_time):
        for street in self.incoming_streets:
            street.update_travelling_cars()
            car = street.get_waiting_car()
            while car is not None:
                if not car.finished():
                    next_street = car.get_next_road()
                    next_street.travelling_cars.append((car, current_time))
                    self.schedule.append((street, current_time))
                    return
                car = street.get_waiting_car()




