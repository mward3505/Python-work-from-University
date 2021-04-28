import heapq
import math


class StorageCollection:
    def __init__(self, is_stack):
        if not isinstance(is_stack, bool):
            raise ValueError("is_stack parameter must be true or false.")
        self.popIndex = 0
        if is_stack:
            self.popIndex = -1
        self.storage = []

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        return self.storage.pop(self.popIndex)

    def is_empty(self):
        return self.storage == []


class Graph:
    def __init__(self):
        self.__vertices = []
        self.__matrix = [[]]

    def __iter__(self):
        vertices = self.bfs(self.__vertices[0])
        for item in vertices:
            yield item

    def add_vertex(self, label):
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
        if not isinstance(w, int) and not isinstance(w, float):
            raise ValueError

        if src not in self.__vertices or dest not in self.__vertices:
            raise ValueError
        else:
            self.__matrix[self.__vertices.index(src)][self.__vertices.index(dest)] = w

        return self

    def add_edge2way(self, src, dest, w):
        self.add_edge(src, dest, w)
        self.add_edge(dest, src, w)

    def vertex_count(self):
        return len(self.__vertices)

    def neighbors(self, vertex):
        result = []
        v = self.__vertices.index(vertex)
        for i in range(self.vertex_count()):
            weight = self.__matrix[v][i]
            if weight is not None:
                result.append((self.__vertices[i], weight))
        return result

    def get_weight(self, src, dest):
        if src not in self.__vertices or dest not in self.__vertices:
            raise ValueError
        elif self.__matrix[self.__vertices.index(src)][self.__vertices.index(dest)] is None:
            return math.inf
        else:
            return self.__matrix[self.__vertices.index(src)][self.__vertices.index(dest)]

    def __iterative_traversal(self, vertex, collection):
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
        stack = StorageCollection(True)
        return self.__iterative_traversal(root, stack)

    def bfs(self, root):
        queue = StorageCollection(False)
        return self.__iterative_traversal(root, queue)

    def get_index(self, priority_queue, vertex_label):
        for i in range(len(priority_queue)):
            if priority_queue[i][1] == vertex_label:
                return i
        return -1

    def dsp(self, src, dest):
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
        path_list = {}

        for vertex in self.__vertices:
            temp = self.dsp(src, vertex)
            path_list[vertex] = temp[1]

        return path_list

    def __str__(self):
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
    pass


if __name__ == "__main__":
    main()
