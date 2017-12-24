import networkx as nx
import matplotlib.pyplot as plt


class Program():
    def __init__(self, name, weight, above):
        self.name = name
        self.weight = weight
        self.above = above

def get_weight(g, v):
    if g.out_degree(v) == 0:
        # leaf node
        g.nodes[v]['total_weight'] = g.nodes[v]['weight']
        return
    total = 0
    w = 0
    error = False
    for u in g.successors(v):
        get_weight(g, u)
        total += g.nodes[u]['total_weight']
        if w == 0:
            w = g.nodes[u]['total_weight']
        elif w != g.nodes[u]['total_weight']:
            error = True
    g.nodes[v]['total_weight'] = total + g.nodes[v]['weight']
    if error:
        print('imbalance at {}'.format(v))
        print([(x, g.nodes[x]['total_weight']) for x in g.successors(v)])
        return

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
    
    get_weight(g, 'ahnofa')
    
