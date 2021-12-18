from os import sep


def load_data(filename):
    data = []
    with open(filename, "r") as f:
        for line in f:
            entry = line.strip().split(" | ")
            entry = [e.split(" ") for e in entry]
            data.append(entry)

    return data


def count_digits(data):
    sizes = [2, 3, 4, 7]
    count = 0
    for entry in data:
        for i in range(4):
            if len(entry[1][i]) in sizes:
                count += 1
    return count


if __name__ == "__main__":
    data = load_data("test-input.txt")

    print(count_digits(data))
