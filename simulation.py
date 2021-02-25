from readfile import get_input_information
from outputfile import output

names = ["a", "b", "c", "d", "e", "f"]

for name in names:
    duration, streets, intersections, cars = get_input_information(f"examples/{name}.txt")

    current_time = 0
    while current_time < duration:
        for intersection in intersections:
            intersection.update_schedule(current_time)
        print(current_time)
        current_time += 1

    output(intersections, duration-1, name)
