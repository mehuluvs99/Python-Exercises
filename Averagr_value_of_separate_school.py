

def get_average(a_list):
    total = 0
    for mark in a_list:
        total += mark
    average = total/len(a_list)
    return round(average,2)

def get_max(a_list):
    max_value = 0
    for mark in a_list:
        if mark > max_value:
            max_value = mark
    return max_value

mark_list = [[89,78,56,78,86,91,72,53,55],
            [68,65,72,83,89,66],
            [58,56,78,25,12,36,45,65]]

average_list = []
for group_list in mark_list:
    average_value = get_average(group_list)
    average_list.append(average_value)
max_average = get_max(average_list)
print('The highest average mark for the '+ str(len(mark_list))+' school is '+ str(max_average))
print('School '+ str(average_list.index(max_average)) + ' Gives the highest average.')
