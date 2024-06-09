#Assignment Class for OOP
import CRN
class Assignments(CRN.Assignments):
    def __init__(self, name, type, due_date, description) -> None:
        self.name = name
        self.weight = type
        self.due_date = due_date
        self.description = description
