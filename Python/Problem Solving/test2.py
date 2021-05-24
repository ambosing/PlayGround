def dfs(g, r, visit):
    for k, v in g.items():
        if k not in visit:
            visit[k] = 0
            r.append("(")
            r.append(k)
            if g[k][1]
                dfs(g, r, visit)
            r.append(")")


def error(g):
    if error_1(g):
        return "E1"
    elif error_2(g):
        return "E2"
    return "No Error"


def error_1(g):
    for k, lst in g.items():
        if len(lst) > 2:
            return True
    return False


def error_2(g):
    for k, lst in g.items():
        s = set(lst)
        if len(lst) != len(s):
            return True
    return False


test_case = [('A', 'B'), ('A', 'C'), ('B', 'G'), ('C', 'H'), ('E', 'F'), ('B', 'D'), ('C', 'E')]

graph = {}
test_case.sort(key=lambda x: (x[0], x[1]))
root = ""
for t in test_case:
    if not root:
        root = t[0]
    if t[0] not in graph.keys():
        graph[t[0]] = [[], [t[1]]]
    else:
        graph[t[0]][1].append(t[1])
    if t[1] not in graph.keys():
        graph[t[1]] = [[t[0]], []]
    else:
        graph[t[1]][0].append(t[0])

route = []
dfs(graph, route, dict())
print(''.join(route))
