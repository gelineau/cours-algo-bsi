import csv
from pprint import pprint
import matplotlib.pyplot as plt


def read_first_n_lines(filename: str, n: int | None) -> list[list[str]]:
    """
    Reads the first n lines (excluding header) from the given CSV file and returns them as a list of lists.
    """
    lines = []
    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 0:
                continue  # Skip header
            if n is not None and i >= n:
                break
            lines.append(row)
    return lines


def filter_lines(lines: list[list[str]], year: str, region: str) -> list[list[str]]:
    """
    Filters the list of CSV rows, keeping only those matching the given year and region.
    """
    filtered = []
    for columns in lines:
        if columns[1] == year and columns[5] == region:
            filtered.append(columns)
    return filtered


def save_lines_to_file(
    filename: str, lines: list[list[str]], header: list[str]
) -> None:
    """
    Saves the given rows to a new CSV file, including the header.
    """

    with open(filename, "w") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for line in lines:
            writer.writerow(line)


def read_header(input_filename: str) -> list[str]:
    with open(input_filename, mode="r") as file:
        reader = csv.reader(file)
        for header in reader:
            return header


def count_lycees_by_city(filename: str) -> dict[str, int]:
    """
    Reads the filtered CSV file and counts the number of lycées per city.
    Returns a dictionary {city: count}.
    """
    city_counts = {}
    with open(filename, mode="r") as file:
        reader = csv.reader(file)

        for i, row in enumerate(reader):
            if i == 0:
                continue  # Skip header
            city = row[10]
            if city in city_counts:
                city_counts[city] += 1
            else:
                city_counts[city] = 1
    return city_counts


def sort_lycees_by_global_success_rate(filename: str) -> list[tuple[str, float]]:
    """
    Sorts schools by their global success rate in descending order.
    Returns a list of tuples (school_name, success_rate).
    """
    lycees = []
    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 0:
                continue  # Skip header
            rate = int(row[13])

            lycees.append((rate, row[3]))
    lycees.sort(reverse=True)
    return lycees


def get_success_rates_by_year(filename: str, uai: str) -> dict[str, int]:
    """
    Returns a dictionary {year: success_rate} for the given school UAI.
    """
    rates = {}
    with open(filename, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 0:
                continue  # Skip header
            if row[2] == uai:

                year = row[1]
                rates[year] = int(row[13])

    return rates


def plot_success_rate_evolution(rates_by_year: dict[str, float]) -> None:
    """
    Plots the evolution of the success rate for a given school UAI.
    """
    # Sort years for correct plotting
    years = sorted(rates_by_year.keys())
    rates = [rates_by_year[year] for year in years]

    plt.figure()
    plt.plot(years, rates)
    plt.title(f"Evolution of Success Rate")  # Set the title of the plot
    plt.xlabel("Year")  # Label the x-axis as "Year"
    plt.ylabel("Success Rate (%)")  # Label the y-axis as "Success Rate (%)"
    plt.grid(True)  # Show a grid on the plot for better readability
    plt.show()  # Display the plot window


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

    lycees_by_city = count_lycees_by_city(output_filename)

    print("\nNombre de lycées par ville :")
    for city, count in lycees_by_city.items():
        print(f"{city}: {count}")

    sorted_lycees = sort_lycees_by_global_success_rate(output_filename)

    pprint(sorted_lycees)

    uai = "0350795Z"
    rates_by_year = get_success_rates_by_year(input_filename, uai)
    plot_success_rate_evolution(rates_by_year)


if __name__ == "__main__":
    main()
