class Engineer:
    def __init__(self,licence_no):
        self.licence_no = licence_no
    def design_project(self):
        print("I am designing a project")

class SeniorEngineer(Engineer):
    def __init__(self,licence_no,num_project):
        super().__init__(licence_no)
        self.num_project = num_project

    def deal_project(self):
        print('I have got a project to do.')
        self.num_project += 1

class SeniorComputerEngineer(SeniorEngineer):
    def __init__(self,licence_no,num_project,current_project):
        super().__init__(licence_no,num_project)
        self.current_project = current_project

leslie = Engineer("AB1234")
leslie.design_project()

cindy = SeniorEngineer('MN5678',4)
cindy.deal_project()
print("Now Cindly Handle "+ str(cindy.num_project)+ ' project.')

terry = SeniorComputerEngineer('PQ34560', 6 , 'Network Connection')
print(terry.current_project)


