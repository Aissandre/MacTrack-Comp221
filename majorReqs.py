# major requirements database
CSmajor = {
    "requirements" :[
        {
        "reqID": "Intro CS",
        "reqName": "Introductory Computer Science",
        "rule": {"type": "SINGLE", "ID": "COMP 123"}
        },
        {
        "reqID" : "OOP",
        "reqName" : "Object Oriented Programming",
        "rule" : {"type" : "SINGLE", "ID" : "COMP 127"}
        },
        {
        "reqID" : "Data Structures",
        "reqName" : "Data Structures",
        "rule" : {"type" : "SINGLE", "ID" : "COMP 128"}
        },
        {
        "reqID" : "Algo",
        "reqName" : "Algorithms",
        "rule" : {"type" : "SINGLE", "ID" : "COMP 221"}
        },
        {
        "reqID" : "Discrete",
        "reqName" : "Discrete Mathematics",
        "rule" : {"type" : "SINGLE", "ID" : "MATH 279"}
        },
        {
        "reqID" : "Software Dev",
        "reqName" : "Software Development",
        "rule" : {"type" : "SINGLE", "ID" : "COMP 225"}
        },
        {
        "reqID" : "Comp Sys",
        "reqName" : "Computer Systems",
        "rule" : {"type" : "SINGLE", "ID" : "COMP 240"}
        },
        {
        "reqID" : "Advanced CS Electives",
        "reqName" : "Advanced Electives",
        "rule" : {
            "type" : "GROUP",
            "count" : 2,
            "options": {
                "department" : ["Computer Science"],
                "attributes" : ["optional", "300-level"]
                }
            }
        },
        {
        "reqID" : "Math Electives",
        "reqName" : "Math Electives",
        "rule" : {
            "type" : "GROUP",
            "count" : 2,
            "options": {
                "department" : ["Mathematics", "Statistics"],
                "attributes" : ["optional"]
                }
            }
        },
        {
        "reqID" : "Capstone",
        "reqName" : "Capstone Course",
        "rule" : {
            "type" : "GROUP",
            "count" : 1,
            "options": {
                "department" : ["Computer Science"],
                "attributes" : ["Capstone"]
                }
            }
        }
    ]
}

