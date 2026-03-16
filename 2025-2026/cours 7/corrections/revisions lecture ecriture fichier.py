def print_start_of_lines(file_name: str):
    with open(file_name) as file:
        for line in file:
            print(line[:10])


def print_start_of_lines_padded1(file_name: str):
    with open(file_name) as file:
        for line in file:
            if line[-1] == "\n":
                line = line[:-1]
            if len(line) < 10:
                line = line + "*" * (10 - len(line))
            else:
                line = line[:10]
            print(line)


def print_start_of_lines_padded(file_name: str):
    with open(file_name) as file:
        for line in file:
            line = line.strip() + "*" * 10
            print(line[:10])


print_start_of_lines_padded1("example.txt")
