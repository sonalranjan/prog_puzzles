

# https://app.codesignal.com/arcade/python-arcade/showing-class/CY8Hj6M5FxBsyFT7D

class Team(object):
    def __init__(self, names):
        self.names = names
        self.adjList = self.buildAdjList()
        
    def buildAdjList(self):
        flmaps = {}; llmaps = {}
        for idx, n in enumerate(self.names):
            fl, ll = n[0].lower(), n[-1].lower()
            if fl not in flmaps:
                flmaps[fl] = set()
            flmaps[fl].add(idx)
            if ll not in llmaps:
                llmaps[ll] = set()
            llmaps[ll].add(idx)
        
        adjList = {k:set() for k in range(len(self.names))}
        for idx, n in enumerate(self.names):
            fl, ll = n[0].lower(), n[-1].lower()
            for i in llmaps.get(fl, set()):
                # create an edge from any names whose last letter = fl
                adjList[i].add(idx)
            for i in flmaps.get(ll, set()):
                # create an edge from any names whose first letter = ll
                adjList[idx].add(i)
        return adjList
    
    def dfsHelper(self, idx, visited):
        if visited[idx]: 
            return visited
            
        visited[idx] = True # dfs
            
        for i in self.adjList[idx]:
            if visited[i]:
                continue
            visited = self.dfsHelper(i, visited)
        
        if False not in visited: # dfs termination
            return visited
            
        visited[idx] = False # backtrack
        
        return visited
        
    def __bool__(self):
        l = len(self.names) 
        if l <= 1:
            return True
        # print(self.adjList)
        sortedL = sorted([(len(self.adjList[idx]), idx) for idx in self.adjList.keys() if len(self.adjList[idx]) > 0], reverse=True)
        for _,i in sortedL:
            visited = [False]*len(self.names)
            visited = self.dfsHelper(i, visited)
            # print(i, self.names[i], visited)
            if False not in visited:
                return True
        
        return False

def solution(team):
    return bool(Team(team))


