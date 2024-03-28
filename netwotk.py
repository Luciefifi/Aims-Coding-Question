import heapq

def maximum_saving(input_network: str) -> int:
    # Parse the input network
    network = []
    for row in input_network.strip().split('\n'):
        row_values = []
        for value in row.split(','):
            try:
                row_values.append(int(value))
            except ValueError:
                row_values.append(-1)
        network.append(row_values)
    n = len(network)

    # Prim's algorithm
    start_node = 0
    visited = [False] * n
    mst_cost = 0
    total_cost = sum(network[i][j] for i in range(n) for j in range(i + 1, n) if network[i][j] != -1)
    heap = [(0, start_node)]  # (cost, node)

    while heap:
        cost, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        mst_cost += cost

        for v in range(n):
            if network[u][v] != -1 and not visited[v]:
                heapq.heappush(heap, (network[u][v], v))

    return total_cost - mst_cost

# Test case
input_network = '''-,14,10,19,-,-,-
14,-,-,15,18,-,-
10,-,-,26,,29,-
19,15,26,-,16,17,21
-,18,-,16,-,-,9
-,-,29,17,-,-,25
-,-,-,21,9,25,-
'''
max_saving = maximum_saving(input_network)
print(max_saving)  # Output: 138