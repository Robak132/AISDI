"""
AISDI - Zad 2
Jakub Robaczewski, Oskar Bartosz
"""
import timeit


def bubblesort(table):
    copy_table = table
    for i in range(len(copy_table)):
        for j in range(1, len(copy_table)-i):
            if copy_table[j] < copy_table[j-1]:
                boot = copy_table[j]
                copy_table[j] = copy_table[j-1]
                copy_table[j-1] = boot
    return copy_table


def selectionsort(table):
    left = 0
    right = len(table) - 1
    while left < right:
        _min = left
        _min_v = table[left]
        _max = left
        _max_v = table[left]
        for i in range(left, right + 1):
            if table[i] < _min_v:
                _min_v = table[i]
                _min = i
            if table[i] > _max_v:
                _max_v = table[i]
                _max = i
        table[_min] = table[left]
        table[left] = _min_v
        table[_max] = table[right]
        table[right] = _max_v

        left += 1
        right -= 1
    return table


def quicksort(table):
    _min = 0
    _max = len(table) - 1
    quicksort_t(table, _min, _max)
    return table


def quicksort_t(table, _min, _max):
    # Jako oś przyjmuje zawsze pierwszy element z listy, zamiana zawsze tego elementu z elementem więkzym lub większym.
    if _min >= _max or _min < 0 or _max >= len(table):
        return 0
    p = _min
    q = _max
    p_q_bool = False
    while True:
        if table[p] >= table[q]:
            table[p], table[q] = table[q], table[p]
            p_q_bool = not p_q_bool
        if p_q_bool:
            p += 1
        else:
            q -= 1
        if p == q:
            break
    quicksort_t(table, _min, p-1)
    quicksort_t(table, p+1, _max)


def measureSorting(func, table, elements=None):
    if elements is None:
        string_m = f"{func}({table})"
    else:
        string_m = f"{func}({table}[:{elements}])"
    string_s = f"from __main__ import {func}\nfrom __main__ import {table}"
    time = timeit.timeit(string_m, string_s, number=1)
    return time


def load(file_name):
    with open(file_name, encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines() if line.strip() != ""]
        words = []
        for line in lines:
            words += line.lower().split(" ")
        return words


def print_mesurements(func, table, start, stop, step, file_name):
    with open(file_name, "w+") as file:
        for i in range(start, stop+1, step):
            time = measureSorting(func, table, i)
            file.write(f"{i:6}: {str(time).replace('.', ',')}\n")
            print(f"{i:6}: {str(time).replace('.', ',')}")


def sort_test(table):
    print("Selection sort")
    print(selectionsort(table))
    print("Bubble sort")
    print(bubblesort(table))
    print("Quick sort")
    print(quicksort(table))


if __name__ == "__main__":
    words = load("pan-tadeusz.txt")
    test_words = [11, 46, 90, 9, 45, 39, 43, 64]

    # Test algorytmów sortujących
    # sort_test(test_words)

    print("Selection sort")
    print_mesurements("selectionsort", "words", 1000, 20000, 1000, "select_sort.txt")

    print("Bubble sort")
    print_mesurements("bubblesort", "words", 1000, 20000, 1000, "bubble_sort.txt")

    print("Quick sort")
    print_mesurements("quicksort", "words", 1000, 70000, 1000, "quick_sort.txt")
