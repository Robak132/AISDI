from random import randint
from timeit import timeit
import sys
sys.setrecursionlimit(20000)

class BinaryTreeError(Exception):
    pass 


class Node:
    def __init__(self, number):
        self.node_value = number
        self.number_of_copies = 1
        self.left = None  # Node
        self.right = None  # Node

    def __str__(self):
        return str(self.node_value)

    def add_new(self, number):
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
    def __init__(self, list_of_values = None):
        self.root = None
        if list_of_values != None:
            self.take_list(list_of_values)

    def take_list(self, list_of_values):
        for element in list_of_values:
            self.add_node(element)

    def add_node(self, number):
        if self.root is None:
            self.root = Node(number)
        else:
            self.root.add_new(number)

    def find_node(self, number):
        active_node = self.root
        while active_node.node_value != number:
            if active_node.right is None and active_node.left is None:
                return None
            if number > active_node.node_value:
                active_node = active_node.right
            else:
                active_node = active_node.left
        return active_node

    def show(self):
        print(self.root.show())

    def find_alot(self, list_of_values):
        for value in list_of_values:
            try:
                find_node(value)
            except:
                pass


class Pot():
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

    #def balance(self, counter = 0):
    #    self.root.


class AVLNode(Node):
    def __init__(self, number, father_node):
        super().__init__(number)
        self.thanos_value = 0
        self.father = father_node

    def add_new(self, number):
        if self.node_value == number:
            self.number_of_copies += 1
            return 0
        elif self.node_value < number:
            if self.right is not None:
                buff = self.right.add_new(number)
                self.thanos_value += buff
                if self.thanos_value == 0:
                    buff = 0 
                if abs(self.check_node_balance()) == 2:
                    buff = self.rotate()
                    self.father.balance()
                return buff
            else:
                self.right = AVLNode(number, self)
                self.thanos_value += 1
                if self.left is None:
                    return 1
                else:
                    return 0
        else:
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
        if self.left is None and self.right is None:
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
        return max(right_h, left_h)
            

    def rotate(self):
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
        right_left = right.left

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
    def __init__(self, list_of_values = None):
        root = None
        self.treepot = Pot(root)
        if list_of_values is not None:
            self.take_list(list_of_values)
        #for element in list_of_values:
        #    self.add_node(element)

    def add_node(self, number):
       # print(f"\n\nDODAWANIE: {number}")
        if self.treepot.root is None:
            self.treepot.root = AVLNode(number, self.treepot)
        else:
        #   print(f"Nasz root: {self.treepot.root}")
           self.treepot.root.add_new(number)
          # self.show()

    def find_node(self, number):
        active_node = self.treepot.root
        while active_node.node_value != number:
            if active_node.right is None and active_node.left is None:
                raise BinaryTreeError("Number not found")
            if number > active_node.node_value:
                active_node = active_node.right
            else:
                active_node = active_node.left
        return active_node

    def show(self):
        self.treepot.root.show()

class Testing():
    def __init__(self, precision = 1000, max_elements = 10000, number_of_repeats = 10):
        self.time_answer = []
        self.counter_table = []
        self.settings = {"precision": 1000, "max_elements": 10000, "number_of_repeats": 10}
        self.change_settings(precision, max_elements, number_of_repeats)
        self.new_counter_tab()
        self.max_random_elements = []
        self.calculate_mre()

    def calculate_mre(self):
        self.max_random_elements = [randint(1, self.settings["max_elements"]) for i in range(1, self.settings["max_elements"])]

    def load_object(self, class_type):
        obj = class_type(self.max_random_elements)
        print(obj.find_node(40))
        return obj

        
    def change_settings(self, precision = None, max_elements = None, number_of_repeats = None):
        if max_elements < 1 or precision < 1 or number_of_repeats < 1:
            raise ValueError
        if precision is not None:
            self.settings["precision"] = precision
        if precision is not None:
            self.settings["max_elements"] = max_elements
        if precision is not None:
            self.settings["number_of_repeats"] = number_of_repeats
        self.new_counter_tab()

    def new_counter_tab(self):
        self.counter_table = [i*self.settings["precision"] for i in range(1, int(self.settings["max_elements"]/self.settings["precision"])+1)]

    def clear_tables(self, answer_only = False):
        self.time_answer = []
        if not answer_only:
            self.counter_table = []

    def test_function(self, function, obj = None ):
        self.time_answer = []
        repeats_buff = self.settings["number_of_repeats"]
        if obj is not None:
            string_settings = f"from __main__ import {obj}\nfrom random import randint"
            function = f"{obj}.{function}"
        else:
            string_settings = f"from __main__ import {function}\nfrom random import randint"
        for test_elements in self.counter_table:
            print(f"Liczba elementów: {test_elements}/{self.settings['max_elements']}", end = "\t")
            average = []
            for repeat in range(repeats_buff):
                test_table = [randint(1, test_elements) for i in range(1, test_elements)]
                string_active = f"{function}({test_table})"
                #print(string_active)
                #print(string_settings)
                time = timeit(string_active, setup = string_settings, number = 1)
                #print(f"TIME: {time}")
                average.append(time)
            buff = sum(average)/len(average)
            self.time_answer.append(buff)
            print(f"time: {buff}")
        return self.counter_table, self.time_answer

    def save_to_file(self, name = "file"):
        if len(self.counter_table) != len(self.time_answer) or not len(self.counter_table) or not len(self.time_answer):
            raise ValueError
        with open(f"{name}.txt", 'w') as file:
            for element in self.counter_table:
                file.write(f"{element}, ")
            file.write("\n")
            for element in self.time_answer:
                file.write((f"{element}, "))


if __name__ == "__main__":
    _list = [randint(1, 10000) for i in range(1, 10000)]
    _listsegr = range(1,100)
    tablica_test = [10,7,12,5,8,11,13,4,6,2]
    tablica_okropna = [44,20,18,45,30,33]
    tablica_błaha = [3,2,1]

    #avltree = AVLTree(_list)
    #avltree.show()
    #print(_list)
    
    testcreating = Testing()
    print(testcreating.test_function("BinaryTree"))
    testcreating.save_to_file("BSTadding")
    print(testcreating.test_function("AVLTree"))
    testcreating.save_to_file("AVLadding")

    #testfinding = Testing(precision = 10000, max_elements = 300000)
    #object1 = testfinding.load_object(BinaryTree)
    #print(object1)
    #print(testfinding.test_function("find_alot", "object1"))
    #testfinding.save_to_file("FindingBST")
    #object2 = testfinding.load_object(AVLTree)
    #print(object2)
    #print(testfinding.test_function("find_alot", "object2"))
    #testfinding.save_to_file("FindingAVL")

    #objectto = AVLTree([_list])
    #timeit("objectto.find_alot", setup = "from __main__ import objectto")

    avltree = AVLTree(range(1,1000))
    print(timeit("avltree.find_node(999)", setup = "from __main__ import avltree", number = 10))
    bsttree = BinaryTree(range(1,1000))
    print(timeit("bsttree.find_node(999)", setup = "from __main__ import bsttree", number = 10))



