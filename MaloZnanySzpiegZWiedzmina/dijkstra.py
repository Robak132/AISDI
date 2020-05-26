def load(name):
    with open(name, "r") as file:
        fin_map = []
        for row in file.readlines():
            fin_map.append(list(row.strip()))
        return fin_map


if __name__ == "__main__":
    map = load("MaloZnanySzpiegZWiedzmina//mapa.txt")
    pass
