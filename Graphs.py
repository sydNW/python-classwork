class Graphs:
    def __init__(self, directed = False):
        self.directed = directed

        """
        here is how the graph is going to look like
        
        graph = {
        
        }
        """

        self.adj_list = dict() # a dictionary uses key value pairs

    def __repr__(self):
        graph_string = ""

        for node, neighbours in self.adj_list.items(): # here we now use the key value pairs, where the node is the key and the neighbour is the value.
            graph_string += f"{node} -> {neighbours}\n"

        return graph_string

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set ()

        else:
            raise ValueError("Node already exists")

    def add_edge(self, from_node, to_node, weight = None):
        if from_node not in self.adj_list:
            self.add_node(from_node)

        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weight is None: #conditions for when the weight is none
            self.adj_list[from_node].add(to_node) # create an edge from the source to the destination

            if not self.directed:
                self.adj_list[to_node].add(from_node) # if the graph is not directed, create an edge from the destination back to the source

        else: #conditions for when there is weight
            self.adj_list[from_node].add((to_node, weight)) #create an edge from the source to the destination including the weight

            if not self.directed:
                self.adj_list[to_node].add((from_node, weight)) #if the graph is not directed, create another edge from the destination back to the source but including the weight

    def BreadthFirstSearch(self, start_node):
        visited = set()
        queue = [start_node]
        order = []

        while queue:
            node = queue.pop(0)

            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)

                for neighbour in neighbours:
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbours not in visited:
                        queue.append(neighbour)
        return order


    def DepthFirstSearch(self, start_node):
        visited = set()
        stack = [start_node]
        order = []

        while stack:
            node = stack.pop()

            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)

                for neighbour in sorted(neighbours):
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbours not in visited:
                        stack.append(neighbour)
        return order



    def obtain_neighbours(self, node):
        return self.adj_list.get(node, set())

if __name__ == "__main__":
    graph_obj = Graphs(directed = True)

    graph_obj.add_edge("A", "B", 2)
    graph_obj.add_edge("A", "J", 2)
    graph_obj.add_edge("A", "C", 3)
    graph_obj.add_edge("A", "D", 4)
    graph_obj.add_edge("B", "D", 4)
    graph_obj.add_edge("D", "C", 7)

    print(graph_obj)

    print("BREADTH FIRST SEARCH: \n")
    print(graph_obj.BreadthFirstSearch("A"))
    print("DEPTH FIRST SEARCH: \n")
    print(graph_obj.DepthFirstSearch("A"))