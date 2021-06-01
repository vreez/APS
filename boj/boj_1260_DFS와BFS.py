import sys; sys.stdin = open("1260.txt", "r")
from collections import deque

def dfs(graph, V, visited):
    visited[V] = True
    arr1.append(str(V))
    # print(V, end=' ')
    for i in graph[V]:
        if visited[i] == False:
            dfs(graph, i, visited)

def bfs(graph, V, visited):
    queue = deque([V])
    visited[V] = True
    while queue:
        node = queue.popleft()
        arr2.append(str(node))
        # print(node, end=' ')
        for i in graph[node]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(N+1):
    graph[i] = sorted(graph[i])
arr1 = []
arr2 = []
dfs(graph, V, visited)
print(' '.join(arr1))
visited = [False for _ in range(N + 1)]
bfs(graph, V, visited)
print(' '.join(arr2))