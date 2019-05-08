import Stack

class GradingSystem:
    def __init__(self):
        self.graders = {}
        self.grades = {}

    def addGrader(self,name):
        self.graders[name] = Stack.Stack()

    def addStudent(self,name):
        self.grades[name] = []

    def addAssignmentsToGraders(self,name,GradeAssignment):
        self.graders[name].push(GradeAssignment)

    def assignmentGraded(self,name,GradeAssignment):
        self.grades[name] = GradeAssignment

    def gradersNotDone(self):
        rtnLst = []
        for x in self.graders.keys():
            if self.graders[x].isEmpty():
                rtnLst += [x]

        return rtnLst

class Student:
    def __init__(self,name,username):
        self.name = name
        self.username = username
        self.assignments = []

    def getName(self):
        return self.name
    
    def getUsername(self):
        return self.username

    def getAssignments(self):
        return self.assignments

class GradeAssignment:
    def __init__(self,grader,assignment):
        self.grader = grader
        self.assignment = assignment
        self.comment = ""

    def gradeAssignment(self,grade,comment):
        self.grader = grade
        self.comment = comment

class Assignment:
    def __init__(self,name,grade="None",comment="No comment"):
        self.a_name = name
        self.grade = grade
        self.comment = comment

    def set_grade(self,grade):
        self.grade = grade

    def get_grade(self):
        return self.grade

    def set_comment(self,comment):
        self.comment = comment

    def get_comment(self):
        return self.comment
