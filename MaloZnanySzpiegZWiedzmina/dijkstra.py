import math


class Graph:
    def __init__(self, name):
        self.map = self.load(name)
        self.start, self.end = self.searchForZeros(self.map)

        self.basic_list = []
        self.distances = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        for y in range(6):
            for x in range(6):
                self.distances[x][y] = Node(math.inf, y, x)
                if (x, y) == self.start:
                    self.distances[x][y].value = 0
                self.basic_list.append(self.distances[x][y])

        while len(sorted(self.basic_list) != 0):
            active_node = self.basic_list[0]
            for neighbour in self.findNeighbour(active_node):
                if self.distances[neighbour.x][neighbour.y].value > self.distances[active_node.x][active_node.y].value + map[neighbour.x][neighbour.y]:
                    self.distances[neighbour.x][neighbour.y].value = self.distances[active_node.x][active_node.y].value + map[neighbour.x][neighbour.y]
                    for elem in self.basic_list:
                        if elem.x == neighbour.x and elem.y == neighbour.y:
                            elem.value = self.distances[active_node.x][active_node.y].value + map[neighbour.x][neighbour.y]
                    neighbour.precursor = active_node

            if active_node.x == self.end[0] and active_node.y == self.end[1]:
                coordinate_list = []
                coordinate_list.append(active_node.y, active_node.x)
                next_one = active_node.precursor
                while next_one != 0:
                    coordinate_list.append(next_one.y, next_one.x)
                    next_one = next_one.preprecursor
                break

            self.basic_list.pop(0)

        for y in range(6):
            for x in range(6):
                #if (y,x) in 
                pass

        



    def findNeighbour(self, node):
        connections = []
        if node.y > 0:
            connections.append(self.map[node.y-1][node.x])
        if node.y < len(self.map[0]) - 1:
            connections.append(self.map[node.y+1][node.x])
        if node.x > 0:
            connections.append(self.map[node.y][node.x-1])
        if node.x < len(self.map) - 1:
            connections.append(self.map[node.y][node.x+1])
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
                    answers_tab.append((x,y))
        return answers_tab


class Node:
    def __init__(self, value, y, x):
        self.value = value
        self.precursor = None
        self.y = y
        self.x = x
        self.connections = []
        #self.visiblity = false

    def __str__(self):
        if self.visibility:
            return str(self.value)
        else:
            return ""
    
    def __repr__(self):
        return self.value



#def find_way(start, end):
#    pass
#    #nodes 

#def create_list(twoDtab, start):
#    queue = []



if __name__ == "__main__":
    Graph("MaloZnanySzpiegZWiedzmina//mapa.txt")
    pass



                
