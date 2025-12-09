from collections import deque
import nodes
import csv

def buildFullGraph():
    db = csv.reader(open('courseCSV.csv', 'r'))
    courseGraph = {}

    for row in db:
        name = row[0]
        ID = row[1]
        department = row[2]

        # the following need parsing algorithms
        attributes = set(row[3].split(';'))
        prerequisites = parsePrereqs(row[4])

        newNode = nodes.Node(
            name,
            ID,
            department,
            attributes,
            prerequisites
        )
        courseGraph[ID] = newNode

    return courseGraph

def parsePrereqs(prereqStr):
    if prereqStr == '':
        return []

    groups = []
    prereqGroups = prereqStr.split(';')

    for group in prereqGroups:
        optionals = set(group.split(','))
        groups.append(optionals)

    return groups

def buildSubgraph(fullgraph, targetCourse):
    subgraph = {}
    q = deque()

    for course in targetCourse:
        q.append(course)
    while q:
        u = q.popleft()

        subgraph[u] = fullgraph[u]
        course = fullgraph[u]
        prereqGroups = course.getPrereqs()

        for group in prereqGroups:
            for prereq in group:
                if prereq not in subgraph:
                    q.append(prereq)
    return subgraph

def sortKhans(graph):
    preqCount = {}
    dependencies = {}

    for node in graph.values():
        preqCount[node] = 0
        dependencies[node] = []

    q = deque()
    output = []

    for node in graph.values():
        for preq in node.getPrereqs():
            for preqID in preq:
                if preqID in graph:
                    prereqNode = graph[preqID]
                    dependencies[prereqNode].append(node)
                    preqCount[node] += 1

    for node in graph.values():
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
    print("Enter courses, separated by commas:")
    inputCourses = [c.strip() for c in input().split(",") if c.strip()]

    if not inputCourses:
        print("No courses entered.")
    else:
        gw = buildFullGraph()
        test = buildSubgraph(gw, inputCourses)
        sorted_nodes = sortKhans(test)
        for out in sorted_nodes:
            print(f"{out.getID()}: {out.getName()}")
