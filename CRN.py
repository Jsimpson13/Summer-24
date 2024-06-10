#CRN Class for OOP
import Assignments
class CRN: 
    def __init__(self, name, credit, crn, assignment_list):
        self.name = name 
        self.credit = credit 
        self.crn = crn
        self.assignment_list = assignment_list
    
def create_assignment(assignment_list):
    name = input("What is the name of the assignment?: ")
    category = input("What category does this assignment fall under?: ")
    due_date = input("When is this Assignment due?: ")
    description = input("Provide a brief description of the assignment: ")
    temp =  Assignments.Assignments(name, category, due_date, description)
    assignment_list[name] = temp
        
    
        
        