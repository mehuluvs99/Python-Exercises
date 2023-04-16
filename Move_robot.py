

class Robot:
    def __init__(self,instruction_file):
        self.instruction_file = instruction_file
        self.instruction_list = None
    def write_instruction(self):
        f = open(self.instruction_file,'w')
        while True:
            movement_x = input("Enter horizontal movement , or q to quit: ")
            if movement_x == 'q':
                break
            movement_y = input("Enter Vertical movement , or q to quit: ")
            if movement_y == 'q':
                break
            # store x and y movement alternately on separate lines
            # write both x and y movement when both are received

            f.write(movement_x + '\n')
            f.write(movement_y + '\n')

        f.close()
    def read_instructions(self):
        try:
            f=open(self.instruction_file,'r')
        except FileNotFoundError as error:
            print(error)
        else:
            #store (movements + '\n') as elements in a list
            self.instruction_list = f.readlines()
            f.close()
    def get_location(self):
        position_x,position_y = 0,0
        distance_x,distance_y = 0,0
        self.read_instructions()
        if self.instruction_file != None:
            for data in self.instruction_list:
                # exclude "\n" at the end of the movement
                temp = data[:-1]
                #get x movement from odd line numbers
                if self.instruction_list.index(data) % 2 == 0:
                    position_x += float(temp)
                    distance_x += abs(float(temp))
                else:
                    #get y movement from even line numbers
                    position_y += float(temp)
                    distance_x += abs(float(temp))
        return position_x,position_y,distance_x,distance_y

robot_1 = Robot('robot_1.txt')
robot_1.write_instruction()
pos_x,pos_y,dis_x,dis_y = robot_1.get_location()
print("The robot is finally at "+ str(pos_x)+ ', '+ str(pos_y))
print('The robot has traveled a distance of '+ str(dis_x)+ ' horizontally '+ str(dis_y)+' vertically')
