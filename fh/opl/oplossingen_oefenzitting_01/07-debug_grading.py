grade1 = input('Grade /20: ')
grade2 = input('Grade /20: ')

grade_sum = grade1 + grade2
result_scale_100 = grade_sum * (100//2*20)
result_string = "Grade /100 = " + str(result_scale_100)
print(result_string)


"""
Mistakes:
input should be converted to int
wrong use of brackets
floating point division should be used instead of integer division
in formatting of string %f should be used instead of %i

Correction
grade1 = int(input('grade on 20: '))
grade2 = int(input('grade on 20: '))

grade_sum = grade1 + grade2
result_on_100 = grade_sum * (100/40)
print('Grade on 100 = ' + str(result_on_100))
"""
