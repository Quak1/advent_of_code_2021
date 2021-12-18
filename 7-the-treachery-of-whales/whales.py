def load_data(filename):
    with open(filename, "r") as f:
        nums = f.readline().strip().split(",")
        return [int(n) for n in nums]


def move_to_position(data, position):
    fuel = 0
    for entry in data:
        steps = abs(position - entry)
        fuel += (steps ** 2 + steps) / 2

    return fuel


def find_minimun(data):
    for i in range(min(data), max(data) + 1):
        if i == 0:
            min_fuel = move_to_position(data, i)
            min_pos = 0
        else:
            fuel = move_to_position(data, i)
            if fuel < min_fuel:
                min_fuel = fuel
                min_pos = i

    return min_fuel, min_pos


if __name__ == "__main__":
    data = load_data("input.txt")

    fuel, pos = find_minimun(data)

    print(pos, fuel)
