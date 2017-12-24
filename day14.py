import day10
import networkx as nx

if __name__=="__main__":
    key = "ffayrhll"
    count = 0
    g = nx.Graph()
    for i in range(128):
        h = day10.hash(key + '-' + str(i))
        bin_str = ''.join(['{0:0>4b}'.format(int(x, base=16)) for x in h])
        for j, c in enumerate(bin_str):
            if c == '1':
                count += 1
                g.add_node(128*i + j)
    for i in range(128):
        for j in range(128):
            if 128*i+j in g.nodes():
                if j < 127 and 128*i+j+1 in g.nodes():
                    g.add_edge(128*i+j, 128*i+j+1)
                if i < 127 and 128*(i+1)+j in g.nodes():
                    g.add_edge(128*i+j, 128*(i+1)+j)
    print(count)
    print(len(list(nx.connected_components(g))))
