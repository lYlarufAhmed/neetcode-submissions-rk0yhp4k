class Graph:
    
    def __init__(self):
        self.edges = defaultdict(list)
        self.visited = set()


    def addEdge(self, src: int, dst: int) -> None:
        self.edges[src].append(dst)




    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.edges and dst in self.edges[src]:
            self.edges[src] = filter(lambda x: x != dst, self.edges[src])
            return True
        return False


    def hasPath(self, src: int, dst: int) -> bool:
        queue = deque()
        queue.append(src)

        while queue:
            s = queue.popleft()
            for d in self.edges[s]:
                if d == dst:
                    return True
                queue.append(d)
        return False

