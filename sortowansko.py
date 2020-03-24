"""
AISDI - Zad 1
Jakub Robaczewski, Oskar Bartosz
"""


def bubblesort():
    pass


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