class WordDictionary:

    def __init__(self):
        self.root = {}
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.setdefault(c, {})
        curr['__end__'] = True
        

    def search(self, word: str) -> bool:

        def dfs(index, node):
            # base case
            if index == len(word):
                return '__end__' in node
            
            char = word[index]

            if char == '.':
                return any(
                    dfs(index+1, val) for key, val in node.items() if key != '__end__'
                )
                        #if dfs(index+1, node[e]): return True
            
            elif char in node:
                return dfs(index+1, node[char])

            
            return False
        
        curr = self.root
        return dfs(0, curr)