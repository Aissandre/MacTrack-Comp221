class Node:

    def __init__(self, name, id, depart, exPreReqs, opPreReqs):
        """
        Initializes a node that represents an MSCS course.
        :param name: Course title
        :param id: Course number
        :param depart: Department name
        :param exPreReqs: Exclusive pre-requisites
        :param opPreReqs: Optional pre-requisites
        """
        self.__name = name
        self.__id = id
        self.__depart = depart
        self.__exPreReqs = exPreReqs
        self.__opPreReqs = opPreReqs

    def getName(self):
        return self.__name

    def getDepart(self):
        return self.__depart

    def getID(self):
        return self.__id

    def getExPreReqs(self):
        return self.__exPreReqs
    
    def getOpPreReqs(self):
        return self.__opPreReqs
