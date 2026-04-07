class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]


    def find(self, n):
        while n != self.parent[n]:
            self.parent[n] = self.parent[self.parent[n]]
            n = self.parent[n]
        return self.parent[n]
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        
        if self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
            self.rank[p2] += 1
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        
        return True



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        # we have to count the number of disjoint set

        res = n
        for n1, n2 in edges:
            if uf.union(n1, n2):
                res -= 1 

        return res