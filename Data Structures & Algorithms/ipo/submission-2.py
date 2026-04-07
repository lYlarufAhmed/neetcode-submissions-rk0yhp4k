class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        mp = list(enumerate(zip(profits, capital)))
        pf = w
        seen = set()
        for _ in range(k):
            matches = [pair for pair in mp if pair[0] not in seen and pair[1][1] <= pf]
            print(matches)
            if matches:
                pr = max(matches, key=lambda x: x[1][0])
                # print(pr)
                i, (p,c) = pr
                seen.add(i)
                pf += p
        
        return pf