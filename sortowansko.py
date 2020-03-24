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
    
        
def selectionsort():
    pass


def quicksort():
    pass


def load(file_name):
    with open(file_name, encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines() if line.strip() != ""]
        words = []
        for line in lines:
            words += line.split(" ")
        return words


if __name__ == "__main__":
    words = load("pan-tadeusz.txt")