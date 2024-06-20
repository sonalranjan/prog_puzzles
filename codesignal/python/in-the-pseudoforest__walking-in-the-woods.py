def solution(n, wmap):
    adjList = buildAdjList(n, wmap)
    dfsmark = {k:-1 for k in range(n)}
    
    for sn in range(n):
        if dfsmark[sn] >= 0 and dfsmark[sn] != sn:
            # visited during a dfs rooted at a lower node
            continue
        dfsAnnotate(sn, adjList, dfsmark, sn)
    # print(f"{adjList=} {dfsmark=}")
    return sum([True for rn in range(n) if dfsmark[rn] == rn])-1


def dfsAnnotate(rn, adjList, dfsmark, sn):
    if dfsmark[rn] == sn:
        return
    
    dfsmark[rn] = sn
    
    for nb in adjList[rn]:
        dfsAnnotate(nb, adjList, dfsmark, sn)
    
    return
    
    
def buildAdjList(n, wmap):
    adjList = {k:[] for k in range(n)}
    for e in wmap:
        n1, n2 = e
        if n2 not in adjList[n1]:
            adjList[n1].append(n2)
        if n1 not in adjList[n2]:
            adjList[n2].append(n1)
    return adjList
