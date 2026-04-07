class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyMaps = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t','u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        res = []
        lenDigits = len(digits)
        if not lenDigits:
            return res 
            
        def nestedLoop(start, comb):
            print(start)
            if not comb:
                comb = keyMaps[digits[start]].copy()
            else:
                curr = []
                for c in comb:
                    for d in keyMaps[digits[start]]:
                        curr.append(c + d)

                comb = curr.copy()
            print(comb)
            if start + 1 == lenDigits:
                return comb
            else:
                return nestedLoop(start+1, comb)
            





        res = nestedLoop(0, [])

        return res
