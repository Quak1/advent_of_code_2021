def load_data(filename):
    with open(filename, "r") as f:
        nums = f.readline().strip().split(",")
        return [int(i) for i in nums]


def simulate_day(fish):
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            fish.append(8)
        else:
            fish[i] -= 1

    return fish


if __name__ == "__main__":
    data = load_data("test-input.txt")

    for i in range(80):
        simulate_day(data)

    print(len(data))
