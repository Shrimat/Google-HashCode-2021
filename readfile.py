from Street import Street
from Intersection import Intersection
from Car import Car

NUM_OF_STREETS_IN_PATH_INDEX = 0

BONUS_POINT_INDEX = 4

CAR_NUM_INDEX = 3

STREET_NUM_INDEX = 2

INTERSECTION_NUM_INDEX = 1

DURATION_INDEX = 0

STREET_TRAVEL_TIME_INDEX = 3

STREET_END_NODE_INDEX = 1

STREET_BEGIN_NODE_INDEX = 0

STREET_NAME_INDEX = 2


def is_street(line: str) -> bool:
    words = line.split(" ")
    return words[1].isdigit()


def get_input_information(input_file):
    with open(input_file, "r") as f:
        file_content_lines = f.read().splitlines()

    basic_info = file_content_lines[0]
    streets = []
    car_paths = []

    i = 1
    while i < len(file_content_lines):
        if not is_street(file_content_lines[i]):
            break
        streets.append(file_content_lines[i])
        i += 1
    while i < len(file_content_lines):
        car_paths.append(file_content_lines[i])
        i += 1

    _, intersection_num, _, _, _ = get_basic_information(basic_info)
    streets, intersection_list = convert_to_list_of_streets(streets, intersection_num)
    cars = convert_to_car_paths(car_paths, streets)

    return basic_info, streets, intersection_list, cars


def get_basic_information(basic_info_lines):
    basic_info_lines = basic_info_lines.split()
    duration = int(basic_info_lines[DURATION_INDEX])
    intersection_num = int(basic_info_lines[INTERSECTION_NUM_INDEX])
    street_num = int(basic_info_lines[STREET_NUM_INDEX])
    car_num = int(basic_info_lines[CAR_NUM_INDEX])
    bonus_points = int(basic_info_lines[BONUS_POINT_INDEX])
    return duration, intersection_num, street_num, car_num, bonus_points


def convert_to_list_of_streets(street_lines, num_of_intersections):
    intersection_list = [Intersection([], intersection_id) for intersection_id in range(num_of_intersections)]
    streets = {}
    for line in street_lines:
        line = line.split(" ")
        street_name = line[STREET_NAME_INDEX]
        end_intersection = int(line[STREET_END_NODE_INDEX])
        travel_time = int(line[STREET_TRAVEL_TIME_INDEX])
        current_street = Street(travel_time)
        streets[street_name] = current_street
        intersection_list[end_intersection].incoming_streets.append(current_street)

    return streets, intersection_list


def convert_to_car_paths(cars, streets):
    car_list = []
    for car in cars:
        current_car = Car([])
        car_line = car.split(" ")
        num_of_streets = int(car_line[NUM_OF_STREETS_IN_PATH_INDEX])
        for street_index in range(num_of_streets):
            street_name = car_line[1 + street_index]
            current_car.streets.append(streets[street_name])
        car_list.append(current_car)

    return car_list
