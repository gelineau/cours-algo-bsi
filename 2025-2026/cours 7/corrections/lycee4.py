def read_first_n_lines(filename: str, n: int | None) -> list[str]:
    """
    Reads the first n lines (excluding header) from the given file and returns them as a list of strings.
    """
    lines = []
    with open(filename, mode="r", encoding="utf-8") as file:
        for i, line in enumerate(file):
            if i == 0:
                continue  # Skip header
            if n is not None and i >= n:
                break
            lines.append(line.rstrip("\n"))
    return lines


def filter_lines(lines: list[str], year: str, region: str) -> list[str]:
    """
    Filters the list of CSV lines, keeping only those matching the given year and region.
    """
    filtered = []
    for line in lines:
        columns = line.split(",")
        if columns[1] == year and columns[5] == region:
            filtered.append(line)
    return filtered


def save_lines_to_file(filename: str, lines: list[str], header: str) -> None:
    """
    Saves the given lines to a new CSV file, including the header.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(header + "\n")
        for line in lines:
            file.write(line + "\n")


def main() -> None:
    input_filename = "lycee.csv"
    output_filename = "lycee_filtre.csv"
    n = None  # Number of lines to read (excluding header)
    year = "2024"
    region = "BRETAGNE"

    header = read_header(input_filename)

    first_lines = read_first_n_lines(input_filename, n)
    filtered_lines = filter_lines(first_lines, year, region)
    save_lines_to_file(output_filename, filtered_lines, header)

    for line in filtered_lines:
        print(line)


def read_header(input_filename: str) -> str:
    # Read header separately
    with open(input_filename, mode="r", encoding="utf-8") as file:
        header = file.readline().rstrip("\n")
    return header


if __name__ == "__main__":
    main()
