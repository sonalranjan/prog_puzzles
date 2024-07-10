
# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/ 
# lc 3203

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        g1, g2 = buildAdjList(edges1), buildAdjList(edges2)
        d1, _, _ = diameter(g1)
        d2, _, _ = diameter(g2)
        return max(d1, d2, (d1+1)//2 + (d2+1)//2 + 1)

def diameter(adjList):
    if not adjList:
        return 0, 0, 0
    v1, d = maxDepth(adjList, 0)
    v2, d = maxDepth(adjList, v1)
    return d, v1, v2

def buildAdjList(edges):
    if not edges:
        return {}
    n = len(edges) + 1 # because it is a tree
    adjList = {k:[] for k in range(n)}
    for e in edges:
        i, j = e[0], e[1]
        adjList[i].append(j)
        adjList[j].append(i)
    return adjList

def maxDepth(adjList, idx):
    n = len(adjList)
    bfs = [idx]
    visited = [0] * n
    visited[idx] = 1
    res, maxd = -1, -1
    for i in bfs:
        for j in adjList[i]:
            if visited[j] != 0:
                continue
            visited[j] = visited[i] + 1
            if visited[j] > maxd:
                res, maxd = j, visited[j]
            bfs.append(j)
    return res, maxd - 1



