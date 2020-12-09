import networkx as nx
import networkx.algorithms as algs

G = nx.DiGraph()
for rule in [line.rstrip('\n') for line in open('input_file.txt')]:
    processing = rule.split(',')
    outside_bag = '_'.join(processing[0].split(' ')[0:2])
    # Processing
    for inside_bags in processing:
        inside_bags_aux = inside_bags.split(' ')[-4:-1]
        G.add_edge(outside_bag, inside_bags_aux[1] + '_' + inside_bags_aux[2])

print(len(list(algs.ancestors(G, 'shiny_gold'))))
