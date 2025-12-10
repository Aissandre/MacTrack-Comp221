from collections import deque
import nodes
import csv
import random

def buildFullGraph():
    db = csv.reader(open('courseCSV.csv', 'r'))
    courseGraph = {}

    for row in db:
        name = row[0]
        ID = row[1]
        department = row[2]
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

def checkMajorReqs(fullGraph, subgraph):
    missingClasses = []
    if 'COMP 123' not in subgraph and 'COMP 120' not in subgraph:
        missingClasses.append('COMP 123')
    if 'COMP 127' not in subgraph:
        missingClasses.append('COMP 127')
    if 'COMP 128' not in subgraph:
        missingClasses.append('COMP 128')
    if 'MATH 279' not in subgraph:
        missingClasses.append('MATH 279')
    if 'COMP 221' not in subgraph:
        missingClasses.append('COMP 221')
    if 'COMP 225' not in subgraph:
        missingClasses.append('COMP 225')
    if 'COMP 240' not in subgraph:
        missingClasses.append('COMP 240')


    # Check for math/stats electives
    validKeys = set()
    for key in subgraph.keys():
        if (key[0:4] == 'MATH' or key[0:4] == 'STAT') and int(key[5:8]) >= 135 and key != 'MATH 279':
            validKeys.add(key)

    if len(validKeys) < 2:
        listOfValidClasses = []
        for id in fullGraph.keys():
            if (id[0:4] == 'MATH' or key[0:4] == 'STAT') and int(id[5:8]) >= 135 and id != 'MATH 279':
                listOfValidClasses.append(id)
        while len(validKeys) < 2:
            randClass = random.choice(listOfValidClasses)
            listOfValidClasses.remove(randClass)
            missingClasses.append(randClass)
            validKeys.add(randClass)


    # Check for advanced comp electives
    validKeys = set()
    for key in subgraph.keys():
        if key[0:4] == 'COMP' and int(key[5:8]) >= 300 and int(key[5:8]) <= 499:
            validKeys.add(key)

    if len(validKeys) < 2:
        listOfValidClasses = []
        for id in fullGraph.keys():
            if id[0:4] == 'COMP' and int(id[5:8]) >= 300 and int(id[5:8]) <= 499:
                listOfValidClasses.append(id)
        while len(validKeys) < 2:
            randClass = random.choice(listOfValidClasses)
            listOfValidClasses.remove(randClass)
            missingClasses.append(randClass)
            validKeys.add(randClass)


    # Check for capstone
    capstone = False
    for key in subgraph.keys():
        if key[0:4] == 'COMP' and int(key[5:8]) >= 400 and int(key[5:8]) != '479':
            capstone = True
            break

    if not capstone:
        listOfValidClasses = []
        for id in fullGraph.keys():
            if id[0:4] == 'COMP' and int(key[5:8]) >= 400 and int(key[5:8]) != '479':
                listOfValidClasses.append(id)
        missingClasses.append(random.choice(listOfValidClasses))

    return missingClasses


if __name__ == '__main__':
    print("Enter courses you want to take (DEPT ###), separated by commas:")
    inputCourses = [c.strip() for c in input().split(",") if c.strip()]

    if not inputCourses:
        print("No courses entered.")
    else:
        gw = buildFullGraph()
        test = buildSubgraph(gw, inputCourses)
        for course in checkMajorReqs(gw, test):
            inputCourses.append(course)
        finalGraph = buildSubgraph(gw, inputCourses)
        sorted_nodes = sortKhans(finalGraph)
        for out in sorted_nodes:
            print(f"{out.getID()}: {out.getName()}")