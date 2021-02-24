# Uses python3

import sys


def dfs(adj):
    """return the post-order indices"""

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


if __name__ == '__main__':
    input_data = sys.stdin.readline().strip()
    data = list(map(int, input_data.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = dfs(adj)

    for x in order:
        print(x + 1, end=' ')

#  4 3 1 2 4 1 3 1 -> 4 3 1 2
#  4 1 3 1 -> 2 3 1 4
#  5 7 2 1 3 2 3 1 4 3 4 1 5 2 5 3 -> 5 4 3 2 1
