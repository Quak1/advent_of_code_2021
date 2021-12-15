import sys

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


def generate_sliding(data):
    sliding_window = []

    for i in range(len(data) - 2):
        sliding_window.append(data[i] + data[i+1] + data[i+2])

    return sliding_window


if __name__ == "__main__":
    try:
        data = load_data(sys.argv[1])
    except IndexError:
        print("Please specify data file as your first argument")
        exit()

    count = count_increments(data)
    print('increment count:', count)

    data_sliding = generate_sliding(data)
    count_sliding = count_increments(data_sliding)
    print('increment count sliding:', count_sliding)