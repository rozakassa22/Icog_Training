class Graph:
    """
    A class to represent a graph using adjacency list representation.
    """

    def __init__(self):
        self.vertices = []

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            setattr(self, vertex, [])
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            getattr(self, vertex1).append(vertex2)
            getattr(self, vertex2).append(vertex1)

    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return getattr(self, vertex)
        else:
            return []

    def __str__(self):
        graph_str = ""
        for vertex in self.vertices:
            graph_str += f"{vertex}: {getattr(self, vertex)}\n"
        return graph_str

def read_cities(file_path):
    """
    Reads a file with city connections and constructs a graph.

    :param file_path: Path to the file containing city connections.
    :return: A Graph object representing the cities and their connections.
    """
    graph = Graph()
    
    with open(file_path, 'r') as file:

        for line in file:
            city1, city2 = line.strip().split(',')
            graph.add_vertex(city1)
            graph.add_vertex(city2)
            graph.add_edge(city1, city2)
    
    return graph

def bfs(graph, start, goal):
    """
    Performs Breadth-First Search on the graph from start to goal.

    :param graph: Graph object
    :param start: Starting vertex
    :param goal: Goal vertex
    :return: List of vertices representing the path from start to goal
    """
    queue = [[start]]
    visited = set()

    while queue:
        path = queue.pop(0)
        vertex = path[-1]

        if vertex in visited:
            continue

        for neighbor in graph.get_neighbors(vertex):
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)

            if neighbor == goal:
                return new_path

        visited.add(vertex)

    return None

def dfs(graph, start, goal):
    """
    Performs Depth-First Search on the graph from start to goal.

    :param graph: Graph object
    :param start: Starting vertex
    :param goal: Goal vertex
    :return: List of vertices representing the path from start to goal
    """
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        vertex = path[-1]

        if vertex in visited:
            continue

        for neighbor in graph.get_neighbors(vertex):
            new_path = list(path)
            new_path.append(neighbor)
            stack.append(new_path)

            if neighbor == goal:
                return new_path

        visited.add(vertex)

    return None

# Example usage:
graph = read_cities('C:/Users/kassa/Downloads/Telegram Desktop/cities.txt')
print(graph)
print(bfs(graph, 'New York','Boston'))
print(dfs(graph,'New York','Boston'))
