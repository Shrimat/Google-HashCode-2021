from readfile import get_input_information
from outputfile import output

duration, streets, intersections, cars = get_input_information("examples/a.txt")

current_time = 0
while current_time < duration:
    for intersection in intersections:
        intersection.update_schedule(current_time)
    current_time += 1

output(intersections, duration-1)
