from GradingSystem import GradingSystem, Student, GradeAssignment, Assignment
from Stack import Stack
"""
I have given you this code, you cannot change it. If it doesn't work with 
your code, means you have to adapt your code to work. I have tested it 
with my code and made sure it runs. Documentation might not have warned you, 
but you always need to be ready when the instructions aren't specific enough. 
"""


print("=" * 80)
print("Nothing should be printed above this line")

# Graders
# log = ["Larry", "Kurt"]
log = ["Larry", "Kurt", "Mark", "Dr. D"]

# Create Students
# I made this a year ago and in the middle of the night. The names have no meanings
s1 = Student("Kevin Bacon", "backevin")
s2 = Student("Jim Carrey", "themask")
s3 = Student("Kathryn Janeway", "voyager")
s4 = Student("James Kirk", "enterprise")
s5 = Student("Bill Gates", "gatesbill")

students = [s1, s2, s3, s4, s5]

extra_s = Student("Did you check this", "testing")

# Assignments
a1 = Assignment("A1")
a2 = Assignment("A2")
a3 = Assignment("A3")
a4 = Assignment("A4")
a5 = Assignment("A5")
a6 = Assignment("A6")

# Test GradeAssignment and Assignment
test_ga = GradeAssignment("NA", a1)
test_a = Assignment("NA")
test_a.set_grade("A")

# Grade System
grading_system = GradingSystem()

# Check code
# Check Grade System
print("Grading System Check")
print("Function {0} in Grading System: {1}".format("addGrader", "addGrader" in dir(GradingSystem)))
print("Function {0} in Grading System: {1}".format("addStudent", "addStudent" in dir(GradingSystem)))
print("Function {0} in Grading System: {1}".format("addAssignmentsToGraders", "addAssignmentsToGraders" in dir(GradingSystem)))
print("Function {0} in Grading System: {1}".format("gradeToStudent", "gradeToStudent" in dir(GradingSystem)))
print("Function {0} in Grading System: {1}".format("gradersNotDone", "gradersNotDone" in dir(GradingSystem)))
print("Instance variable {0} is type {1}: {2}".format("graders", dict, type(grading_system.graders) == dict))
print("Instance variable {0} is type {1}: {2}".format("grades", dict, type(grading_system.grades) == dict))
	

print("")
# Check Student
print("Student Type Check")
print("Function {0} in Student: {1}".format("addAssignment", "addAssignment" in dir(Student)))
print("Instance variable {0} is type {1}: {2}".format("name", str, type(s1.name) == str))
print("Instance variable {0} is type {1}: {2}".format("username", str, type(s1.username) == str))
print("Instance variable {0} is type {1}: {2}".format("assignments", list, type(s1.assignments) == list))
print("")
# Grade Grade Assignment
print("Grade Assignment Check")
print("Function {0} in Grade Assignment: {1}".format("gradeAssignment", "gradeAssignment" in dir(GradeAssignment)))
print("Instance variable {0} is type {1}: {2}".format("grader", str, type(test_ga.grader) == str))
print("Instance variable {0} is type {1}: {2}".format("assignment", Assignment, type(test_ga.assignment) == Assignment))
print("")

# Test Assignment 
print("Assignment Check")
print("Function {0} in Grading System: {1}".format("set_grade", "set_grade" in dir(Assignment)))
print("Function {0} in Grading System: {1}".format("get_grade", "get_grade" in dir(Assignment)))
print("Function {0} in Grading System: {1}".format("set_comment", "set_comment" in dir(Assignment)))
print("Function {0} in Grading System: {1}".format("get_comment", "get_comment" in dir(Assignment)))
print("Instance variable {0} is type {1}: {2}".format("a_name", str, type(test_a.a_name) == str))
print("Instance variable {0} is type {1}: {2}".format("grade", str, type(test_a.grade) == str))
print("Instance variable {0} is type {1}: {2}".format("comment", str, type(test_a.comment) == str))

print("")
print("=" * 80)


# Add graders to system
for g in log:
	grading_system.addGrader(g)

# Testing to make sure it works
for g in grading_system.graders:
	if g not in log:
		print("Grader {0} not found in {1}".format(g, log))
	if type(grading_system.graders[g]) != Stack:
		print("Grader {0} is not a stack".format(g))

for s in students:
	grading_system.addStudent(s)

if len(grading_system.grades.keys()) != len(students):
	print("Number of students in grading system does not match students in student list")

new_ga1 = GradeAssignment(log[0], a1)
new_ga2 = GradeAssignment(log[1], a2)
new_ga3 = GradeAssignment(log[1], a3)
new_ga4 = GradeAssignment(log[0], a4)
new_ga5 = GradeAssignment("Mark", a5)
new_ga6 = GradeAssignment("Dr. D", a6)
ga_list = [GradeAssignment("Mark", a1)]

gas = [new_ga1, new_ga2, new_ga3, new_ga4, new_ga5, new_ga6]
for ga in gas:
	try:
		grading_system.addAssignmentsToGraders(ga.grader, ga)
	except:
		print("Error inserting into grading system")
# Testing you can input a list
grading_system.addAssignmentsToGraders("Mark", ga_list)

gnd = grading_system.gradersNotDone()
if len(gnd) == 0:
	print("Graders not done should not be empty")
if len(gnd) != 4:
	print("Graders not done should have 4 items")

# Mark should have 2
if len(grading_system.graders["Mark"].s) != 2: # You should not do anything like this, I did this for testing
	print("There should be 2 GAs for Mark to grade")

# This is where I got tired, but it should work

ga_pop = grading_system.graders[log[0]].pop()
ga_pop.gradeAssignment("F", "Great work!!!")
grading_system.gradeToStudent(extra_s, ga_pop)
ga_pop.gradeAssignment("A", "Eh, seen better")
for s in students:
	grading_system.gradeToStudent(s, ga_pop)


if len(grading_system.grades) != len(students) + 1:
	print("Not enough students in grade book")


ga_pop = grading_system.graders[log[0]].pop() # Throw it away

for g in grading_system.grades:
	if len(grading_system.grades[g]) == 0:
		print("Student {0} should not be empty".format(g))

# print(grading_system.gradersNotDone())
if len(grading_system.gradersNotDone()) != 3:
	print("There should be one less grader, Larry")

print("=" *80)
print("If there is anything between the 2 equal lines, not done")
# for g in log: