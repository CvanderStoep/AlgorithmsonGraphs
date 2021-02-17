import sys


def reach(adj, x, y):
    number_vertices = len(adj)
    visited = [False] * number_vertices

    def explore(vertex):
        visited[vertex] = True
        for neighbour in adj[vertex]:
            if not visited[neighbour]:
                explore(neighbour)

    explore(vertex=x)
    # print(visited)
    return visited[y]


def main():
    input_data = sys.stdin.readline().strip()

    data = list(map(int, input_data.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))


if __name__ == '__main__':
    main()
