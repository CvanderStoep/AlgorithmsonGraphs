# Uses python3

import sys
import queue


# def bipartite(adj):
#     # write your code here
#     return -1
def change_color(color):
    if color == "black":
        color = "red"
    else:
        color = "black"
    return color


def bipartite(adj):
    number_vertices = len(adj)
    visited = [False] * number_vertices
    color = [None] * number_vertices
    q = queue.Queue()

    current_color = "black"
    for vertex in range(n):
        if not visited[vertex]:
            q.put(vertex)
            visited[vertex] = True
            color[vertex] = current_color
            while not q.empty():
                u = q.get()
                current_color = change_color(current_color)
                for v in adj[u]:
                    if color[u] == color[v]:
                        return 0  # is not bipartite
                    if not visited[v]:
                        color[v] = current_color
                        q.put(v)
                        visited[v] = True
    return 1


if __name__ == '__main__':
    input_data = sys.stdin.readline().strip()
    data = list(map(int, input_data.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))

#  4 4 1 2 4 1 2 3 3 1 -> 0 (not bipartite)
#  5 4 5 2 4 2 3 4 1 4 -> 1 (bipartite)
#  6 4 1 2 2 3 3 4 5 6 -> 1
#  10000 1 1595 7210 -> 1
