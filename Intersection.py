class Intersection:
    def __init__(self, streets, iid: int):
        self.incoming_streets = streets
        self.intersection_id = iid
        self.schedule = []
        self.curr_street = None

    def update_schedule(self, current_time):
        if self.curr_street is None or len(self.curr_street.waiting_cars) == 0:
            if len(self.incoming_streets) == 0:
                return None
            if self.get_max_car_street(current_time) is None:
                return

        self.curr_street.update_travelling_cars(current_time)
        while self.curr_street.get_waiting_car:
            car = self.curr_street.get_waiting_car()
            if car is None:
                break
            next_street = car.get_next_road()
            if not car.finished():
                next_street.travelling_cars.append((car, current_time))
                return

    def get_max_car_street(self, current_time):

        street = self.incoming_streets[0]
        num_cars = len(street.waiting_cars)
        for i in range(1, len(self.incoming_streets)):
            temp_street = self.incoming_streets[i]
            temp_street.update_travelling_cars(current_time)
            temp_num_cars = len(temp_street.waiting_cars)
            if temp_num_cars > num_cars:
                street = temp_street
                num_cars = temp_num_cars
        if num_cars == 0:
            return None
        self.incoming_streets.remove(street)
        self.curr_street = street
        self.schedule.append((street, current_time))

    def get_schedule(self, end_time):
        if len(self.schedule) == 0:
            return None
        output = str(self.intersection_id) + '\n' + str(len(self.schedule)) + '\n'
        for i in range(len(self.schedule)):
            if i == len(self.schedule) - 1:
                output += self.schedule[i][0].name + ' ' + str(end_time - self.schedule[i][1])
            else:
                output += self.schedule[i][0].name + ' ' + str(self.schedule[i + 1][1] - self.schedule[i][1])
            output += '\n'
        return output
