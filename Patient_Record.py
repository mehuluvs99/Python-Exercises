def print_q(*a_list,**a_dict):
    for person in a_list:
        for patient,info in a_dict.items():
            if person == patient:
                print(person + ':')
                for key,value in info.items():
                    print(key + ' = ' + str(value))
                print()

q_list = ['Nelson', 'Tiffany','Robo','Michelle','Polly']
p_dict = {'Nelson':{'age':15,'weight':50},
          'Tiffany':{'age':25,'weight':60},
          'Sabrina':{'age':50,'weight':70},
          'Michelle':{'age':25,'weight':40},
         }

print('These waiting people are on the record.')
print_q(*q_list,**p_dict)
