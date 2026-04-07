class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N+1)]
        rank = [1] * (N+1)

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]
            pass
        
        def union(n1, n2):
            par1, par2 = find(n1), find(n2)
            if par1 == par2:
                return False
            if rank[par1] > rank[par2]:
                par[par2] = par1
            elif rank[par2] > rank[par1]:
                par[par1] = par2

            else:
                par[par2] = par1
                rank[par1] += 1
            # if rank[par1] > rank[par2]:
            #     par[par2] = par1
            #     rank[par1] += rank[par2]
            # else:
            #     par[par1] = par2
            
            return True
        


        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
            
        return []
