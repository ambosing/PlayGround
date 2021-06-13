def dfs(g, r, visit, a):
    for c in g[a][1]:
        if c not in visit:
            r.append("(")
            r.append(c)
            visit[c] = 0
            dfs(g, r, visit, c)
            r.append(")")


def error(g):
    if error_1(g):
        return "E1"
    elif error_2(g):
        return "E2"
    elif error_3(g):
        return "E3"
    elif error_4(g):
        return "E4"
    return "No Error"


def error_1(g):
    for k, lst in g.items():
        if len(lst[1]) > 2:
            return True
    return False


def error_2(g):
    for k, lst in g.items():
        s = set(lst[1])
        if len(lst[1]) != len(s):
            return True
    return False


def error_3(g):
    for k, lst in g.items():
        for i in lst[0]:
            if k == i:
                return True
        if len(lst[0]) >= 2:
            for key in lst[0]:
                if g[key][0]:
                    return True
    return False


def error_4(g):
    cnt = 0
    for k, lst in g.items():
        if not lst[0]:
            cnt += 1
    if cnt >= 2:
        return True
    return False


#test_case = [('A', 'B'), ('A', 'C'), ('B', 'G'), ('C', 'H'), ('E', 'F'), ('B', 'D'), ('C', 'E')]
#test_case = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('D', 'C')]
#test_case = [('B', 'D'), ('D', 'E'), ('A', 'B'), ('C', 'F'), ('E', 'G'), ('A', 'C')]
#test_case = [('A', 'B'), ('E', 'F'), ('A', 'C'), ('B', 'G'), ('C', 'H'), ('E', 'F'), ('B', 'D'), ('C', 'E')]
test_case = [('B', 'A'), ('B', 'B')]
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

error_code = error(graph)

if error_code == "No Error":
    route = ["(", root]
    dfs(graph, route, dict(), root)
    route.append(")")
    print(''.join(route))
else:
    print(error_code)
