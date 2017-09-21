# PS6-Q1

g = {"A":["B", "F", "E"], "B":["C", "F", "G"], "C":["D","G"], "D":["H", "G"], "E":["F"], "F":[], "G":["F", "H"], "H":[]}
weights = {"AB": 1, "AE": 4, "AF":8, "BC": 2, "BF": 6, "BG": 6, "CD":1, "CG":2, "DH":4, "DG":1, "EF":5, "GF":1, "GH":1}

def dijkstra(g, weights, start):
    # write your code here
    
    def initialize(g, start):
        keys = sorted(g.keys())
        for key in keys:
            distance[key] = float('inf')
        distance[start] = 0
    
    def relax(u, v):
        if distance[v] > distance[u] + weights[str(u) + str(v)]:
            distance[v] = distance[u] + weights[str(u) + str(v)]
            prev[v] = u
    
    def getMin():
        m = None
        for node in q:
            if m == None or distance[node] < distance[m]:
                m = node
        q.remove(m)
        return m
    
    distance = {}
    q = sorted(g.keys())
    seen = set()
    prev = {str(node) : None for node in g.keys()}
    
    initialize(g, start)
    
    while q:
        minNode = getMin()
        seen.add(minNode)
        for child in g[minNode]:
            if child not in seen:
                relax(minNode, child)
        print str(minNode)
        for node in sorted(distance.keys()):
            print str(node) + ": " + str(distance[node]) + " ",
        print
    
    for key in sorted(prev.keys()):
        print str(key) + ": " + str(prev[key]) + " ",
    print
    
    return distance
            
        
print dijkstra(g, weights, "A")