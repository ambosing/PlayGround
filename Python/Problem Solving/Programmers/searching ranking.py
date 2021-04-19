def query_parsing(queries):
    new_queries = []
    for query in queries:
        new_query = []
        query = query.split()
        for q in query:
            if q != "and":
                new_query.append(q)
        new_queries.append(new_query)
    return new_queries


def solution(infos, query):
    answer = []
    query = query_parsing(query)
    for q in query:
        cnt = 0
        for i in infos:
            info = i.split()
            for idx in range(5):
                if q[idx] == "-":
                    continue
                if idx < 4 and q[idx] != info[idx]:
                    break
                if idx == 4 and int(info[idx]) < int(q[idx]):
                    break
            else:
                cnt += 1
        answer.append(cnt)

    return answer