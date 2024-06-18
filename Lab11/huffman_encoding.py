# Dany jest alfabet i częstość wystąpień każdego znaku w alfabecie

class Node:
    def __init__(self, freq, id):
        self.left = None
        self.right = None
        self.parent = None
        self.freq = freq
        self.id = id
        self.encoded = ""

def encode(S:list, F:list) -> list:
    n = len(S)
    oldN = n
    nodes = [Node(F[i], i) for i in range(n)]
    F = [(F[i], i) for i in range(n)]
    F.sort()
    
    while True:
        new = Node(nodes[F[0][1]].freq + nodes[F[1][1]].freq, n)
        new.left = nodes[F[0][1]]
        new.right = nodes[F[1][1]]
        nodes[F[0][1]].parent = new
        nodes[F[1][1]].parent = new
        nodes.append(new)
        F[1], F[-1] = F[-1], F[1]
        F.pop()
        F[0], F[-1] = F[-1], F[0]
        F.pop()
        F.append((new.freq, n))
        F.sort()
        n += 1
        if len(F) == 1: break

    current = nodes[F[0][1]]
    travel(current, "", oldN)
    
    result = [nodes[i].encoded for i in range(oldN)]
    return result

def travel(current:Node, data, n):
    if current.id < n:
        current.encoded += data
    if current.left != None:
        travel(current.left, data + "1", n)
    if current.right != None:
        travel(current.right, data + "0", n)

S = ['a', 'b', 'c', 'd', 'e']
F = [700, 200, 120, 300, 10]

print(encode(S, F))