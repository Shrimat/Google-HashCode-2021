f = open("schedule.txt", "w")
intersections = []
f.write(str(len(intersections)) + "\n")

for intersection in intersections:
    f.write(intersection.get_schedule())
    f.write("\n")

f.close()
