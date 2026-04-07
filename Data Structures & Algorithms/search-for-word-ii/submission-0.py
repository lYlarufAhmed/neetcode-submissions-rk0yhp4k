class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class Trie:

            def __init__(self):
                self.root = {}
            
            def add(self, word):
                curr = self.root

                for c in word:
                    curr = curr.setdefault(c, {})
                curr['_end_'] = True
        
        trie = Trie()

        for word in words:
            trie.add(word)
        trie_root = trie.root
        
        ROWS, COLS = len(board), len(board[0])

        res, visit = set(), set()

        def dfs(r,c, node, word):

            if r >= ROWS or c >= COLS or r < 0 or c < 0 or (r,c) in visit or board[r][c] not in node:
                return

            visit.add((r,c))

            word += board[r][c]
            next_node = node[board[r][c]]
            if '_end_' in  next_node:
                res.add(word)
            

            dfs(r+1, c, next_node, word)
            dfs(r-1, c, next_node, word)
            dfs(r, c-1, next_node, word)
            dfs(r, c+1, next_node, word)

            visit.remove((r, c))
            

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie_root, "")
        
        
        
        return list(res)


        