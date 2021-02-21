import sys

"""checks a directed graph for cycles"""

# TODO check for a way to remove these global variable clock
# why is this not necessary for the other variables like visited; pre ; post

global clock
clock = 1


def acyclic2(adj):
    """checks whether the DAG contains cycles"""

    number_vertices = len(adj)
    visited = [False] * number_vertices
    pre = [0] * number_vertices
    post = [0] * number_vertices

    def previsit(v):
        global clock
        pre[v] = clock
        clock += 1

    def postvisit(v):
        global clock
        post[v] = clock
        clock += 1

    def explore(vertex):
        previsit(vertex)
        visited[vertex] = True
        for neighbour in adj[vertex]:
            if not visited[neighbour]:
                explore(neighbour)
        postvisit(vertex)

    for vertex in range(number_vertices):
        # keep exploring connected vertices until it stops
        if not visited[vertex]:
            explore(vertex=vertex)

    # for a DAG with edge u -> v; post(u) > post(v)
    for vertex in range(number_vertices):
        for neighbour in adj[vertex]:
            if post[neighbour] >= post[vertex]:
                return 1  # -> cycle detected
    return 0  # no cycle detected


def main():
    input_data = sys.stdin.readline().strip()
    # reads in the data as a single string separated with spaces
    # number vertices, number of edges, edge_1, edge_2, ... edge_n
    # outputs whether it is a DAG (return 0) or not a DAG (return 1)
    data = list(map(int, input_data.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic2(adj))


if __name__ == '__main__':
    main()
