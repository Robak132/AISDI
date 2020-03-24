"""
AISDI - Zad 1
Jakub Robaczewski, Oskar Bartosz
"""


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
    print(table)
    low = 0
    high = len(table)-1
    if low==high:
        return table
    pivot = table[low]
    p = low
    q = high
    while True:
        while p!=q:
            if table[q] < table[p]:
                buf = table[p]
                table[p] = table[q]
                table[q]= buf
                break
            else:
                q -=1
        while p!=q:
            if table[q] < table[p]:
                buf = table[p]
                table[p] = table[q]
                table[q]= buf
                break
            else:
                p += 1
        if p==q:
            break
    if p==low:
        t = [table[p]]
        t += quicksort(table[p+1 : high+1])
        return t
    elif p == high:
        t = quicksort(table[low : p])
        t.append(table[p])
        return t
    else:
        lewa = quicksort(table[low : p])
        lewa.append(table[p])
        lewa += (quicksort(table[p+1 : high+1]))
        return lewa

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