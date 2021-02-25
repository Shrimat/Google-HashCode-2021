

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

    print(basic_info)
    print(streets)
    print(car_paths)

    return basic_info, streets, car_paths


'''print(basic_info)
print(roads)
print(car_paths)'''