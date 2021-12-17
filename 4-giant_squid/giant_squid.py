from os import sep


def load_data(filename):
    with open(filename, "r") as f:
        sequece = f.readline().strip().split(",")
        f.readline()

        data = []
        board = []
        for entry in f:
            if entry == "\n":
                data.append(board)
                board = []
                continue
            temp_entry = entry.strip().replace("  ", " ").split(" ")
            board.append(temp_entry)

        data.append(board)
        return sequece, data


# def


if __name__ == "__main__":
    load_data("test_input.txt")
