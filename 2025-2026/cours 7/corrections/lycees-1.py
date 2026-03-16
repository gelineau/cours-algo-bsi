def read_first_n_lines(filename: str, n: int) -> list[str]:
    """
    Reads the first n lines from the given file and returns them as a list of strings.
    """
    lines = []
    with open(filename, mode="r", encoding="utf-8") as file:
        for i, line in enumerate(file):
            if i == 0:
                continue
            if i >= n:
                break
            lines.append(line.rstrip("\n"))
    return lines


def main() -> None:
    input_filename = "lycee.csv"
    n = 10  # Number of lines to read

    first_lines = read_first_n_lines(input_filename, n)

    for line in first_lines:
        print(line)


if __name__ == "__main__":
    main()
