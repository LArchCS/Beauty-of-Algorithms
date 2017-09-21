# PS6-Q1

g = {"A":["C"], "B":["C"], "C":["D","E"], "D":["F"], "E":["F"], "F":["G", "H"], "G":[], "H":[]}

def topSort(graph):
    # write your code here
    def dfs(node):
        if node in seen:
            return
        print node, 
        seen.add(node)
        for child in sorted(graph[node]):
            dfs(child)
        topoSort.insert(0, node)
    topoSort = []
    seen = set()
    keys = sorted(graph.keys())
    for node in sorted(keys):
        if node not in seen:
            dfs(node)
    return topoSort

topSort(g)