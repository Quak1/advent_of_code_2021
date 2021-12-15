from os import getgid
import sys


def load_data(filename):
    data = []
    with open(filename, "r") as f:
        for line in f:
            data.append(line.strip())
    return data


def get_most_common(data):
    count = []
    for i in range(len(data[0])):
        temp = {"zeros": 0, "ones": 0}
        for entry in data:
            if entry[i] == "0":
                temp["zeros"] += 1
            else:
                temp["ones"] += 1

        if temp["zeros"] > temp["ones"]:
            temp["most_common"] = 0
        else:
            temp["most_common"] = 1

        count.append(temp)

    return count


def get_rates(data):
    gamma = ""
    epsilon = ""

    count = get_most_common(data)
    for entry in count:
        if entry["most_common"] == 0:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    return gamma, epsilon


if __name__ == "__main__":
    try:
        data = load_data(sys.argv[1])
    except IndexError:
        print("Please specify data file as your first argument")
        exit()

    gamma, epsilon = get_rates(data)

    print(gamma, epsilon)
    print(int(gamma, 2), int(epsilon, 2))
    print(int(gamma, 2) * int(epsilon, 2))
