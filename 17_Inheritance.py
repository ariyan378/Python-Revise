class University:
    def __init__(self,name):
        self.name=name

class Cse(University):#Inheritance happens here
    def __init__(self,name , department):
        super().__init__(name)
        self.department = department
        
    def intro(self):
        
        return f"Department Name [{ self.department}] and University Name [{self.name}] "  
         
cse = Cse('Daffodil International University' , 'Cse')
print(cse.intro())  
        