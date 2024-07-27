class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        uniquePath = {}
        
        for path in paths:
            for i in range(len(path)):
                if path[i] in uniquePath:
                    del uniquePath[path[i]]
                else:
                    uniquePath[path[i]] = i
                
        for key, value in uniquePath.items():
            if value == 1:
                return key