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

# prereq structure
# prereqs = [
#   {pq1,pq2},  the stuff inside the curly brackets is OR
#   {pq3,pq4},  the stuff curly brackets themselves is AND
# ] this means prereqs are (pq1 or pq2) AND (pq3 or pq4)
