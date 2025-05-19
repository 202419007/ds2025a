class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


G1 = Graph(4)
G2 = Graph(4)

# 0 == A, 1 == B, 2 == C, 3 == D  # ';'은 한줄로 연결하려고
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print("G2 무방향 그래프")
for r in range(G2.SIZE):
    for c in range(G2.SIZE):
        print(G2.graph[r][c], end=' ')
    print()

# 0 == A, 1 == B, 2 == C, 3 == D
G2.graph[0][1] = 1; G2.graph[0][2] = 1
G2.graph[3][0] = 1; G2.graph[3][2] = 1