car_plate = ['AB1234','AC4513','CV1214','AD5564','AD4869','LM4567','RE2315','RR2135']
odd_days = ['MO','WE','FR']
even_days = ['TU','TH','SA']
pass_list = []

today=input('Enter day of a week (sunday to saturday: ')
for plate in car_plate:
    last_digit = int(plate[-1])
    if today in odd_days and last_digit %2 !=0:
        pass_list.append(plate)
    elif today in even_days and last_digit % 2 ==0:
        pass_list.append(plate)
    elif today == 'SU':
        pass_list.append(plate)
print(*pass_list, sep='\n')
