input_string = input('Enter the temperature in Celsius: ')

while input_string != 'q':
    celsius = float(input_string)
    fahrenheit = celsius * 9/5 + 32
    print('The temperature in Fahrenheit is:', fahrenheit)
    input_string = input('Enter the temperature in Celsius: ')

# for this exercise you cannot use a for loop
# to use a for loop you should know the number of iterations in advance

