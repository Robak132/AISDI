from random import randint
from timeit import timeit
import matplotlib.pyplot as plt

class Heap:
    """
    Stos maksymalny. Zaimplementowany na liście jednowymiarowej.
    """
    def __init__(self, init_table=None, branches=2):
        """
        Podczas tworzenia kopca w konstruktorze podajemy tablicę 
        z jakiej ma zrobić kopiec oraz ilość gałęzi na węzeł (domyślnie 2)
        """
        self.branches = branches
        self.values = [None]
        if init_table is not None:
            self.makeStack(init_table)

    def makeStack(self, table):               #Tworzy kopiec z listy
        for value in table:
            self.add(value)
            #print(f"DODAWANIE {value}")
            #self.show()
            #print("\n")

    def add(self, number):
        """
        Dodawanie elementu i kopcowanie 
        """
        if len(self.values) == 1:   # Jeśli dodawany jest pierwszy element to nie ma sensu kopcować
            self.values.append(number)
        else:
            child = len(self.values)
            self.values.append(number)
            const = (child+(self.branches-2))//self.branches    # Ojciec (adres) węzła umiejszczany jest w zmiennej const
            while self.values[child] > self.values[const]:  #Jeśli dodany element jest większy od ojca....
                temp = self.values[child]                   
                self.values[child] = self.values[const]     #To jest zamieniany miejscami
                self.values[const] = temp
                child = const
                const = (child+(self.branches-2))//self.branches    
                if const == 0:                              #Jeśli dotarliśmy do korzenia to przerywamy kopcowanie 
                    break

    def checkStack(self) -> bool:
        """
        Dla każdego z węzłów sprawdza czy węzły niżej są od niego mniejsze
        """
        for i in range(1, len(self.values)):
            node = self.values[i]
            for j in range(self.branches-1, -1, -1):
                if self.branches*i+1-j < len(self.values):
                    if node < self.values[self.branches*i+1-j]:
                        return False
        return True

        
    def show(self):
        """
        Dla każdego z węzłów pokazuje jego synów w konwencji:
        OJCIEC | SYN, SYN, ..., SYN
        """
        for i in range(1, len(self.values)):                                    #Czyli dla każdego węzła...
            print(f"Node: {self.values[i]:>4}\tBranches: ", end="")
            for j in range(self.branches-1, -1, -1):                            #...Bierzemy tyle węzłów ile z niego wychodzi... 
                if self.branches*i+1-j < len(self.values):
                    print(f"{self.values[self.branches*i+1-j]:>4} ", end="")    #... I dla każdego wypisujemy jego dane
                else:
                    print("None ", end="")
            print()

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
        self.counter_table = [i*self.settings["precision"] for i in range(1, int(self.settings["max_elements"]/self.settings["precision"])+1)]

    def clear_tables(self, answer_only=False):
        """
        Wymazuje tablice objektu. Jeśli answer_only, wymaże jedynie odpowiedzi.
        """
        self.time_answer = []
        if not answer_only:
            self.counter_table = []
            self.max_random_elements = []

    def test_function(self, function, obj=None, list_type="random", argument = None):
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
                if argument == None:
                    string_active = f"{function}({test_table})"
                else:
                    string_active = f"{function}({test_table}, {argument})"
                time = timeit(string_active, setup=string_settings, number=1)
                average.append(time)
            buff = sum(average)/len(average)
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

    def show_plot(self, label_string, save  = False):
        plt.plot(self.counter_table, self.time_answer)
        plt.title(label_string)
        plt.ylabel('Time of execution [s]')
        plt.xlabel('Number of elements')
        if save:
            plt.savefig(f"{label_string}.png")
        else:
            plt.show()


if __name__ == "__main__":
    #_list = [randint(1, 1000000) for i in range(1, 1000000)]
    #h = Heap(branches=3)
    #h.makeStack(_list)
    #print(h.checkStack())
    #h.show()

    testcreating2 = Testing(2000, 100000, 7)
    testcreating2.test_function("Heap")
    testcreating2.save_to_file("Heap_2")
    testcreating2.show_plot("Heap for 2 braches")

    testcreating3 = Testing(2000, 100000, 7)
    testcreating3.test_function("Heap",  argument = "branches = 3")
    testcreating3.save_to_file("Heap_3")
    testcreating3.show_plot("Heap for 3 braches")

    testcreating4 = Testing(2000, 100000, 7)
    testcreating4.test_function("Heap",  argument = "branches = 4")
    testcreating4.save_to_file("Heap_4")
    testcreating4.show_plot("Heap for 4 braches")



