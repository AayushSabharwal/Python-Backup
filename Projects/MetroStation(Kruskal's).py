def parent(node):  # finds parent of node
    if parents[node] == node:
        return node

    parents[node] = parent(parents[node])
    return parents[node]


f = open("metro_cost_matrix.txt", "r")
cost_mat = []  # cost matrix
for line in f:
    cost_mat.append([int(x) for x in line.split()])
f.close()

n = len(cost_mat)  # number of nodes
cost_list = []  # list of tuples (a, b, cost) representing cost of edge joining a and b
for i in range(n):
    for j in range(n):
        if i > j:  # so we don't consider duplicate entries
            cost_list.append((i, j, cost_mat[i][j]))

cost_list.sort(key=lambda x: x[2])  # sorting by cost

parents = list(range(n))

edges = 0  # number of edges in our graph so far
net_cost = 0  # net cost of network
edges_in_graph = []  # list of edges in our final graph
while edges < n - 1:
    current = cost_list[0]  # current edge under consideration
    if parent(current[0]) != parent(current[1]):  # if the edge joins two disjoint subsets
        parents[current[0]] = parents[current[1]]
        net_cost += current[2]
        edges_in_graph.append(current)
        edges += 1

    cost_list = cost_list[1:]
print("net cost = ", net_cost)
for edge in edges_in_graph:
    print(edge)
print(parents)
