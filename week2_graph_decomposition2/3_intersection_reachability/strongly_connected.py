# Uses python3

import sys

sys.setrecursionlimit(200000)


def dfs(adj):
    """returns the number of strongly connected components in a directed graph"""

    number_vertices = len(adj)
    visited = [False] * number_vertices
    pre = [0] * number_vertices
    post = [0] * number_vertices
    clock = 1

    def previsit(v):
        nonlocal clock
        pre[v] = clock
        clock += 1

    def postvisit(v):
        nonlocal clock
        post[v] = clock
        clock += 1

    def explore(vertex):
        # previsit(vertex)
        visited[vertex] = True
        for neighbour in adj[vertex]:
            if not visited[neighbour]:
                explore(neighbour)
        postvisit(vertex)

    for vertex in range(number_vertices):
        # keep exploring connected vertices until it stops
        if not visited[vertex]:
            explore(vertex=vertex)

    # returns the ordered indices
    order = []
    for vertex in range(number_vertices, 0, -1):
        order.append(post.index(vertex))
    return order


def number_of_strongly_connected_components(adj):
    result = 0  # this is the number of strongly connected components (SCC)
    number_vertices = len(adj)
    visited = [False] * number_vertices

    def explore(vertex):
        visited[vertex] = True
        for neighbour in adj[vertex]:
            if not visited[neighbour]:
                explore(neighbour)

    #  run DFS on the reverse Graph
    adjR = [[] for _ in range(n)]
    for vertex in range(n):
        for neighbour in adj[vertex]:
            adjR[neighbour].append(vertex)
    order = dfs(adjR)

    #  run DFS again on Graph in reverse postorder obtained from previous DFS(Graph Reverse)
    for v in order:
        if not visited[v]:
            explore(v)
            result += 1  # adds one to the number of SCC
    return result


if __name__ == '__main__':
    input_data = sys.stdin.readline().strip()
    data = list(map(int, input_data.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))

#  4 3 1 2 2 3 3 4 -> 4
#  4 4 1 2 4 1 2 3 3 1 -> 2
#  5 7 2 1 3 2 3 1 4 3 4 1 5 2 5 3 -> 5
#  9 13 1 9 1 2 2 3 3 4 4 3 4 5 6 5 6 7 8 6 7 8 7 9 9 6 7 3 -> 5
#  10000 1 1595 7210 -> 10000
