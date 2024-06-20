
# https://app.codesignal.com/arcade/graphs-arcade/in-the-pseudoforest/4neXxESSsRy92ghTD

def solution(n, wmap):
    adjList = buildAdjList(n, wmap)
    
    dfsmark = {k:(-1, 0) for k in range(n)}
    maxcount = {}
    for sn in range(n):
        if 0 <= dfsmark[sn][0] < sn:
            # already visited
            continue
        # print(f"{sn=}")
        maxcount[sn] = 1
        if not dfsNumBackedgesLTK(sn, -1, adjList, dfsmark, sn, maxcount):
             return False
             
    return True
    
def dfsNumBackedgesLTK(rn, pn, adjList, dfsmark, sn, maxcount):
    # print(f"{rn=} {pn=} {sn=}")
    if dfsmark[rn][0] == sn:
        assert False
    
    dfsmark[rn] = (sn, dfsmark.get(pn, (-1, 0))[1]+1)
    # print(f"{rn=} {adjList[rn]=}")
    for nb in adjList[rn]:
        # print(f"{nb=} {rn=} {pn=} {sn=}")
        if dfsmark[nb][0] != -1: 
            if dfsmark[nb][1] > dfsmark[rn][1]:
                continue
            if dfsmark[nb][1] == dfsmark[rn][1] - 1:
                continue 
            # print(f"* {nb=} {rn=} {sn=} {maxcount=}")
            maxcount[sn] -= 1
            if maxcount[sn] < 0:
                # print(f"FAIL {nb=} {rn=} {sn=} {maxcount=}")
                return False
            continue
        if not dfsNumBackedgesLTK(nb, rn, adjList, dfsmark, sn, maxcount):
            return False
    
    return True
        
def buildAdjList(n, wmap):
    adjList = {k:[] for k in range(n)}
    
    for e in wmap:
        n1, n2 = e
        if n2 not in adjList[n1]:
            adjList[n1].append(n2)
        if n1 not in adjList[n2]:
            adjList[n2].append(n1)
    
    return adjList
