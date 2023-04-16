

#moved in east and north direction

class Journey:
    def __init__(self,*movement_list):
        self.travel = movement_list
    def is_round_trip(self):
        x_pos, y_pos = 0, 0
        
        for movement in self.travel:
            x_pos = x_pos + movement[0]
            y_pos = y_pos + movement[1]
        return x_pos == 0 and y_pos == 0

peter = [[90,50],[-80,-40],[-10,-10]]
peter_j = Journey(*peter)
print(peter_j.is_round_trip())

susan = [[50,40],[-60,10],[20,-70],[10,30]]
susan_j = Journey(*susan)
print(susan_j.is_round_trip())
