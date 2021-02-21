import sys

"""checks a directed graph for cycles"""


def reach(adj, x, y):
    """checks whether two vertices in a graph are connected"""
    number_vertices = len(adj)
    # start by setting all the vertices as unvisited
    visited = [False] * number_vertices

    # explore all vertices recursively, starting with x
    def explore(vertex):
        visited[vertex] = True
        for neighbour in adj[vertex]:
            if not visited[neighbour]:
                explore(neighbour)

    explore(vertex=x)
    # if y is part of the visited vertices, then they are connected
    return visited[y]


def acyclic(adj):
    number_vertices = len(adj)
    for vertex1 in range(number_vertices):
        for vertex2 in range(vertex1 + 1, number_vertices):
            if reach(adj, vertex1, vertex2) and reach(adj, vertex2, vertex1):
                return 1  # if vertex 1 can be reaches from vertex 2 and vice versa -> cycle
    return 0  # no cycle detected


if __name__ == '__main__':
    input_data = sys.stdin.readline().strip()
    # input = sys.stdin.read()
    data = list(map(int, input_data.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))

# 4 4 1 2 4 1 2 3 3 1 -> 1 (cycle)
# 5 7 1 2 2 3 1 3 3 4 1 4 2 5 3 5 -> 0 (no cycle)
