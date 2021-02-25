class Car:
    def __init__(self, streets):
        self.streets = streets

    def get_next_road(self):
        return self.streets.pop(0)

    def finished(self) -> bool:
        return self.streets.empty()
