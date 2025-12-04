class Nodes:
    def __init__(self, name, depart, code, attrib, prereqs):
        self.__name = name
        self.__depart = depart
        self.__code = code
        self.__attrib = attrib
        self.__prereqs = prereqs
        # maybe add info variable but not part of MVP

    def getName(self):
        return self.__name

    def getDepart(self):
        return self.__depart

    def getCode(self):
        return self.__code

    def getAttrib(self):
        return self.__attrib

    def getPrereqs(self):
        return self.__prereqs



