"""
AISDI - Zad 1
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
    min = 0
    max = len(table) - 1
    quicksort_t(table, min, max)
    return table


def quicksort_t(table, min, max):
    #Jako oś przyjmuje zawsze pierwszy element z listy, zamiana zawsze tego elementu z elementem więkzym lub większym.
    if min >= max or min<0 or max >= len(table):
        return 0
    p = min
    q = max
    p_q_bool = False
    while True:
        if table[p]>=table[q]:
            table[p], table[q] = table[q], table[p]
            p_q_bool = not p_q_bool
        if p_q_bool:
            p += 1
        else:
            q -= 1
        if p == q:
            break
    quicksort_t(table, min, p-1)
    quicksort_t(table, p+1, max)

tab = [4,2,9,4,8,1,0,4,7,2]
print(quicksort(tab))

def measureSorting(func, table, elements = None):
    if elements == None:
        string_m = f"{func}({table})"
    else:
        string_m = f"{func}({table}[:{elements}])"
    string_s = f"from __main__ import {func}\nfrom __main__ import {table}"
    time = timeit.timeit(string_m, string_s, number = 1)
    return time


def load(file_name):
    with open(file_name, encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines() if line.strip() != ""]
        words = []
        for line in lines:
            words += line.lower().split(" ")
        return words

if __name__ == "__main__":
    words = load("pan-tadeusz.txt")
    sorted_words_a = bubblesort(words[:1000])
    sorted_words_b = selectionsort(words[:1000])
    sorted_words_c = quicksort(words[:1000])
    time_q = measureSorting("quicksort", "words", 1000)
    time_b = measureSorting("bubblesort", "words", 1000)
    time_s = measureSorting("selectionsort", "words", 1000)
    print(f"quick: {time_q}\nselection: {time_s}\nbubble: {time_b}\nQuickest: {min(time_q,time_b,time_s)}")