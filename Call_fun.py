import Operator as ol
import Handle as hn

my_num_list = [4,5,6,7,8,9]
my_name_list = ['Any','Sam','Ken','Gloria','Danny','Sanny']

ol.delete_names(my_num_list,'Sam')
print(my_num_list)

ol.add_names(my_name_list,'Arya',2)
print(my_name_list)

my_sum = hn.add_number(my_num_list,1,5)
print(my_sum)

my_ave = hn.get_mean(my_num_list, 1 ,5)
print(my_ave)