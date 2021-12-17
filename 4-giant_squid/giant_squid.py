def load_data(filename):
    with open(filename, "r") as f:
        sequece = f.readline().strip().split(",")
        f.readline()

        data = []
        board = []
        for entry in f:
            if entry == "\n":
                data.append({"board": board, "hits": {}})
                board = []
                continue
            temp_entry = entry.strip().replace("  ", " ").split(" ")
            board.append(temp_entry)

        data.append({"board": board, "hits": {}})
        return sequece, data


def mark_board(board, num, board_size=5):
    for row in range(board_size):
        for col in range(board_size):
            if board["board"][row][col] == num:
                if f"row {row}" in board["hits"]:
                    board["hits"][f"row {row}"].append(col)
                else:
                    board["hits"][f"row {row}"] = [col]
                if f"col {col}" in board["hits"]:
                    board["hits"][f"col {col}"].append(row)
                else:
                    board["hits"][f"col {col}"] = [row]
                return board


def check_win(board, board_size=5):
    for k in board["hits"]:
        if len(board["hits"][k]) == board_size:
            return True
    return False


def play(boards, sequence):
    for num in sequence:
        for board in boards:
            mark_board(board, num)
            if check_win(board):
                return get_score(board, num)
    return False


def get_score(board, num, board_size=5):
    count = 0
    for key in board["hits"]:
        if key[:3] == "row":
            for i in range(board_size):
                if not i in board["hits"][key]:
                    row = int(key[4:])
                    count += int(board["board"][row][i])

    print(count)
    print(num)
    return count * int(num)


if __name__ == "__main__":
    sequence, data = load_data("test_input.txt")

    print(play(data, sequence))
