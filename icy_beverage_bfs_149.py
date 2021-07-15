class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

visited = []
for i in range(n):
    visited.append([False] * m)

def bfs(point):
    count = 0
    queue = [point]
    flag = False
    while not len(queue) == 0:
        p = queue.pop()
        for j in range(4):
            x = p.x + dx[j]
            y = p.y = dy[j]
            if 0 <= x <= m and 0 <= y <= n and not visited[x][y]:
                visited[x][y] = True
                if graph[x][y] == 1:
                    queue.append(Point(x, y))
                    flag = True
    if flag:
        count += 1
    return count

visited[0][0] = True
result = 0
for k in range(m):
    for m in range(n):
        result += bfs(Point(k, m))

print(result)
