class Graph:
    def __init__(self):
        self.__vertices = []  # Keep track of indexes of vertices
        self.__matrix = [[]]  # The actual Adjacency Matrix

    def add_vertex(self, label):
        if label in self.__vertices:  # Make sure vertex is unique
            raise ValueError("Oops, that vertex already exists.")

        self.__vertices.append(label)  # Add vertex to list

        # Resize the matrix
        # self.__matrix = [[None for x in range(vertex_count)] for y in range(vertex_count)]
        # for i in range(vertex_count - 1):
        #     for j in range(vertex_count - 1):
        #         self.__matrix[i][j] = temp[i][j]
        # print(self.__matrix)

        for sub_matrix in self.__matrix:
            sub_matrix.append(None)
        self.__matrix.append([])
        for i in range(len(self.__vertices)):
            self.__matrix[-1].append(None)

        return self

    def add_edge(self, src, dest, w):
        if src not in self.__vertices or dest not in self.__vertices:
            raise ValueError("Either source or destination don't exist.")
        self.__matrix[self.__vertices.index(src)][self.__vertices.index(dest)] = w

    def get_weight(self, src, dest):
        if src not in self.__vertices or dest not in self.__vertices:
            raise ValueError("Either source or destination or both don't exist.")
        result = self.__matrix[self.__vertices.index(src)][self.__vertices.index(dest)]
        if result is None:
            raise ValueError("There is no Edge!")
        return result

    def __str__(self):
        result = "graph {\n"
        vertices_count = len(self.__vertices)
        for vertex in range(vertices_count):
            label = self.__vertices[vertex]
            for edge in range(vertices_count):
                value = self.__matrix[vertex][edge]
                if value is not None:
                    result += "\t" + label + "->" + self.__vertices[edge] \
                        + "[\"label=\"" + str(value) + "" + "\", weight=\"" + str(value) + "\"];\n"
        result += "}"
        return result


graph = Graph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

graph.add_edge("B", "C", 3)
graph.add_edge("A", "C", 2)
graph.add_edge("D", "A", 1)

print(graph)
