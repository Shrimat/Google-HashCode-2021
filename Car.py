class Car:
    def __init__(self, streets, path):
        self.streets = streets
        self.path = path

    def get_next_road(self):
        return self.streets.pop(0)

    def finished(self) -> bool:
        return self.streets.empty()
