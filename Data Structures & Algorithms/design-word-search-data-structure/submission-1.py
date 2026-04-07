class WordDictionary:

    def __init__(self):
        self.root = {}
        

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            node = node.setdefault(c, dict())
        node['__end__'] = True
        
        

    def search(self, word: str) -> bool:

        def dfs(index, nodes):
            if index == len(word):
                return '__end__' in nodes
            char = word[index]
            if char == '.':
                for node in nodes:
                    if node != '__end__':
                        if dfs(index+1, nodes[node]): return True
            elif char in nodes:
                return dfs(index+1, nodes[char])

            return False

        return dfs(0, self.root)
            
        
