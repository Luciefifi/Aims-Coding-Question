def parse_network(input_network: str):
    lines = input_network.strip().split('\n')
    network = []
    for line in lines:
        row = line.split(',')
        network.append([int(cost) if cost and cost != '-' else float('inf') for cost in row])
    return network

def maximum_spanning_tree(network):
    num_nodes = len(network)
    max_spanning_tree = [0] * num_nodes
    max_spanning_tree[0] = float('inf')
    visited = [False] * num_nodes

    for _ in range(num_nodes):
        max_cost = 0
        u = -1

        for node in range(num_nodes):
            if not visited[node] and max_spanning_tree[node] > max_cost:
                u = node
                max_cost = max_spanning_tree[node]

        visited[u] = True

        for v in range(num_nodes):
            if not visited[v] and network[u][v] > max_spanning_tree[v]:
                max_spanning_tree[v] = network[u][v]

    total_cost = sum(sum(cost for cost in row if cost != float('inf')) for row in network)
    spanning_tree_cost = sum(cost for cost in max_spanning_tree if cost != float('inf'))

    max_saving = total_cost - spanning_tree_cost
    return max_saving

input_network = '''-,14,10,19,-,-,-
14,-,-,15,18,-,-
10,-,-,26,,29,-
19,15,26,-,16,17,21
-,18,-,16,-,-,9
-,-,29,17,-,-,25
-,-,-,21,9,25,-
'''

max_saving = maximum_spanning_tree(parse_network(input_network))
print(max_saving)
