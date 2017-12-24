import networkx as nx
import matplotlib.pyplot as plt

class Program():
    def __init__(self, name, weight, above):
        self.name = name
        self.weight = weight
        self.above = above

if __name__=="__main__":
    # Parse
    f = open("input7.txt")
    programs = []
    for line in f:
        parts = line.strip().split(' -> ')
        name, weight = parts[0].split(' ')
        weight = int(weight[1:-1])
        programs.append(Program(name, weight, [x.strip() for x in parts[1].split(',')] if len(parts) > 1 else []))
    g = nx.DiGraph()
    for program in programs:
        g.add_node(program.name, weight = program.weight)
    for program in programs:
        for p in program.above:
            g.add_edge(program.name, p)


    current = programs[1].name
    while (g.in_degree(current) > 0):
        current = list(g.predecessors(current))[0]
    print(current)
