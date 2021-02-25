def output(intersections, end_time, name):
    f = open(f"schedule-{name}.txt", "w")
    f.write(str(len(intersections)) + "\n")

    for intersection in intersections:
        result = intersection.get_schedule(end_time)
        if result is not None:
            f.write(result)
        #f.write("\n")

    f.close()
