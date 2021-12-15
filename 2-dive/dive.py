import sys


def load_data(filename):
    data = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip().split(" ")
            line[1] = int(line[1])
            data.append(line)

        return data


# Part One
def get_position(data):
    horizontal = 0
    depth = 0
    for entry in data:
        if entry[0] == "forward":
            horizontal += entry[1]
        elif entry[0] == "down":
            depth += entry[1]
        elif entry[0] == "up":
            depth -= entry[1]

    return [horizontal, depth]


# Part Two
def get_position_aim(data):
    horizontal = 0
    depth = 0
    aim = 0
    for entry in data:
        if entry[0] == "forward":
            horizontal += entry[1]
            depth += aim * entry[1]
        elif entry[0] == "down":
            aim += entry[1]
        elif entry[0] == "up":
            aim -= entry[1]

    return [horizontal, depth]


if __name__ == "__main__":
    try:
        data = load_data(sys.argv[1])
    except IndexError:
        print("Please specify data file as your first argument")
        exit()

    position = get_position(data)
    print(position)
    print(position[0] * position[1])

    position = get_position_aim(data)
    print(position)
    print(position[0] * position[1])
