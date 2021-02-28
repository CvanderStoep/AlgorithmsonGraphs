# Uses python3

import sys
import queue


def distance(adj, s, t):
    number_vertices = len(adj)
    visited = [False] * number_vertices
    max_distance = number_vertices  # maxdistance < N
    dist = [max_distance] * number_vertices
    q = queue.Queue()
    q.put(s)
    dist[s] = 0
    visited[s] = True

    while not q.empty():
        u = q.get()
        for v in adj[u]:
            if not visited[v]:
                q.put(v)
                dist[v] = dist[u] + 1
                visited[v] = True
    if dist[t] < max_distance:
        return dist[t]
    return -1


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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))

#  4 4 1 2 4 1 2 3 3 1 2 4 -> 2
#  5 4 5 2 1 3 3 4 1 4 3 5 -> -1 (not reachable)
#  9 13 1 9 1 2 2 3 3 4 4 3 4 5 6 5 6 7 8 6 7 8 7 9 9 6 7 3 1 6 -> 2
#  10000 1 1595 7210 500 501 -> -1
