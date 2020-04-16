from random import randint

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
    def __init__(self, list_of_values):
        self.root = None
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
                raise BinaryTreeError("Number not found")
            if number > active_node.node_value:
                active_node = active_node.right
            else:
                active_node = active_node.left
        return active_node

    def show(self):
        print(self.root.show())


class Pot():
    def __init__(self, root):
        self.root = root

    def set_left(self, root):
        self.root = root

    def set_right(self, root):
        self.root = root

    def get_left(self):
        return self.root

    def get_right(self):
        return self.root


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
                if self.right.check_node_balance() == -2:
                    print("ROTACJAAAAA PRAWA 1")
                    self.rotate_right(self, self.right)
                    return 0
                elif self.right.check_node_balance() == 2:
                    print("ROTACJAAAAA LEWA 1")
                    self.rotate_left(self, self.right)
                    return 0
                self.thanos_value += buff
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
                if self.left.check_node_balance() == -2:
                    print("ROTACJAAAAA PRAWA 2")
                    self.rotate_right(self, self.left)
                    return 0
                elif self.left.check_node_balance() == 2:
                    print("ROTACJAAAAA LEWA 2")
                    self.rotate_left(self, self.left)
                    return 0
                self.thanos_value -= buff
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
        print(f"{str(self.left):<10}{str(self):>3}({self.number_of_copies:2})[{self.thanos_value:2}]'{str(self.father):2}'{str(self.right):>10}")
        if self.left is not None:
            self.left.show()
        if self.right is not None:
            self.right.show()

    def rotate_left(self, father, node):
        # print(f"Father: {father}")
        # print(f"Son: {node}")
        right = node.right
        right_left = right.left

        right.set_left(node)
        node.set_right(right_left)
        
        if father.get_right() == node:
            father.set_right(right)
        else:
            father.set_left(right)

        node.thanos_value = 0
        if right is not None:
            right.thanos_value = 0
        if right_left is not None:
            right_left.thanos_value = 0

    def rotate_right(self, father, node):
        # print(f"Father: {father}")
        # print(f"Son: {node}")
        left = node.left
        left_right = left.right
        
        left.set_right(node)
        node.set_left(left_right)

        if father.get_right() == node:
            father.set_right(left)
        else:
            father.set_left(left)
        
        node.thanos_value = 0
        if left is not None:
            left.thanos_value = 0
        if left_right is not None:
            left_right.thanos_value = 0

class AVLTree(BinaryTree): # Dodać doniczkę
    def __init__(self, list_of_values):
        root = None
        self.treepot = Pot(root)
        for element in list_of_values:
            self.add_node(element)

    def add_node(self, number):
        print(f"\n\nDODAWANIE: {number}")
        if self.treepot.root is None:
            self.treepot.root = AVLNode(number, self.treepot)
        else:
            self.treepot.root.add_new(number)
            self.treepot.root.show()

    def perfectly_balanced():
        pass

    def as_all_things_should_be():
        pass

if __name__ == "__main__":
    _list = [randint(1, 10) for i in range(1, 10)]
    # print(_list)
    tablica_rosnaca = [1,2,3,4,5,6,7,8,9,10]
    tablica_test = [5,2,6,1,3,8,7]
    # tree = BinaryTree(_list)
    # tree.show()

    avltree = AVLTree(tablica_test)
 #   avltree.show()
   # print(f"Root: {avltree.flowerpot.right}")

    #print(tree.find_node(11))