import math

class Graph:
    def __init__(name):
        self.map = self.load(name)
        self.start, self.end = self.searchForZeros(self.map)

        self.basic_list = []
        self.distances = [6][6]
        for y in range(6):
            for x in range(6):
                if (x, y == self.start):
                    self.distances[x][y] = Node(0, y, x)
                else:
                    self.distances[x][y] = Node(math.inf, y, x)
                basic_list.append(self.distances[x][y])

        while len(sorted(basic_list) != 0):
            active_node = basic_list[0]
            for neighbour in findNeighbour(active_node):
                if distances[neighbour.x][neighbour.y].value > distances[active_node.x][active_node.y].value + map[neighbour.x][neighbour.y]:
                    distances[neighbour.x][neighbour.y].value = distances[active_node.x][active_node.y].value + map[neighbour.x][neighbour.y]
                    for elem in basic_list:
                        if elem.x == neighbour.x and elem.y == neighbour.y:
                            elem.value = distances[active_node.x][active_node.y].value + map[neighbour.x][neighbour.y]
                    neighbour.precursor = active_node

            if active_node.x == self.end[0] and active_node.y == self.end[1]:
                break
            basic_list.pop(0)

    def findNeighbour(node):
        connections = []
        if node.y > 0:
            connections.append(twoDlist[node.y-1][node.x])
        if node.y < len(twoDlist[0])-1:
            connections.append(twoDlist[node.y+1][node.x])
        if node.x > 0:
            connections.append(twoDlist[node.y][node.x-1])
        if node.x < len(twoDlist)-1:
            connections.append(twoDlist[node.y][node.x+1])
        return connections

    def load(name):
        with open(name, "r") as file:
            fin_map = []
            for row in file.readlines():
                fin_map.append(list(row.strip()))
            return fin_map

    def searchForZeros(twoDtab):
        answers_tab = []
        for y, row in enumerate(twoDtab):
            for x, elem in enumerate(row):
                if elem == "0":
                    answers_tab.append((x,y))
        return answers_tab

class Node:
    def __init__(value, y, x):
        self.value = value
        self.precursor = None
        self.y = y
        self.x = x
        self.connections = []
        #self.visiblity = false

    def __str__():
        if self.visibility:
            return str(self.value)
        else:
            return ""
    
    def __repr__():
        return self.value



#def find_way(start, end):
#    pass
#    #nodes 

#def create_list(twoDtab, start):
#    queue = []



if __name__ == "__main__":
    Graph("MaloZnanySzpiegZWiedzmina//mapa.txt")
    pass



                
