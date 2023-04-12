def bfs(adj_l, s):
    visited = [0] * len(adj_l)
    visited[s] += 1
    queue = [s]
    answer = []

    while queue != []:
        s = queue.pop(0)
        answer.append(s)
        for v in adj_l[s]:
            if visited[v] == 0:
                queue.append(v)
                visited[v] = 1
    return answer

adj_l_1 = {
    0:[1, 2],
    1:[0, 2],
    2:[0, 1, 3],
    3:[2, 4, 5],
    4:[3, 5],
    5:[3, 4]
}

adj_l_2 = {
    0:[],
    1:[2],
    2:[1]
}

print(bfs(adj_l_2, 0))


assert bfs(adj_l_1, 0) == [0, 1, 2, 3, 4, 5]
assert bfs(adj_l_1, 1) == [1, 0, 2, 3, 4, 5]
assert bfs(adj_l_1, 3) == [3, 2, 4, 5, 0, 1]
assert bfs(adj_l_1, 5) == [5, 3, 4, 2, 0, 1]
