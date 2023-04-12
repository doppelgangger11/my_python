from typing import List

class Solution:
    def canVisitAllRooms(self, adj_l: List[List[int]]) -> bool:
        s = 0
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
        if len(answer) != len(visited) or visited != [1] * len(adj_l):
            return False
        return True