# PS6-Q1

g = {"A":["B", "F"], "B":["C", "E"], "C":["D"], "D":["B", "H"], "E":["D"], "F":["E", "G"], "G":["F"], "H":["G"]}

def dfs(g, start, seen):
    if not start:
        return
    print start,
    seen.add(start)
    for child in g[start]:
        if child not in seen:
            dfs(g, child, seen)

dfs(g, "A", set())