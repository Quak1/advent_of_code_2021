LIFETIME = 9


def load_data(filename):
    with open(filename, "r") as f:
        nums = f.readline().strip().split(",")
        fish = [0 for _ in range(LIFETIME)]
        for d in nums:
            fish[int(d)] += 1
    return fish


def simulate_day(fish):
    new_fish = fish[0]
    for i in range(LIFETIME - 1):
        fish[i] = fish[i + 1]

    fish[6] += new_fish
    fish[LIFETIME - 1] = new_fish

    return fish


def count_fish(fish):
    count = 0
    for i in fish:
        count += i

    return count


if __name__ == "__main__":
    data = load_data("input.txt")

    for i in range(256):
        simulate_day(data)

    print(count_fish(data))
