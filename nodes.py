class Node:
    def __init__(self, name, id, depart, attrib, prereqs):
        self.__name = name
        self.__id = id
        self.__depart = depart
        self.__attrib = attrib
        self.__prereqs = prereqs
        # maybe add info variable but not part of MVP

    def getName(self):
        return self.__name

    def getDepart(self):
        return self.__depart

    def getID(self):
        return self.__id

    def getAttrib(self):
        return self.__attrib

    def getPrereqs(self):
        return self.__prereqs

# Example Nodes
COMP123 = Node(
    "Core Concepts in Computer Science",
    "COMP 123",
    "CS",
    {"100 Level", "Required"},
    []
)

COMP127 = Node(
    "Object-Oriented Programming and Abstraction",
    "COMP 127",
    "CS",
    ["100 Level", "Required"],
    [{"COMP 123"}]
)

COMP128 = Node(
    "Data Structures",
    "COMP 128",
    "CS",
    ["100 Level", "Required"],
    [{"COMP 127"}]
)

COMP221 = Node(
    "Algorithm Design and Analysis",
    "COMP 221",
    "CS",
    ["200 Level", "Required"],
    [{"COMP 128"}, {"MATH 279"}]
)
# prereq structure
# prereqs = [
#   {pq1,pq2},  the stuff inside the curly brackets is OR
#   {pq3,pq4},  the stuff curly brackets themselves is AND
# ] this means prereqs are (pq1 or pq2) AND (pq3 or pq4)

if __name__ == "__main__":
    print(COMP123.getName())
    print(COMP123.getDepart())
    print(COMP123.getID())

