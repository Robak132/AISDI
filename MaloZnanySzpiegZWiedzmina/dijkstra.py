import math


class Graph:
    def __init__(self, name):
        self.map = self.load(name)
        self.start, self.end = self.searchForZeros(self.map)

        self.basic_list = []
        self.distances = [[0, 0, 0, 0, 0] for i in range(len(self.map))] 
        for y in range(6):
            for x in range(6):
                self.distances[y][x] = Node(math.inf, y, x)
                if (x, y) == self.start:
                    self.distances[y][x].value = 0
                self.basic_list.append(self.distances[y][x])
        self.basic_list = sorted(self.basic_list)

        while len(self.basic_list) != 0:
            active_node = self.basic_list[0]
            for neighbour in self.findNeighbour(active_node):
                if (neighbour.value > active_node.value + int(self.map[neighbour.y][neighbour.x])) or math.isinf(neighbour.value):
                    neighbour.value = active_node.value + int(self.map[neighbour.y][neighbour.x])
                    neighbour.precursor = active_node

            self.basic_list.pop(0)
            self.basic_list = sorted(self.basic_list)

        x, y = self.end
        next_one = self.distances[y][x]
        coordinate_list = [(self.start[1], self.start[0])]
        # coordinate_list.append((active_node.y, active_node.x))
        # next_one = active_node.precursor
        while next_one.value != 0:
            coordinate_list.append((next_one.y, next_one.x))
            next_one = next_one.precursor
        for y in range(6):
            for x in range(6):
                if (y, x) in coordinate_list:
                    print(f"{self.map[y][x]}", end="")
                else:
                    print("•", end="")
            print("")
        print(coordinate_list)

    def findNeighbour(self, node):
        connections = []
        if node.y > 0:
            connections.append(self.distances[node.y - 1][node.x])
        if node.y < len(self.map[0]) - 1:
            connections.append(self.distances[node.y + 1][node.x])
        if node.x > 0:
            connections.append(self.distances[node.y][node.x - 1])
        if node.x < len(self.map) - 1:
            connections.append(self.distances[node.y][node.x + 1])
        return connections

    def load(self, name):
        with open(name, "r") as file:
            fin_map = []
            for row in file.readlines():
                fin_map.append(list(row.strip()))
            return fin_map

    def searchForZeros(self, twoDtab):
        answers_tab = []
        for y, row in enumerate(twoDtab):
            for x, elem in enumerate(row):
                if elem == "0":
                    answers_tab.append((x, y))
        return answers_tab


class Node:
    def __init__(self, value, y, x):
        self.value = value
        self.precursor = None
        self.y = y
        self.x = x

    def __repr__(self):
        return str(self.value)

    def __lt__(self, sth):
        return (self.value < sth.value)


if __name__ == "__main__":
    Graph("MaloZnanySzpiegZWiedzmina//mapa.txt")
    pass
