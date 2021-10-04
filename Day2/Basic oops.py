#THIS PROJECT IS DONE IN OOPS CONCEPT OF INHERITANCE. 
#OOPS INHERITANCE

class Employee():
    raise_amt = 1.04
    def __init__(self , first , last , pay ):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + "@gmail.com"
    def fullname(self):
        return('{} {}'.format(self.first , self.last))    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)    

class Developer(Employee):
    #pass
    raise_amt = 1.10

    def __init__(self, first, last, pay , prog_lang):
        super().__init__(first, last, pay)
        #Employee.__init__(self ,first, last, pay )
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self , first , last , pay ,employees=None):
        super().__init__(first , last , pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self , emp):
        if emp not in self.employees:
            self.employees.append(emp)  
    def remove_emp(self , emp):
        if emp  in self.employees:
            self.employees.remove(emp)  
    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())  


# dev_1 = Employee("Hrishab" , "Shukla" , 50000)
# dev_2 = Employee("AAAN" , "DPPS" , 60000)
# print(dev_1.email)
# print(dev_2.email)
# dev_1 = Developer("Hrishab" , "Shukla" , 50000)
# dev_2 = Developer("AAAN" , "DPPS" , 60000)
# print(dev_1.email)
# print(dev_2.email)
#print(help(Developer))
#By applying help function we will get to know how developer class is inherits from employee class run and check it 
# dev_1 = Employee("Hrishab" , "Shukla" , 50000)
# dev_2 = Developer("AAAN" , "DPPS" , 60000)
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
# dev_2.apply_raise()
# print(dev_2.pay)

dev_1 = Developer("Hrishab" , "Shukla" , 50000 , 'python')
dev_2 = Developer("AAAN" , "DPPS" , 60000 , 'java')
# print(dev_1.email)
# print(dev_1.prog_lang)
mgr_1 = Manager('sue','smith' , 90000 , [dev_1])
#print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print(issubclass(Developer,Employee))
