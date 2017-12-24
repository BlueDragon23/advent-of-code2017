import networkx as nx

if __name__=="__main__":
    f = open("input12.txt")
    g = nx.Graph()
    for i in range(2000):
        g.add_node(i)
    for i, line in enumerate(f):
        _, connected = line.split(' <-> ')
        connected = [int(x) for x in connected.split(',')]
        for x in connected:
            g.add_edge(i, x)
    comps = list(nx.connected_components(g))
    for comp in comps:
        if 0 in comp:
            print(len(comp))

    print(len(comps))
