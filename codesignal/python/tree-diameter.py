

# https://app.codesignal.com/arcade/graphs-arcade/in-the-pseudoforest/Sby2j4SHqDncwyQjh

def solution(n, tree):
    adjList = buildAdjList(n, tree)
    # print(adjList, len(adjList))
    d, _, _ = diameter(adjList)
    return d
        
def diameter(adjList):
    if not adjList:
        return 0, 0, 0
    minv = min(adjList.keys())
    v1, d = maxDepth(adjList, minv)
    v2, d = maxDepth(adjList, v1)
    # print(d, v1, v2)
    return d, v1, v2

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

def buildAdjList(n, edges):
    if not edges:
        return {}
    assert n == len(edges) + 1 # because it is a tree
    adjList = {k:[] for k in range(n)}
    for e in edges:
        i, j = e[0], e[1]
        adjList[i].append(j)
        adjList[j].append(i)
    return adjList



