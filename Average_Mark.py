student = [['Annie',85,90,75],
            ['Bony', 85,35,45],
            ['Johny',55,65,45],
            ['Danny',65,35,66]
            ]

each_test_total = []
num_tests = len(student[0])-1
num_students = len(student)

for test_index in range(num_tests):
    each_test_total.append(0)
for student_index in range(num_students):
    for test_index in range(num_tests):
        each_test_total[test_index] += student[student_index][test_index + 1]

each_test_average = []
for test_index in range(num_tests):
    each_test_average.append(each_test_total[test_index] / len(student))
for test_index in range(num_tests):
    print('The average for test '+ str(test_index + 1)+ ' is ' + str(each_test_average[test_index]))
