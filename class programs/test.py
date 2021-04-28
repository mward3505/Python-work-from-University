def __str__(self):
    vertices_count = len(self.__vertices)
    result = "digraph G {\n"
    for label in self.__vertices:
        index = self.__vertices.index(label)
        for value in range(vertices_count):
            float_value = self.__matrix[index][value]
            if float_value is not None:
                float_string = "{:.1f}".format(float_value)
                result += "   " + label + " -> " + self.__vertices[value] + " [label=\"" + float_string + \
                          "\",weight=\"" + str(self.get_weight(label, self.__vertices[value])) \
                          + "\"];\n"
    result += "}\n"
    return result