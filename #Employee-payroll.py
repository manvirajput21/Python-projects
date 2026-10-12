#Employee Payroll system
class employee:
    def __init__(self,id, name,salary):
        self.name = name
        self.id = id
        self.salary = salary
        self.basic = 0
        self.allowance = 0
        self.deduction = 0
        self.history = []

    def display(self):
        print('EMP NAME "{} " EMP ID "{}" CURRENT SALARY "{}" '.format(self.name , self.id,self.salary))
    
emp = []
    
def add():
     name = input("ENTER EMPLOYEE NAME ")
     id = int(input("ENTER EMP ID"))
     salary=float(input("ENTER CURRENT SALARY"))
     for a in emp:
        if a.id == id:
            print("EMPLOYEE ID ALREADY EXISTS")
            return

     a = employee(id, name, salary)
     emp.append(a)
     print("EMPLOYEE ADDED SUCCESSFULLY")

def display():
    if len(emp)==0:
        print("NO ACCOUNT FOUND")
    else:
        for a in emp:
            a.display()

def search_emp(id):
    for a in emp:
        if a.id == id:
             return a
    return None
    
def salary_cal():
    id = int(input("ENTER EMP ID"))
    a= search_emp(id)
    if a.id ==id:
        basic =float(input("ENTER BASIC SALARY"))
        allowance = float(input("ENTER ALLOWANCE SALARY"))
        deduction = float(input("ENTER DEDUCTION SALARY"))
        a.basic = basic
        a.allowance = allowance
        a.deduction = deduction
        net_salary = basic+ allowance - deduction
        a.salary = net_salary
        a.history.append('NET SALARY"{}"'.format(net_salary))
       
        print("ACTUAL SALARY:", a.salary)
        print("EMPLOYEE NAME:", a.name)
        print("BASIC SALARY:", basic)
        print("ALLOWANCES:", allowance)
        print("DEDUCTIONS:", deduction)
        print("NET SALARY:", net_salary)
        return

    print("EMPLOYEE NOT FOUND")


def payslip():
    id = int(input("ENTER EMPLOYEE ID: "))

    for a in emp:
        if a.id == id:
            print("\n========== EMPLOYEE PAYSLIP ==========")
            print("EMPLOYEE NAME:", a.name)
            print("EMPLOYEE ID:", a.id)
            print("--------------------------------------")
            print("BASIC SALARY:", a.basic)
            print("ALLOWANCES:", a.allowance)
            print("DEDUCTIONS:", a.deduction)
            print("--------------------------------------")
            print("NET SALARY:", a.salary)
            print("======================================")
            return

    print("EMPLOYEE NOT FOUND")

def payroll_data():
    id = int(input("ENTER EMP ID: "))
    a = search_emp(id)

    if a:
        print("\n--- PAYROLL HISTORY ---")
        print("EMP NAME:", a.name)
        print("EMP ID:", a.id)

        if len(a.history) == 0:
            print("NO PAYROLL HISTORY FOUND")
        else:
            for net_salary in a.history:
                print("NET SALARY:", net_salary)
    else:
        print("EMPLOYEE NOT FOUND")
def main():
      while True:
        print("\n--- EMP PAYROLL SYSTEM ---")
        print("1. ADD EMP")
        print("2. DISPLAY  EMP")
        print("3. SEARCH EMP")
        print("4. CAL NET SALARY")
        print("5. PAYSLIP")
        print("7. PAYROLL DATA")
        print("8. EXIT")

        choice = input("ENTER YOUR CHOICE: ")

        if choice == '1':
            add()
        elif choice == '2':
            id = int(input("ENTER EMPLOYEE ID: "))
            a = search_emp(id)
            if a:
              a.display()
            else:
              print("EMPLOYEE NOT FOUND")
        elif choice == '3':
            search_emp()
        elif choice == '4':
            salary_cal()
        elif choice == '5':
            payslip()
        elif choice == '6':
            payroll_data()
        elif choice == '7':
            print("THANK YOU FOR USING OUR BANK")
            break
        else:
            print("INVALID CHOICE")


main()

         
            
            
            
            
            
            
            
                
    
    
    