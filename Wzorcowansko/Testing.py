import matplotlib.pyplot as plt
import timeit
from random import randint


class Testing():
    """
    Klasa Testująca.
    Pozwala na zmierzenie czasu funkcji lub metody klasy
    Atrybuty:
    - time_answer - Przechowuje tablice czasu po uruchomieniu testowania
    - counter_table - Liczona na podstawie settings. Przechowuje kolejne liczby elementów do testowania.
    - setting - Słownik: precision to co ile elementów liczyć; max_elements to do ilu elementów liczyć; number_of_repeats to ilość testów do wykonania dla pojedyńczego przypadków, z których poiliczy średnią
    - max_random_elements - tablica trzymająca tyle liczb ile mówi max_elements.
    """
    def __init__(self, precision=1000, max_elements=10000, number_of_repeats=10):
        self.time_answer = []
        self.counter_table = []
        self.settings = {"precision": 1000, "max_elements": 10000, "number_of_repeats": 10}
        self.change_settings(precision, max_elements, number_of_repeats)
        self.new_counter_tab()
        self.max_random_elements = []
        self.calculate_mre()

    def calculate_mre(self, sorted=False):
        """
        Tworzy nową max_random_elements.
        Jeśli flaga sorted, stworzy posortowaną listę
        Jeśli nie, będą to losowe wartości
        """
        if sorted:
            self.max_random_elements = range(1, self.settings["max_elements"])
        else:
            self.max_random_elements = [randint(1, self.settings["max_elements"]) for i in range(1, self.settings["max_elements"])]

    def load_object(self, class_type):
        """
        Tworzy objekt wybranej klasy, ładując do niego wartości z max_random_elements
        """
        obj = class_type(self.max_random_elements)
        return obj

    def change_settings(self, precision=None, max_elements=None, number_of_repeats=None):
        """
        Zmienia ustawienia
        """
        if max_elements < 1 or precision < 1 or number_of_repeats < 1:
            raise ValueError
        if precision is not None:
            self.settings["precision"] = precision
        if precision is not None:
            self.settings["max_elements"] = max_elements
        if precision is not None:
            self.settings["number_of_repeats"] = number_of_repeats
        self.new_counter_tab()

    def new_counter_tab(self, sorted=False):
        """
        Tworzy nową counter_table, na podstawie settings
        """
        self.counter_table = [i * self.settings["precision"] for i in range(1, int(self.settings["max_elements"] / self.settings["precision"]) + 1)]

    def clear_tables(self, answer_only=False):
        """
        Wymazuje tablice objektu. Jeśli answer_only, wymaże jedynie odpowiedzi.
        """
        self.time_answer = []
        if not answer_only:
            self.counter_table = []
            self.max_random_elements = []

    def test_function(self, function, obj=None, list_type="random", argument=None):
        """
        Klasa licząca czas wykonania "function"
        Jeśli "function" jest metodą klasy, należy jako arg "obj" podać objekt tej Klasy.
        Funkcja jest testowana za pomocą różnych typów list: (list_type)
        - random - Losowa lista z każdym obiegiem pętli
        - memory - Kolejne n elementów z listy w pamięci (max_random_elements)
        - sorted - Posortowane rosnąco n liczb
        Zmienna n to kolejne elementy listy counter_table.
        """
        self.time_answer = []
        repeats_buff = self.settings["number_of_repeats"]
        if obj is not None:
            string_settings = f"from __main__ import {obj}\nfrom random import randint"
            function = f"{obj}.{function}"
        else:
            string_settings = f"from __main__ import {function}\nfrom random import randint"
        print(f"Obliczanie czasu: {function}\t\tdodatkowe argumenty: ({argument})")
        for test_elements in self.counter_table:
            print(f"Liczba elementów: {test_elements}/{self.settings['max_elements']}", end="\t")
            average = []
            for repeat in range(repeats_buff):
                test_table = []
                if list_type == "sorted":
                    test_table = range(1, test_elements)
                elif list_type == "random":
                    test_table = [randint(1, test_elements) for i in range(1, test_elements)]
                elif list_type == "memory":
                    test_table = self.max_random_elements[0:test_elements]
                if argument is None:
                    string_active = f"{function}({test_table})"
                else:
                    string_active = f"{function}({test_table}, {argument})"
                time = timeit(string_active, setup=string_settings, number=1)
                average.append(time)
            buff = sum(average) / len(average)
            self.time_answer.append(buff)
            print(f"time: {buff}")
        return self.counter_table, self.time_answer

    def save_to_file(self, name="file"):
        """
        Zapisywanie do pliku dwóch tablic, counter_table oraz time_answer
        """
        if len(self.counter_table) != len(self.time_answer) or not len(self.counter_table) or not len(self.time_answer):
            raise ValueError
        with open(f"{name}.txt", 'w') as file:
            for element in self.counter_table:
                file.write(f"{element};")
            file.write("\n")
            for element in self.time_answer:
                element = str(element).replace(".", ",")
                file.write((f"{element};"))

    def show_plot(self, label_string, save=False):
        plt.plot(self.counter_table, self.time_answer)
        plt.title(label_string)
        plt.ylabel('Time of execution [s]')
        plt.xlabel('Number of elements')
        if save:
            plt.savefig(f"{label_string}.png")
        else:
            plt.show()
