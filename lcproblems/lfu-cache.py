from datetime import datetime

# https://leetcode.com/problems/lfu-cache/

class DLList:                                                                                                                                           
                                                                                                                                                        
    class DLNode:                                                                                                                                       
        def __init__(self, data):                                                                                                                       
            self._prev = None                                                                                                                           
            self._next = None                                                                                                                           
            self._data = data                                                                                                                           
                                                                                                                                                        
        def __repr__(self):                                                                                                                             
            return f"{self._data}"                                                                                                                      
                                                                                                                                                        
    def __init__(self):                                                                                                                                 
        self._head = None                                                                                                                               
        self._tail = None                                                                                                                               
                                                                                                                                                        
    def popleft(self):                                                                                                                            
        if not self._head:                                                                                                                              
            return                                                                                                                                      
        h = self._head                                                                                                                                  
        nxn = h._next
        if nxn:                                                                                                                                   
            nxn._prev = None                                                                                                                                
        self._head = nxn                                                                                                                                
        if self._tail == h:                                                                                                                             
            self._tail = nxn                                                                                                                            
        return h                                                                                                                                        
                                                                                                                                                                                                                                                                                   
                                                                                                                                                        
    def find(self, data):                                                                                                                               
        n = self._head                                                                                                                                  
        while n and not (n._data == data):                                                                                                              
            n = n._next                                                                                                                                 
        return n                                                                                                                                        

    def append(self, data):                                                                                                                             
        d = self.DLNode(data)                                                                                                                           
        if not self._head:                                                                                                                              
            self._head = d                                                                                                                              
            self._tail = d                                                                                                                              
            return                                                                                                                                      
        pvn = self._tail                                                                                                                                
        pvn._next = d                                                                                                                                   
        d._prev = pvn                                                                                                                                   
        self._tail = d                                                                                                                                  
        return                    
                                                                                                                                                     
    def remove(self, data):                                                                                                                             
        n = self.find(data)                                                                                                                             
        if not n:                                                                                                                                       
            return                                                                                                                                      
        pvn, nxn = n._prev, n._next                                                                                                                     
        if pvn:                                                                                                                                         
            pvn._next = nxn 
        if nxn:                                                                                                                            
            nxn._prev = pvn                                                                                                                                 
        n._prev = None                                                                                                                                  
        n._next = None                                                                                                                                  
        if self._head == n:                                                                                                                             
            self._head = nxn                                                                                                                            
        if self._tail == n:                                                                                                                             
            self._tail = pvn                  
             
    def __repr__(self):                                                                                                                                 
        arr = []                                                                                                                                        
        n = self._head                                                                                                                                  
        while n:                                                                                                                                        
            arr.append(str(n))                                                                                                                          
            n = n._next                                                                                                                                 
        return "->".join(arr)       


class LFUCache:

    class CacheValue:

        def __init__(self, key, val):
            self._use_count = 0
            self._key = key
            self._val = val
            self._ts = 0
            self.update()
            
        def update(self):
            self._use_count += 1
            self._ts = datetime.now().timestamp()

        def getKey(self):
            return (self._use_count, self._ts, self._key)
            
        def __repr__(self):
            return f"{self._key=} {self._use_count=} {self._ts=}"

    

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = {}
        self._dllists = {}

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        cVal = self._cache[key]
        oldKey = cVal.getKey()
        cVal.update()
        newKey = cVal.getKey()
        self._cache[key] = cVal
        self._updateList(oldKey, newKey)
        # print(f"get:post: {key=}", self._dllists, self._cache)
        return cVal._val

    def put(self, key: int, value: int) -> None:
        #print(f"put:pre: {key=}", self._dllists, self._cache)
        if key in self._cache:
            cVal = self._cache[key]
            cVal._val = value
            oldKey = cVal.getKey()
            cVal.update()
            self._cache[key] = cVal
            newKey = cVal.getKey()
            self._updateList(oldKey, newKey)
        else:
            if len(self._cache) >= self._capacity:
                self._killSomeEntries()
            cVal = self.CacheValue(key=key, val=value)
            self._cache[key] = cVal
            newKey = cVal.getKey()
            self._updateList(oldKey=None, newKey=newKey)
        # print(f"put:post: {key=}", self._dllists, self._cache)
    
    def _updateList(self, oldKey, newKey):
        if oldKey and oldKey[0] in self._dllists:
            self._dllists[oldKey[0]].remove(oldKey)
        dl = self._dllists.get(newKey[0], DLList())
        dl.append(newKey)
        self._dllists[newKey[0]] = dl
        # self._dllist = sorted(self._dllist, reverse=True, key=lambda x: (x._use_count, x._ts))

    def _killSomeEntries(self):
        if len(self._cache) < self._capacity or len(self._cache) <= 0:
            return
        while len(self._cache) >= self._capacity:
            minx = min(self._dllists.keys())
            if not (self._dllists[minx] and self._dllists[minx]._head):
                del self._dllists[minx]
                continue
            kNode = self._dllists[minx].popleft()
            if not kNode:
                break
            del self._cache[kNode._data[2]]
        
    def __repr__(self):
        return f"{len(self._cache)=} {self._dllists=} {self._cache=}"

