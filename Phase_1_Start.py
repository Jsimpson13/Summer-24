#Phase 1 Summer 24 Project

import CRN






def create_crn():
    name = input("What is the name of the class?: ")
    credit = input("How many credit hours is this class worth?: ")
    crn = input("What is the Course Regitration Number for this Class?: ")
    a = CRN.CRN(name, credit, crn, {})
    return a

    
    


a = create_crn()
CRN.create_assignment(a.assignment_list)
print(a)



