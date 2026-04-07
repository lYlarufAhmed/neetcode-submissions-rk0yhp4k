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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToIndexMap = {}
        uf = UnionFind(len(accounts))
        for index, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in emailToIndexMap:
                    uf.union(index, emailToIndexMap[email])
                else:
                    emailToIndexMap[email] = index
        
        emailGroup = defaultdict(list)

        for email, index in emailToIndexMap.items():
            leader = uf.find(index)
            emailGroup[leader].append(email)
        
        for ind in emailGroup:
            emailGroup[ind] = [accounts[ind][0]] + sorted(emailGroup[ind])
        
        return list(emailGroup.values())