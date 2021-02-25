f = open("../a.txt", "r")
file_content_lines = f.read().splitlines()


def is_road(line: str) -> bool:
    words = line.split(" ")
    return words[1].isdigit()


basic_info = file_content_lines[0]
roads = []
car_paths = []

i = 1
while i < len(file_content_lines):
    if not is_road(file_content_lines[i]):
        break
    roads.append(file_content_lines[i])
    i += 1
while i < len(file_content_lines):
    car_paths.append(file_content_lines[i])
    i += 1

'''print(basic_info)
print(roads)
print(car_paths)'''