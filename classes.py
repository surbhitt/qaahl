# classes only

class GraphNode:
    url = ""
    paths = []
    def __init__(self, url="", paths=[]) -> None:
        self.url = url
        self.paths = paths

    def rec(self) -> None:
        pass
    
    def print_graph(self) -> None:
        pass
