class Employee:
    def __init__(self,basic_salary=500):
        self.basic_salary = basic_salary

class chef(Employee):
    def __init__(self,hourly_wage,hours,day):
        super().__init__(550)
        self.hourly_wage = hourly_wage
        self.hours = hours
        self.day = day
    
    def get_monthly_income(self):
        return self.hourly_wage * self.hours * self.day + self.basic_salary
    
class waiter(Employee):
    def __init__(self,monthly_salary,tips):
        super().__init__(600)
        self.monthly_salary = monthly_salary
        self.tips = tips

    def get_monthly_income(self):
        return self.monthly_salary + self.tips * 0.5 + self.basic_salary

class Cleaner(Employee):
    def __init__(self, monthly_salary, extra_hour, extra_hour_wage):
        super().__init__()
        self.monthly_salary = monthly_salary
        self.extra_hours = extra_hour
        self.extra_hours_wage = extra_hour_wage

    def get_monthly_income(self):
        return self.monthly_salary + self.extra_hours * self.extra_hours_wage + self.basic_salary


peter = chef(20,8,26)
peter_Salary = peter.get_monthly_income()
print("Peter's Salary : ",peter_Salary)

gary = waiter(3000,200)
gary_salary = gary.get_monthly_income()
print("Gary's Salary : ",gary_salary)

michael = Cleaner(3500,15,20)
michael_salary = michael.get_monthly_income()
print("Michael's Salary : ",michael_salary)

income = 20000
profit = income - peter_Salary - gary_salary - michael_salary
print("Net Profit : ",profit)