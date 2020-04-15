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


class AVLNode(Node):
    def __init__(self, number, layer=1):
        super().__init__(number)
        self.thanos_value = 0
        self.layer = layer

    def add_new(self, number):
        if self.node_value == number:
            self.number_of_copies += 1
            return 0
        elif self.node_value < number:
            if self.right is not None:
                buff = self.right.add_new(number)
                if self.right.check_node_balance() == -2:
                    print("ROTACJAAAAA PRAWA")
                    self.rotate_right(self, self.right)
                    return 0
                elif self.right.check_node_balance() == 2:
                    print("ROTACJAAAAA LEWA")
                    self.rotate_left(self, self.right)
                    return 0
                self.thanos_value += buff
                return buff
            else:
                self.right = AVLNode(number)
                self.thanos_value += 1
                if self.left is None:
                    return 1
                else:
                    return 0
        else:
            if self.left is not None:
                buff = self.left.add_new(number)
                if self.left.check_node_balance() == -2:
                    print("ROTACJAAAAA PRAWA")
                    self.rotate_right(self, self.left)
                    return 0
                elif self.left.check_node_balance() == 2:
                    print("ROTACJAAAAA LEWA")
                    self.rotate_left(self, self.left)
                    return 0
                self.thanos_value -= buff
                return buff
            else:
                self.left = AVLNode(number)
                self.thanos_value -= 1
                if self.right is None:
                    return 1
                else:
                    return 0

    def check_node_balance(self):
        return self.thanos_value

    def show(self):
        print(f"{str(self.left):<10}{str(self):>3}({self.number_of_copies:2})[{self.thanos_value:2}]{str(self.right):>10}")
        if self.left is not None:
            self.left.show()
        if self.right is not None:
            self.right.show()

    def rotate_left(self, father, node):
        # print(f"Father: {father}")
        # print(f"Son: {node}")
        right = node.right
        right_left = right.left

        right.left = node
        node.right = right_left
        
        if father.right == node:
            father.right = right
        else:
            father.left = right

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
        
        left.right = node
        node.left = left_right

        if father.right == node:
            father.right = left
        else:
            father.left = left
        
        node.thanos_value = 0
        if left is not None:
            left.thanos_value = 0
        if left_right is not None:
            left_right.thanos_value = 0

class Flowerpot():
    def __init__(self):
        self.left = None

    def set_root(self, root):
        self.left = root

    def get_root(self):
        return self.left

class AVLTree(BinaryTree): # Dodać doniczkę
    def add_node(self, number):
        print(f"\n\nDODAWANIE: {number}")
        if self.root is None:
            self.root = AVLNode(number)
        else:
            self.root.add_new(number)
            self.root.show()

    def perfectly_balanced():
        pass

    def as_all_things_should_be():
        pass

if __name__ == "__main__":
    _list = [randint(1, 10) for i in range(1, 10)]
    # print(_list)
    tablica_rosnaca = [1,2,3,4,5,6,7,8,9,10]
    tablica_test = [1,2,3]
    # tree = BinaryTree(_list)
    # tree.show()

    avltree = AVLTree(tablica_test)
 #   avltree.show()
   # print(f"Root: {avltree.flowerpot.right}")

    #print(tree.find_node(11))