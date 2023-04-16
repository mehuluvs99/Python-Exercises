import random

def get_char(char_list,number):
    temp_list = []
    for i in range(number):
        temp_list.append(random.choice(char_list))
    return temp_list

while True:
    num_char = int(input('Numner of characters in your password: '))
    num_upper = int(input('At least how many uppercase letters: '))
    num_lower = int(input('At least how many lowercase letters: '))
    num_digits = int(input('At least how many digits : '))
    num_symbols = int(input('At least how many symbols: '))
    if num_char<num_upper+num_lower+num_digits+num_symbols:
        print('The character number do not match.')
    else:
        break

upper_list = [chr(i) for i in range(65,65+26)]
upper_char = get_char(upper_list,num_upper)
lower_list = [chr(i) for i in range(97,97+26)]
lower_char = get_char(lower_list,num_lower)
digit_list = [str(i) for i in range(0,10)]
digit_char = get_char(digit_list,num_digits)
symbols_list = [chr(i) for i in range(32,48)]
symbols_list += [chr(i) for i in range(58,65)]
symbols_list += [chr(i) for i in range(91,97)]
symbols_list += [chr(i) for i in range(123,127)]
symbol_char = get_char(symbols_list,num_symbols)

num_unfilled_chars = num_char - num_upper - num_lower - num_digits - num_symbols
whole_list = upper_list + lower_list + digit_list + symbols_list
remaining_char = get_char(whole_list,num_unfilled_chars)

password = upper_char+lower_char+digit_char+symbol_char+remaining_char
random.shuffle(password)
password = ''.join(password)
print(password)
