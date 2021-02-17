# Uses python3

import sys


def number_of_components(adj):
    result = 0  # this is the number of connected components (CC)
    number_vertices = len(adj)
    visited = [False] * number_vertices

    def explore(vertex):
        visited[vertex] = True
        for neighbour in adj[vertex]:
            if not visited[neighbour]:
                explore(neighbour)

    for vertex in range(number_vertices):
        # keep exploring connected vertices until it stops, then add +1 to the CC
        if not visited[vertex]:
            explore(vertex=vertex)
            result += 1
    return result


def main():
    input_data = sys.stdin.readline().strip()
    # reads in the data as a single string separated with spaces
    # number vertices, number of edges, edge_1, edge_2, ... edge_n
    data = list(map(int, input_data.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))


if __name__ == '__main__':
    main()
