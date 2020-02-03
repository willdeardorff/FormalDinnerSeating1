#family_dinner.py
#Jan_19_2020
#Will Deardorff

import random

# from stackoverflow...
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

student = []
waiter = []
left_over = []
kitchen = []
at_table = []

try:
    with open("Dinner Seating - Student List 2018-19 4.csv") as student_file:
       for line in student_file:
           #find second ',' and store the first and last names only in student list
            npos = find_nth(line,',',2)
            if npos > 0:
                name = line[:npos]
                #print(name)
                student.append(name)


except IOError as err:
    print("Error" + str(err))

num_student = len(student)
print(str(num_student))

waiter = random.sample(student,31)
print('number of waiters = ' + str(len(waiter)))


left_over = list(set(student).difference(set(waiter)))
num_left = len(left_over)
print(str(num_left))


kitchen = random.sample(left_over,7)
num_kitchen = len(kitchen)
print(str(num_kitchen))

at_table = list(set(left_over).difference(set(kitchen)))
print(str(len(at_table)))

try:
    with open ('seat.csv','w') as output_file:
        for each_student in kitchen:
            print(each_student + ',Kitchen' , file=output_file)
        counter = 1
        for each_student in waiter:
            scounter = str(counter)
            print(each_student + ',' + 'W' + scounter.zfill(2), file=output_file)
            counter = counter + 1
            if counter > 31:
                counter = 1
        for each_student in at_table:
            print(each_student + ',' + str(counter), file=output_file)
            counter = counter + 1
            if counter > 31:
                  counter = 1
except IOError as err:
    print ('IO Error writing student file: ' + str(err))



