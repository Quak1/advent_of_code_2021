def load_data(filename):
    with open(filename, 'r') as f:
        data = []
        for line in f:
            data.append(int(line.strip()))
    return data


def count_increments(data):
    increment_count = 0
    previous_entry = data[0]

    for entry in data[1:]:
        if entry > previous_entry:
            increment_count += 1
        previous_entry = entry

    return increment_count


if __name__ == "__main__":
    data = load_data('input.txt')
    count = count_increments(data)
    print('increment count:', count)