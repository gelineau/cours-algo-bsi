import time
import threading


def sleep_sort(num):
    def append_number(result_list, n):
        time.sleep(n)
        result_list.append(n)

    threads = []
    sorted_numbers = []

    for n in num:
        thread = threading.Thread(target=append_number, args=(sorted_numbers, n))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sorted_numbers


# Example usage:
numbers_to_sort = [5, 2, 8, 1, 3]
print("Original list:", numbers_to_sort)

sorted_list = sleep_sort(numbers_to_sort)
print("Sorted list:", sorted_list)
