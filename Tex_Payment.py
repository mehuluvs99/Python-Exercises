class Person:
    def __init__(self,id_number):
        self.id_number = id_number
    def pay_tax(self,taxable_income,tax_rate):
        tax = taxable_income * tax_rate
        print('The tax is $ '+ str(tax))
        return tax

class Businessman(Person):
    def pay_tax(self, taxable_income,business_allowance,tax_rate):
        tax = (taxable_income - business_allowance) * tax_rate
        print('The tax is $ '+ str(tax))
        return tax

class Employee(Person):
    def refund_tax(self,amount):
        print('The refund is $ '+ str(amount))
        return amount

gary_businessman=Businessman('A123456')
gary_tax=gary_businessman.pay_tax(60000,8000,0.3)
ivy_self_emplyed = Person('T456548')
ivy_tax = ivy_self_emplyed.pay_tax(30000,0.25)
bobby_employee = Employee('K656689')
bobby_tax = bobby_employee.pay_tax(40000,0.2)
bobby_refund = bobby_employee.refund_tax(2000)