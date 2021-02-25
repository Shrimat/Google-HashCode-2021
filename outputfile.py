def output(intersections, end_time):
    f = open("schedule.txt", "w")
    f.write(str(len(intersections)) + "\n")

    for intersection in intersections:
        result = intersection.get_schedule(end_time)
        if result is not None:
            f.write(result)
        #f.write("\n")

    f.close()
