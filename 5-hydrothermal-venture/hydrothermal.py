from collections import Counter


def load_data(filename):
    data = []
    with open(filename, "r") as f:
        for line in f:
            points = line.strip().split(" -> ")
            points = [[int(n) for n in i.split(",")] for i in points]
            data.append(points)
    return data


def extend_vector(vector):
    x1 = vector[0][0]
    y1 = vector[0][1]
    x2 = vector[1][0]
    y2 = vector[1][1]

    points = []
    while x1 != x2 or y1 != y2:
        points.append(str([x1, y1]))
        x1 += 0 if x1 == x2 else 1 if x1 < x2 else -1
        y1 += 0 if y1 == y2 else 1 if y1 < y2 else -1
    points.append(str([x2, y2]))

    return points


def extend_all(vectors):
    points = []
    for vector in vectors:
        # p1 = vector[0]
        # p2 = vector[1]
        # if p1[0] == p2[0] or p1[1] == p2[1]:
        points.extend(extend_vector(vector))

    return points


def check_collisions(points):
    counter = Counter(points)

    count = 0
    for val in counter.values():
        if val > 1:
            count += 1
    return count


if __name__ == "__main__":
    data = load_data("input.txt")
    points = extend_all(data)

    collision_count = check_collisions(points)
    print(collision_count)
