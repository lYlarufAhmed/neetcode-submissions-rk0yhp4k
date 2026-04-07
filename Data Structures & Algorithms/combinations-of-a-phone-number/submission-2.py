class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        keyMaps = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t','u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }
        if not digits: return []
        res = ['']
        for d in digits:
            temp = []
            for prev in res:
                for c in keyMaps[int(d)]:
                    temp.append(prev+c)
            res = temp

        return res
        