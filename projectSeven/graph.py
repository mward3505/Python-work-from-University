import math


class StorageCollection:
    """Organize the storage to use a stack"""
    def __init__(self, is_stack):
        if not isinstance(is_stack, bool):
            raise ValueError("is_stack parameter must be true or false.")
        self.popIndex = 0
        if is_stack:
            self.popIndex = -1
        self.storage = []

    def push(self, value):
        """Pushes items on to the stack"""
        self.storage.append(value)

    def pop(self):
        """Pops items from the stack"""
        return self.storage.pop(self.popIndex)

    def is_empty(self):
        """Checks the stack for when it's empty"""
        return self.storage == []


class Graph:
    """Creates a graph"""
    def __init__(self):
        """Constructs the graph properties"""
        self.__vertices = []
        self.__matrix = [[]]

    def __iter__(self):
        """Creates an iterator for the vertices"""
        vertices = self.bfs(self.__vertices[0])
        for item in vertices:
            yield item

    def add_vertex(self, label):
        """Adds vertex to the graph"""
        if not isinstance(label, str):
            raise ValueError

        vertices_count = len(self.__vertices)
        self.__vertices.append(label)
        temp = self.__matrix
        self.__matrix = [[None for x in range(vertices_count + 1)] for y in range(vertices_count + 1)]
        for i in range(0, vertices_count):
            for j in range(0, vertices_count):
                self.__matrix[i][j] = temp[i][j]

        return self

    def add_edge(self, src, dest, w):
        """Adds a distance between two vertices"""
        if not isinstance(w, int) and not isinstance(w, float):
            raise ValueError

        if src not in self.__vertices or dest not in self.__vertices:
            raise ValueError
        else:
            self.__matrix[self.__vertices.index(src)][self.__vertices.index(dest)] = w

        return self

    def vertex_count(self):
        """Counts the vertices"""
        return len(self.__vertices)

    def neighbors(self, vertex):
        """Helps find the neighbors for the graph"""
        result = []
        v = self.__vertices.index(vertex)
        for i in range(self.vertex_count()):
            weight = self.__matrix[v][i]
            if weight is not None:
                result.append((self.__vertices[i], weight))
        return result

    def get_weight(self, src, dest):
        """Returns the weight of a path if it is found otherwise will assign infinity"""
        if src not in self.__vertices or dest not in self.__vertices:
            raise ValueError
        elif self.__matrix[self.__vertices.index(src)][self.__vertices.index(dest)] is None:
            return math.inf
        else:
            return self.__matrix[self.__vertices.index(src)][self.__vertices.index(dest)]

    def __iterative_traversal(self, vertex, collection):
        """helps iterate through the graph"""
        result = []
        visited = [False] * len(self.__vertices)
        vertices_count = len(self.__vertices)
        index = self.__vertices.index(vertex)
        collection.push(index)
        visited[index] = True

        while not collection.is_empty():
            v = collection.pop()
            result.append(self.__vertices[v])

            for i in range(vertices_count):
                neighbor = self.__matrix[v][i]
                if neighbor is not None and visited[i] == False:
                    collection.push(i)
                    visited[i] = True
        return result

    def dfs(self, root):
        """Depth first search through the graph"""
        stack = StorageCollection(True)
        return self.__iterative_traversal(root, stack)

    def bfs(self, root):
        """Breadth first search through the graph"""
        queue = StorageCollection(False)
        return self.__iterative_traversal(root, queue)

    def get_index(self, priority_queue, vertex_label):
        """Returns the current index"""
        for i in range(len(priority_queue)):
            if priority_queue[i][1] == vertex_label:
                return i
        return -1

    def dsp(self, src, dest):
        """Helps find the shortest distance between the source and the destination provided"""
        priority_queue = []
        # Set all nodes as unvisited
        visited = []

        vertex_count = self.vertex_count()

        # Assign to every node a tentative distance value
        for vertex in self:
            if vertex == src:
                priority_queue.insert(0, (0, vertex, None))
            else:
                priority_queue.append((float('infinity'), vertex, None))

        while priority_queue[0][0] < float('infinity') and dest not in visited:
            # Get the current node, the first unvisited node in the priority queue
            for i in range(vertex_count):
                if priority_queue[i][1] not in visited:
                    current_vertex = priority_queue[i][1]
                    current_distance = priority_queue[i][0]
                    break

            # Visit all the neighbors and assign a tentative distance
            for item in self.neighbors(current_vertex):
                neighbor = item[0]
                if neighbor in visited:
                    continue
                weight = item[1]
                distance = current_distance + weight
                # Find the vertex in the priority queue to check and update its distances
                neighbor_index = self.get_index(priority_queue, neighbor)
                if neighbor_index == -1:
                    continue
                elif priority_queue[neighbor_index][0] > distance:
                    priority_queue[neighbor_index] = (distance, neighbor, current_vertex)

            visited.append(current_vertex)

            # Sort list so lowest distance is on top
            priority_queue = sorted(priority_queue, key=lambda x: x[0])

        # See if we found a path
        target_index = self.get_index(priority_queue, dest)
        resulting_length = priority_queue[target_index][0]
        if resulting_length == float('infinity'):
            return resulting_length, []
        else:
            # Trace back the path from the target to the source
            current_vertex = dest
            resulting_path = []
            resulting_path.append(current_vertex)
            while current_vertex != src:
                current_vertex = priority_queue[self.get_index(priority_queue, current_vertex)][2]
                resulting_path.insert(0, current_vertex)
            return resulting_length, resulting_path

    def dsp_all(self, src):
        """Returns all available shortest paths for the desired source"""
        path_list = {}

        for vertex in self.__vertices:
            temp = self.dsp(src, vertex)
            path_list[vertex] = temp[1]

        return path_list

    def __str__(self):
        """Helps print out the graph and it's paths"""
        vertices_count = len(self.__vertices)
        result = "digraph G {\n"
        for label in self.__vertices:
            index = self.__vertices.index(label)
            for value in range(vertices_count):
                float_value = self.__matrix[index][value]
                if float_value is not None:
                    float_string = "{:.1f}".format(float_value)
                    result += "   " + label + " -> " + self.__vertices[
                        value] + " [label=\"" + float_string + "\",weight=\"" + float_string + "\"];\n"
        result += "}\n"
        return result


def main():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")

    graph.add_edge("A", "B", 2)
    graph.add_edge("A", "F", 9)

    graph.add_edge("B", "F", 6)
    graph.add_edge("B", "D", 15)
    graph.add_edge("B", "C", 8)

    graph.add_edge("C", "D", 1)

    graph.add_edge("E", "C", 7)
    graph.add_edge("E", "D", 3)

    graph.add_edge("F", "B", 6)
    graph.add_edge("F", "E", 3)

    print(graph)
    print("starting BFS with vertex A")
    for vertex in graph.bfs("A"):
        print(vertex, end="")
    print()
    print()

    print("starting BFS with vertex A")
    for vertex in graph.dfs("A"):
        print(vertex, end="")
    print()
    print()

    result = graph.dsp("A", "F")
    print(result[1])
    print()
    print(graph.dsp_all("A"))


if __name__ == "__main__":
    main()
