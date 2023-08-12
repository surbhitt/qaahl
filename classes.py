# classes only

class GraphNode:
    # data members
    rel_path = ""
    paths = []
    
    # member functions
    def __init__(self, rel_path="", paths=[]) -> None:
        self.rel_path = rel_path
        self.paths = paths
    
    def __str__(self) -> str:
        return f"{self.rel_path=} | {self.paths=}"

    def rec(self) -> None:
        pass
    
    def print_graph(self) -> None:
        pass
