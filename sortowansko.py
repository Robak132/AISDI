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

