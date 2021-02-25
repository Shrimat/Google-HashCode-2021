f = open("schedule.txt", "w")
intersections = []
f.write(str(len(intersections)) + "\n")

for intersection in intersections:
    f.write(intersection.intersection_id)
    for street in intersection.incoming_streets:
        f.write(street.name)
        # TODO: Add the time schedule for that intersection

f.close()
