from data_reader import read_data

data = read_data("rosalind_tree.txt").split("\n")
n = int(data.pop(0))
if data[-1] == "" : data.pop(-1)
edges = []
for info in data :
    edges.append(list(map(int,info.split(" "))))

num_edges = len(edges)
min_edges = n - 1 - num_edges

print(min_edges)
