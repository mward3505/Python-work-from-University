#     totalLayers = self.height() + 1
#     totalWidth = (2 ** totalLayers) * 2
#     nodePosition = [None] * (totalLayers)
#     for i in range(totalLayers):
#         nodePosition[i] = [None] * (2 ** i)
#         for j in range(2 ** i):
#             nodePosition[i][j] = [0] * 3
#
#     lastLayer = nodePosition[totalLayers - 1]
#     gap = totalWidth // len(lastLayer)
#     for i in range(len(lastLayer)):
#         lastLayer[i][0] = i * gap
#         lastLayer[i][1] = lastLayer[i][0]
#         lastLayer[i][2] = lastLayer[i][0]
#
#     for i in reversed(range(totalLayers - 1)):
#         for j in range(len(nodePosition[i])):
#             first = nodePosition[i + 1][j * 2][0]
#             second = nodePosition[i + 1][j * 2 + 1][0]
#             nodePosition[i][j][1] = first + 1
#             nodePosition[i][j][2] = second - 1
#             nodePosition[i][j][0] = ((second - first) // 2) + first
#
#     result = [""] * (totalLayers * 2)
#     for i in range(1, len(result), 2):
#         for j in range(totalWidth):
#             result[i] += " "
#
#     self.__nodePrettyPrint(result, self.root, [0] * (totalLayers), nodePosition, ' ')
#     return "\n".join(result)
#
# def __nodePrettyPrint(self, result, node, nodeList, nodePosition, char):
#     level = node.level()
#     startLine = nodePosition[level][nodeList[level]][1]
#     endLine = nodePosition[level][nodeList[level]][2]
#     position = nodePosition[level][nodeList[level]][0]
#     resultLevel = level * 2
#     nodeList[level] += 1
#     currentLen = len(result[resultLevel])
#
#     for i in range(currentLen - 1, startLine):
#         result[resultLevel] += " "
#
#     for i in range(startLine, position):
#         result[resultLevel] += "_"
#
#     result[resultLevel] += str(node.get_value())
#
#     for i in range(position + len(str(node.get_value())), endLine):
#         result[resultLevel] += "_"
#
#     result[resultLevel + 1] = self.__strInsert(result[resultLevel + 1], startLine, '/')
#     if (endLine == startLine):
#         endLine += len(str(node.get_value()))
#     result[resultLevel + 1] = self.__strInsert(result[resultLevel + 1], endLine + 1, '\\')
#
#     if (node.left_child() is not None):
#         self.__nodePrettyPrint(result, node.left_child(), nodeList, nodePosition, '/')
#     elif (level + 1) < len(nodeList):
#         nextLevel = level + 1
#         capacity = 1
#         while nextLevel < len(nodeList):
#             nodeList[nextLevel] += capacity
#             capacity *= 2
#             nextLevel += 1
#
#     if (node.right_child() is not None):
#         self.__nodePrettyPrint(result, node.right_child(), nodeList, nodePosition, '\\')
#     elif (level + 1) < len(nodeList):
#         nextLevel = level + 1
#         capacity = 1
#         while nextLevel < len(nodeList):
#             nodeList[nextLevel] += capacity
#             capacity *= 2
#             nextLevel += 1