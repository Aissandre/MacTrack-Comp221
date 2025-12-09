from collections import deque
import nodes
import csv

def buildGraph():
    db = csv.reader(open('courseCSV.csv', 'r'))
    courseGraph = {}

    for row in db:
        name = row[0]
        ID = row[1]
        department = row[2]

        # the following need parsing algorithms
        attributes = row[3]
        prerequisites = row[4]
        newNode = nodes.Node(
            name,
            ID,
            department,
            attributes,
            prerequisites
        )
        courseGraph[ID] = newNode
    return courseGraph

def sortKhans(graph):
    preqCount = {}
    dependencies = {}
    idNode = {}                                         # this is because our current test graph is not a dictionary yet
    for node in graph:
        preqCount[node] = 0
        dependencies[node] = []
        idNode[node.getID()] = node

    q = deque()
    output = []

    for node in graph:
        for preq in node.getPrereqs():
            for preqID in preq:
                if preqID in idNode:                    # change this line after buildGraph() has been implemented
                    prereqNode = idNode[preqID]         # remove after buildGraph() has been implemented
                    dependencies[prereqNode].append(node)
                    preqCount[node] += 1

    for node in graph:
        if preqCount[node] == 0:
            q.append(node)

    while q:
        u = q.popleft()
        output.append(u)
        for dep in dependencies[u]:
            preqCount[dep] -= 1
            if preqCount[dep] == 0:
                q.append(dep)

    return output


if __name__ == '__main__':
    graphTest = [
        nodes.COMP123,
        nodes.COMP127,
        nodes.COMP128,
        nodes.COMP221,
        nodes.COMP225,
        nodes.MATH279,
        nodes.COMP240,
        nodes.COMP480
    ]
    gw = buildGraph()
    print(gw)
    for node in gw.values():
        print(f"{node.getName()}: {node.getPrereqs()}")
    # sorted_nodes = sortKhans(graphTest)
    # for out in sorted_nodes:
    #     print(f"{out.getID()}: {out.getName()}")
