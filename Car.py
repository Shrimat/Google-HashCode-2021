class Car:
    def __init__(self, streets):
        self.streets = streets

    def get_next_road(self):
        if self.streets.empty():
            return None
        return self.streets.pop(0)

    def finished(self) -> bool:
        return len(self.streets) == 0
