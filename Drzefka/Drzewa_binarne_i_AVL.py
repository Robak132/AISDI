from random import randint
from timeit import timeit
import sys
sys.setrecursionlimit(20000)


class BinaryTreeError(Exception):
    pass


class Node:
    """
    Klasa będąca najmniejszym elementem drzewa.
    Przechowuje informacje o swojej wartości oraz wskazuje na węzły wychodzące po lewej i po prawej
    """
    def __init__(self, number):
        self.node_value = number
        self.number_of_copies = 1
        self.left = None  # Node
        self.right = None  # Node

    def __str__(self):
        return str(self.node_value)

    def add_new(self, number):
        """
        Funkcja która szuka miejsca w które można wpisać nową wartość
        """
        if self.node_value == number:
            self.number_of_copies += 1
        elif self.node_value < number:
            if self.right is not None:
                self.right.add_new(number)
            else:
                self.right = Node(number)
        else:
            if self.left is not None:
                self.left.add_new(number)
            else:
                self.left = Node(number)

    def show(self):
        print(f"{str(self.left)}\t\t{self}({self.number_of_copies})\t\t{str(self.right)}")
        if self.left is not None:
            self.left.show()
        if self.right is not None:
            self.right.show()


class BinaryTree:
    """
    Drzewo Binarne.
    Działa na węzłach, jego podstawową jednostką którą przechowuje jest węzeł.
    Posiada wskaźnik na root, Czyli pierwszy węzeł drzewa.
    """
    def __init__(self, list_of_values = None):
        """
        Inicjalizowanie drzewa listą.
        Wartości z listy są do niego dodawane kolejno
        """
        self.root = None
        if list_of_values != None:
            self.take_list(list_of_values)

    def take_list(self, list_of_values):
        for element in list_of_values:
            self.add_node(element)

    def add_node(self, number):
        """
        Funkcja dodająca "number" do istniejącego już drzewa (self)
        Jeśli Drzewo jeszcze nie jest zaczęte, stworzy korzeń.
        """
        if self.root is None:
            self.root = Node(number)
        else:
            self.root.add_new(number)

    def find_node(self, number):
        """
        Funkcja zwracająca węzeł drzewa, który trzyma wartość "number"
        """
        active_node = self.root                                             # Przypisanie korzenia pod buff 
        while active_node.node_value != number:                             # Pętla trwa dopóki nie znajdzie węzła z "number"
            if active_node.right is None and active_node.left is None:      # Sygnalizuje brak elementu w drzewie przez zwrócenie "None"
                return None
            if number > active_node.node_value:
                active_node = active_node.right
            else:
                active_node = active_node.left
        return active_node

    def show(self):
        print(self.root.show())

    def find_alot(self, list_of_values):
        """
        Funkcja stworzona na potrzeby testu.
        Dostaje na wejście listę rzeczy które wyszukuje w drzewie.
        """
        for value in list_of_values:
                self.find_node(value)



class Pot():
    """
    Doniczka.
    Klasa której celem jest wkazywanie na korzeń w drzewie AVL. Dzięki tej klasie, po każdym obrocie drzewo prawidłowo rozpoznaje swój korzeń.
    Ma ona symulować Klasę AVLNode pod wzlględem metod, aby uogólnić zapis kodu (niewyodrębniać przyadków gdy działamy na root)
    """
    def __init__(self, root):
        self.root = root
        self.node_value = None

    def set_left(self, root):
        self.root = root

    def set_right(self, root):
        self.root = root

    def get_left(self):
        return self.root

    def get_right(self):
        return self.root

    def __repr__(self):
        return "None"


class AVLNode(Node):
    """
    Węzeł AVL.
    Rozbudowana wersja węzła BST.
    Przechowuje dodatkowo informacje o węźle z którego pochodzi, oraz informację o balansie węzła.
    """
    def __init__(self, number, father_node):
        super().__init__(number)
        self.thanos_value = 0
        self.father = father_node

    def add_new(self, number):
        """
        Funkcja realizująca dodawanie elementu do drzewa AVL, samopoprawiająca drzewo.
        Dzieli się na 3 etapy:
        - Dodawanie elementu na odpowiednie miejsce
        - Powiadamia węzły wyżej poprzez rekurencję o nowym Balansie
        - Jeśli dodanie węzła sprawiło że któryś węzeł jest niewyważony, uruchamia balansowanie drzewa
        """
        if self.node_value == number:                           # Przypadek w którym chcemy dodać wartość już znajdującą się w którymś z węzłów
            self.number_of_copies += 1
            return 0
        elif self.node_value < number:                          # Wybiera lewą gałąź jeśli "number" jest mniejszy od wartości węzła
            if self.right is not None:                          # Jeśli po prawej stronie już coś istnieje, przechodzi do węzła 
                buff = self.right.add_new(number)               # W drodze powrotej przesyłą informacje o balansie
                self.thanos_value += buff                       # Idealnie wyważone, tak jak wszystko powinno być
                if self.thanos_value == 0:                      # Jeśli nowo ustalony balans wyniósł zero, nie ma powodu wysyłać informacji wyżej, ponieważ dodanie element nie miało już wpływu na wyższe węzły 
                    buff = 0 
                if abs(self.check_node_balance()) == 2:         # Jeśli spowodowało to niewyważenie uruchamiane jest balansowanie
                    buff = self.rotate()
                    self.father.balance()                       # Po rotacji drzewo balansowane jest na nowo od miejsca zrotowanego
                return buff
            else:
                self.right = AVLNode(number, self)
                self.thanos_value += 1
                if self.left is None:
                    return 1
                else:
                    return 0
        else:                                                   # Wybiera prawą gałąź jeśli "number" jest mniejszy od wartości węzła (Kod dalej analogiczny, z drobnymi zmianami wynikającymi z przejścia na prawą)
            if self.left is not None:
                buff = self.left.add_new(number)
                self.thanos_value -= buff
                if self.thanos_value == 0:
                    buff = 0
                if abs(self.check_node_balance()) == 2:
                    buff = self.rotate()
                    self.father.balance()
                return buff
            else:
                self.left = AVLNode(number, self)
                self.thanos_value -= 1
                if self.right is None:
                    return 1
                else:
                    return 0

    def set_left(self, root):
        self.left = root

    def set_right(self, root):
        self.right = root

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def check_node_balance(self):
        return self.thanos_value

    def show(self):
        print(f"{str(self.left):<10}{str(self):>3}({str(self.number_of_copies):>3})[{self.thanos_value:>2}]{str(self.right):>10}\tNode Father: {str(self.father):>4}")
        if self.left is not None:
            self.left.show()
        if self.right is not None:
            self.right.show()

    def balance(self, counter = 0):
        """
        Funckja która liczy balans wszystkich węzłów od wybranego w dół.
        Uruchamia się jedynie po rotacjach.
        Liczy głębokość prawej i lewej strony, następnie liczy różnicę stanowiącą balans
        """
        if self.left is None and self.right is None:                # Jeśli to ostatni węzeł, zwróć wyżej głębokość counter
            self.thanos_value = 0
            return counter
        if self.left is not None:
            left_h = self.left.balance(counter + 1)
        else:
            left_h = counter
        if self.right is not None:
            right_h = self.right.balance(counter + 1)
        else:
            right_h = counter
        self.thanos_value = right_h - left_h
        return max(right_h, left_h)                                 # Wyżej podawana jest większa z głębokości 
            

    def rotate(self):
        """
        Komentarz który tak naprawdę tu istnieje, ale jeszcze nie.
        """
       # print("ROTACJA")
        if self.check_node_balance() == -2:
            if self.left.check_node_balance() == 1:
                self.rotate_left(self, self.left)
            self.rotate_right(self.father, self)
        elif self.check_node_balance() == 2:
            if self.right.check_node_balance() == -1:
                self.rotate_right(self, self.right)
            self.rotate_left(self.father, self)
        return 0

    def rotate_left(self, father, node):
        right = node.right
        right_left = right.left             # Wartość która tak naprawdę nie istnieje, ale jednak tak.

        right.set_left(node)
        if node is not None:
            node.father = right

        node.set_right(right_left)
        if right_left is not None:
            right_left.father = node

        if father.get_right() == node:
            father.set_right(right)
        else:
            father.set_left(right)

        if right is not None:
            right.father = father
        
    def rotate_right(self, father, node):
        left = node.left
        left_right = left.right

        left.set_right(node)
        if node is not None:
            node.father = left

        node.set_left(left_right)
        if left_right is not None:
            left_right.father = node

        if father.get_right() == node:
            father.set_right(left)
        else:
            father.set_left(left)

        if left is not None:
            left.father = father


class AVLTree(BinaryTree):
    """
    Drzewo AVL
    ROzbudowane drzewo Binarne, w którym różnica głębokości lewej i prawej gałęzi dla każdego węzła nie może być większa od 1
    """
    def __init__(self, list_of_values = None):
        root = None
        self.treepot = Pot(root)
        if list_of_values is not None:
            self.take_list(list_of_values)


    def add_node(self, number):
        """
        Analogiczne do BST.
        """
       # print(f"\n\nDODAWANIE: {number}")                  # Aby w konsoli zobaczyć proces tworzenia, należy odkomentować te trzy instrukcje
        if self.treepot.root is None:
            self.treepot.root = AVLNode(number, self.treepot)
        else:
        #   print(f"Nasz root: {self.treepot.root}")
           self.treepot.root.add_new(number)
          # self.show()

    def find_node(self, number):
        """
        Analogiczne do BST
        """
        active_node = self.treepot.root
        while active_node.node_value != number:
            if active_node.right is None and active_node.left is None:
                return None
            if number > active_node.node_value:
                active_node = active_node.right
            else:
                active_node = active_node.left
        return active_node

    def show(self):
        self.treepot.root.show()

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
    def __init__(self, precision = 1000, max_elements = 10000, number_of_repeats = 10):
        self.time_answer = []
        self.counter_table = []
        self.settings = {"precision": 1000, "max_elements": 10000, "number_of_repeats": 10}
        self.change_settings(precision, max_elements, number_of_repeats)
        self.new_counter_tab()
        self.max_random_elements = []
        self.calculate_mre()

    def calculate_mre(self, sorted = False):
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
        
    def change_settings(self, precision = None, max_elements = None, number_of_repeats = None):
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

    def new_counter_tab(self, sorted = False):
        """
        Tworzy nową counter_table, na podstawie settings
        """
        self.counter_table = [i*self.settings["precision"] for i in range(1, int(self.settings["max_elements"]/self.settings["precision"])+1)]

    def clear_tables(self, answer_only = False):
        """
        Wymazuje tablice objektu. Jeśli answer_only, wymaże jedynie odpowiedzi.
        """
        self.time_answer = []
        if not answer_only:
            self.counter_table = []
            self.max_random_elements = []

    def test_function(self, function, obj = None ,list_type = "random"):
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
        print(f"Obliczanie czasu: {function}")
        for test_elements in self.counter_table:
            print(f"Liczba elementów: {test_elements}/{self.settings['max_elements']}", end = "\t")
            average = []
            for repeat in range(repeats_buff):
                test_table=[]
                if list_type == "sorted":
                    test_table = range(1, test_elements)
                elif list_type == "random":
                    test_table = [randint(1, test_elements) for i in range(1, test_elements)]
                elif list_type == "memory":
                    test_table = self.max_random_elements[0:test_elements]
                string_active = f"{function}({test_table})"
                time = timeit(string_active, setup = string_settings, number = 1)
                average.append(time)
            buff = sum(average)/len(average)
            self.time_answer.append(buff)
            print(f"time: {buff}")
        return self.counter_table, self.time_answer

    def save_to_file(self, name = "file"):
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
                file.write((f"{element};"))


if __name__ == "__main__":
    _list = [randint(1, 10000) for i in range(1, 10000)]
    _listsegr = range(1,100)
    tablica_okropna = [44,20,18,45,30,33]           # Do sprawdzenia obrotu lewo-prawego
    tablica_błaha = [3,2,1]                         

    #avltree = AVLTree(_list)                       # Dwie linie kodu wygenerują i wypiszą drzewo AVL
    #avltree.show()
    
    ##Testowanie tworzenia BST i AVL
    #testcreating = Testing()
    #print(testcreating.test_function("BinaryTree"))
    #testcreating.save_to_file("BSTadding")
    #print(testcreating.test_function("AVLTree"))
    #testcreating.save_to_file("AVLadding")

    ##Testowanie szukania BST i AVL
    #testfinding = Testing(precision = 10000, max_elements = 200000)
    #object1 = testfinding.load_object(BinaryTree)
    #print(testfinding.test_function("find_alot", "object1", list_type = "memory"))
    #testfinding.save_to_file("FindingBST")
    #object2 = testfinding.load_object(AVLTree)
    #print(testfinding.test_function("find_alot", "object2", list_type = "memory"))
    #testfinding.save_to_file("FindingAVL")

    ##Testowanie tworzenia BST i AVL (pesymistyczne)
    #testcreatingpesimistic = Testing(precision = 100, max_elements = 1000)
    #print(testcreatingpesimistic.test_function("BinaryTree", list_type = "sorted"))
    #testcreatingpesimistic.save_to_file("BSTadding_psm")
    #print(testcreatingpesimistic.test_function("AVLTree", list_type = "sorted"))
    #testcreatingpesimistic.save_to_file("AVLadding_psm")

    #Testowanie szukania BST i AVL (pesymistyczne)
    testfindingpesimistic = Testing(precision = 100, max_elements = 1000)
    testfindingpesimistic.calculate_mre(sorted = True)
    object1 = testfindingpesimistic.load_object(BinaryTree)
    print(testfindingpesimistic.test_function("find_alot", "object1", list_type = "memory"))
    testfindingpesimistic.save_to_file("FindingBST_psm")
    object2 = testfindingpesimistic.load_object(AVLTree)
    print(testfindingpesimistic.test_function("find_alot", "object2", list_type = "memory"))
    testfindingpesimistic.save_to_file("FindingAVL_psm")

    #objectto = AVLTree([_list])
    #timeit("objectto.find_alot", setup = "from __main__ import objectto")




