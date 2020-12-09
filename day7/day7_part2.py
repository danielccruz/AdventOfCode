import networkx as nx

G = nx.DiGraph()
for rule in [line.rstrip('\n') for line in open('input_file.txt')]:
    processing = rule.split(',')
    outside_bag = '_'.join(processing[0].split(' ')[0:2])
    # Processing
    for inside_bags in processing:
        inside_bags_aux = inside_bags.split(' ')[-4:-1]
        G.add_edge(outside_bag, inside_bags_aux[1] + '_' + inside_bags_aux[2], weight=inside_bags_aux[0])
        if inside_bags_aux[0].isdigit():
            G[outside_bag][inside_bags_aux[1] + '_' + inside_bags_aux[2]]['weight'] = inside_bags_aux[0]
        else:
            G[outside_bag][inside_bags_aux[1] + '_' + inside_bags_aux[2]]['weight'] = 0
        print(inside_bags_aux[0])


# Travessal
def count_bags(target):
    return sum(int(G.get_edge_data(target, sucessor)['weight']) *
               (1 + int(count_bags(sucessor))) for sucessor in
               G.successors(target))


print(count_bags('shiny_gold'))
