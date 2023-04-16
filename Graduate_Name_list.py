black_list = ['Susan','John','Michael','Robert']
num_students = int(input('Enter number of student: '))
student_list = []
white_list = []

for student in range(num_students):
    prompt = input('Input a name: ')
    while prompt == '':
        prompt= input('input a non-empty name: ')
    student_list.append(prompt)

for student in student_list:
    if student not in black_list:
        white_list.append(student)
print('These '+str(len(white_list))+ ' student are allowed to graduate.')
print(*sorted(white_list),sep='\n')

