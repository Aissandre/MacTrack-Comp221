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

# Course Nodes
COMP112 = Node(
     "Introduction to Data Science",
     "COMP 112",
     "Computer Science",
     {"100 Level", "Optional"},
     []
)

COMP120 = Node(
     "Computing and Society",
     "COMP 120",
     "Computer Science",
     {"100 Level", "Optional"},
     []
)

COMP123 = Node(
     "Core Concepts in Computer Science",
     "COMP 123",
     "Computer Science",
     {"100 Level", "Required"},
     []
)

COMP127 = Node(
     "Object-Oriented Programming and Abstraction",
     "COMP 127",
     "Computer Science",
     {"100 Level", "Required"},
     [{"COMP 123"}]
)

COMP128 = Node(
     "Data Structures",
     "COMP 128",
     "Computer Science",
     {"100 Level", "Required"},
     [{"COMP 127"}]
)

COMP154 = Node(
     "Digital Ethics",
     "COMP 154",
     "Computer Science",
     {"100 Level", "Optional"},
     []
)

COMP212 = Node(
     "Intermediate Data Science",
     "COMP 212",
     "Computer Science",
     {"200 Level", "Optional"},
     [{"COMP 123"}, {"STAT 112"}, {"STAT 155"}]
)

COMP221 = Node(
     "Algorithm Design and Analysis",
     "COMP 221",
     "Computer Science",
     {"200 Level", "Required"},
     [{"COMP 128,COMP 124"}, {"MATH 279"}]
)

COMP225 = Node(
     "Software Design and Development",
     "COMP 225",
     "Computer Science",
     {"200 Level", "Required"},
     [{"COMP 127,COMP 124"}]
)

COMP240 = Node(
     "Computer Systems",
     "COMP 240",
     "Computer Science",
     {"200 Level", "Required"},
     [{"COMP 127"}]
)

COMP272 = Node(
     "Advanced Remote Sensing",
     "COMP 272",
     "Computer Science",
     {"200 Level", "Optional"},
     [{"GEOG 352"}]
)

COMP302 = Node(
     "Introduction to Database Management Systems",
     "COMP 302",
     "Computer Science",
     {"300 Level", "Optional"},
     [{"COMP 127"}]
)

COMP320 = Node(
     "Computational Biology",
     "COMP 320",
     "Computer Science",
     {"300 Level", "Optional"},
     [{"COMP 123"}]
)

COMP321 = Node(
     "Software Testing",
     "COMP 321",
     "Computer Science",
     {"300 Level", "Optional"},
     [{"COMP 127"}, {"COMP 128"}]
)

COMP325 = Node(
     "Video Games: Coding and Narrative",
     "COMP 325",
     "Computer Science",
     {"300 Level", "Optional"},
     [{"COMP 127"}]
)

COMP340 = Node(
     "Digital Electronics",
     "COMP 340",
     "Computer Science",
     {"300 Level", "Optional"},
     [{"MATH 137"}]
)

COMP342 = Node(
     "Operating Systems and Computer Architecture",
     "COMP 342",
     "Computer Science",
     {"300 Level", "Optional"},
     [{"COMP 240"}]
)

COMP361 = Node(
     "Theory of Computation",
     "COMP 361",
     "Computer Science",
     {"300 Level", "Optional"},
     [{"COMP 128,COMP 221,COMP 124"}, {"MATH 279"}]
)

COMP364 = Node(
     "Human-Computer Interaction",
     "COMP 364",
     "Computer Science",
     {"300 Level", "Optional"},
     [{"COMP 123"}]
)

COMP365 = Node(
     "Computational Linear Algebra",
     "COMP 365",
     "Computer Science",
     {"300 Level", "Optional"},
     [{"MATH 236"}, {"MATH 135,MATH 137,MATH 237"}, {"COMP 120,COMP 123,COMP 127,COMP 128"}]
)

COMP381 = Node(
     "Programming Languages",
     "COMP 381",
     "Computer Science",
     {"300 Level", "Optional"},
     [{"COMP 128"}]
)

COMP435 = Node(
     "Data Visualization",
     "COMP 435",
     "Computer Science",
     {"400 Level", "Optional"},
     [{"COMP 127"}]
)

COMP440 = Node(
     "Collective Intelligence",
     "COMP 440",
     "Computer Science",
     {"400 Level", "Optional"},
     [{"COMP 221,[{\"COMP 127\"}, {\"STAT 253\"}]"}] #COMP 221; or both COMP 127 and STAT 253
)

COMP445 = Node(
     "Parallel and Distributed Processing",
     "COMP 445",
     "Computer Science",
     {"400 Level", "Optional"},
     [{"COMP 240"}, {"COMP 221"}]
)

COMP446 = Node(
     "Internet Computing",
     "COMP 446",
     "Computer Science",
     {"400 Level", "Optional"},
     [{"COMP 225"}]
)

COMP456 = Node(
     "Projects in Data Science",
     "COMP 456",
     "Computer Science",
     {"400 Level", "Optional"},
     [{"COMP 212"}, {"STAT 253"}]
)

COMP465 = Node(
     "Interactive Computer Graphics",
     "COMP 465",
     "Computer Science",
     {"400 Level", "Optional"},
     [{"COMP 240"}]
)

COMP479 = Node(
     "Network Science",
     "COMP 479",
     "Computer Science",
     {"400 Level", "Optional"},
     [{"COMP 123"}, {"MATH 236"}, {"MATH 279"}, {"COMP 221,MATH 354,STAT 354,MATH 375,MATH 379"}]
)

COMP480 = Node(
     "Bodies/Minds: AI Robotics",
     "COMP 480",
     "Computer Science",
     {"400 Level", "Optional"},
     [{"COMP 221"}]
)

COMP484 = Node(
     "Introduction to Artificial Intelligence",
     "COMP 484",
     "Computer Science",
     {"400 Level", "Optional"},
     [{"COMP 221,[{\"COMP 127\"}, {\"STAT 253\"}]"}] #COMP 221; or both COMP 127 and STAT 253
)

COMP487 = Node(
     "Computer Security and Privacy",
     "COMP 487",
     "Computer Science",
     {"400 Level", "Optional"},
     [{"COMP 240"}]
)

MATH135 = Node(
     "Applied Multivariable Calculus I",
     "MATH 135",
     "Mathematics",
     {"100 Level", "Optional"},
     []
)

MATH137 = Node(
     "Applied Multivariable Calculus II",
     "MATH 137",
     "Mathematics",
     {"100 Level", "Optional"},
     []
)

MATH212 = Node(
     "Philosophy of Mathematics",
     "MATH 212",
     "Mathematics",
     {"200 Level", "Optional"},
     [{"PHIL 111"}, {"MATH 279"}]
)

MATH236 = Node(
     "Linear Algebra",
     "MATH 236",
     "Mathematics",
     {"200 Level", "Optional"},
     [{"MATH 279,MATH 137,STAT 155"}]
)

MATH237 = Node(
     "Applied Multivariable Calculus III",
     "MATH 237",
     "Mathematics",
     {"200 Level", "Optional"},
     [{"MATH 137"}]
)

MATH279 = Node(
     "Discrete Mathematics",
     "MATH 279",
     "Mathematics",
     {"200 Level", "Required"},
     []
)

MATH312 = Node(
     "Differential Equations",
     "MATH 312",
     "Mathematics",
     {"300 Level", "Optional"},
     [{"MATH 236"}, {"MATH 237"}]
)

MATH313 = Node(
     "Advanced Symbolic Logic",
     "MATH 313",
     "Mathematics",
     {"300 Level", "Optional"},
     [{"PHIL 111,MATH 279"}]
)

MATH354 = Node(
     "Probability",
     "MATH 354",
     "Mathematics",
     {"300 Level", "Optional"},
     [{"MATH 137,MATH 237"}]
)

MATH355 = Node(
     "Statistical Theory",
     "MATH 355",
     "Mathematics",
     {"300 Level", "Optional"},
     [{"STAT 155"}, {"MATH 236"}, {"MATH 354,STAT 354"}] #MATH 354/STAT 354 CROSS-LIST
)

MATH361 = Node(
     "Theory of Computation",
     "MATH 361",
     "Mathematics",
     {"300 Level", "Optional"},
     [{"COMP 128,COMP 221"}, {"MATH 279"}]
)

MATH365 = Node(
     "Computational Linear Algebra",
     "MATH 365",
     "Mathematics",
     {"300 Level", "Optional"},
     [{"MATH 236"}, {"MATH 135,MATH 137,MATH 237"}, {"COMP 120,COMP 123,COMP 127,COMP 128"}]
)

MATH375 = Node(
     "Graph Theory",
     "MATH 375",
     "Mathematics",
     {"300 Level", "Optional"},
     [{"MATH 279"}]
)

MATH376 = Node(
     "Algebraic Structures",
     "MATH 376",
     "Mathematics",
     {"300 Level", "Optional"},
     [{"MATH 279"}, {"MATH 236"}]
)

MATH377 = Node(
     "Real Analysis",
     "MATH 377",
     "Mathematics",
     {"300 Level", "Optional"},
     [{"MATH 137"}, {"MATH 236,MATH 237,MATH 279"}]
)

MATH378 = Node(
     "Complex Analysis",
     "MATH 378",
     "Mathematics",
     {"300 Level", "Optional"},
     [{"MATH 236"}, {"MATH 237"}]
)

MATH379 = Node(
     "Combinatorics",
     "MATH 379",
     "Mathematics",
     {"300 Level", "Optional"},
     [{"MATH"}, {"279"}]
)

MATH432 = Node(
     "Mathematical Modeling",
     "MATH 432",
     "Mathematics",
     {"400 Level", "Optional"},
     [{"MATH 312"}, {"COMP 120,COMP 123,COMP 124"}]
)

MATH437 = Node(
     "Topics in Applied Mathematics",
     "MATH 437",
     "Mathematics",
     {"400 Level", "Optional"},
     [{"MATH 236"}, {"COMP 120,COMP 123,COMP 124"}]
)

MATH465 = Node(
     "Signal Processing",
     "MATH 465",
     "Mathematics",
     {"400 Level", "Optional"},
     [{"MATH 236"}, {"COMP 123"}]
)

MATH471 = Node(
     "Topology",
     "MATH 471",
     "Mathematics",
     {"400 Level", "Optional"},
     [{"MATH 236"}, {"MATH 365,MATH 375,MATH 376,MATH 377,MATH 378,MATH 379"}]
)

MATH476 = Node(
     "Representation Theory",
     "MATH 476",
     "Mathematics",
     {"400 Level", "Optional"},
     [{"MATH 376"}]
)

MATH477 = Node(
     "Topics in Analysis",
     "MATH 477",
     "Mathematics",
     {"400 Level", "Optional"},
     [{"MATH 236"}, {"MATH 377"}]
)

MATH479 = Node(
     "Network Science",
     "MATH 479",
     "Mathematics",
     {"400 Level", "Optional"},
     [{"COMP 123"}, {"MATH 236"}, {"MATH 279"}, {"COMP 221,MATH 354,STAT 354,MATH 375,MATH 379"}]
)

STAT112 = Node(
     "Introduction to Data Science",
     "STAT 112",
     "Statistics",
     {"100 Level", "Optional"},
     []
)

STAT125 = Node(
     "Epidemiology",
     "STAT 125",
     "Statistics",
     {"100 Level", "Optional"},
     []
)

STAT155 = Node(
     "Introduction to Statistical Modeling",
     "STAT 155",
     "Statistics",
     {"100 Level", "Optional"},
     []
)

STAT202 = Node(
     "Data and Society",
     "STAT 202",
     "Statistics",
     {"200 Level", "Optional"},
     [{"STAT 155"}, {"STAT 112,COMP 112"}] #STAT 112/COMP 112 CROSS-LIST
)

STAT212 = Node(
     "Intermediate Data Science",
     "STAT 212",
     "Statistics",
     {"200 Level", "Optional"},
     [{"COMP 112"}, {"COMP 123"}, {"STAT 155"}]
)

STAT253 = Node(
     "Statistical Machine Learning",
     "STAT 253",
     "Statistics",
     {"200 Level", "Optional"},
     [{"STAT 155"}]
)

STAT354 = Node(
     "Probability",
     "STAT 354",
     "Statistics",
     {"300 Level", "Optional"},
     [{"MATH 137,MATH 237"}]
)

STAT355 = Node(
     "Statistical Theory",
     "STAT 355",
     "Statistics",
     {"300 Level", "Optional"},
     [{"STAT 155"}, {"MATH 236"}, {"MATH 354,STAT 354"}] #MATH 354/STAT 354 CROSS-LIST
)

STAT451 = Node(
     "Causal Interference",
     "STAT 451",
     "Statistics",
     {"400 Level", "Optional"},
     [{"STAT 155"}]
)

STAT452 = Node(
     "Correlated Data",
     "STAT 452",
     "Statistics",
     {"400 Level", "Optional"},
     [{"STAT 155"}, {"MATH 354,STAT 354"}] #MATH 354/STAT 354 CROSS-LIST
)

STAT453 = Node(
     "Survival Analysis",
     "STAT 453",
     "Statistics",
     {"400 Level", "Optional"},
     [{"STAT 155"}, {"MATH 354"}]
)

STAT454 = Node(
     "Bayesian Statistics",
     "STAT 454",
     "Statistics",
     {"400 Level", "Optional"},
     [{"STAT 155"}, {"MATH 354"}]
)

STAT456 = Node(
     "Projects in Data Science",
     "STAT 456",
     "Statistics",
     {"400 Level", "Optional"},
     [{"STAT 212"}, {"STAT 253"}]
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
