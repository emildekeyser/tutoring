#numbers is a list we fill with integers the user provides.
numbers = []
new_number = input("What number would you like to add?: ")
#Keep adding numbers until the user enters the character 'q'.
while(new_number != 'q'):
    numbers.append(int(new_number))
    new_number = input("What number would you like to add?: ")

#Print the provided list.
print("Input:", numbers)

#Make a copy of the list of numbers. This copy will be manipulated instead of the original list. The reason a copy is
#needed is that the comparison between neigbouring values has to be done using the original values, not values that are
#the result of replacement by neighbouring values. So, the original list of numbers will be used to get the original values.
numbers_copy = list(numbers)

#The algorithm does not have any effect on lists that have less than 2 elements. If we would remove this if-statement,
#the algorithm would result in an IndexError for lists of size 1.
if(len(numbers_copy) > 1):
    #Iterate through the copy of the list of numbers.
    for i in range(len(numbers_copy)):
        #if i is the first index
        if(i == 0):
            numbers_copy[i] = max(numbers[i], numbers[i+1])
        #if i is the last index
        elif(i == len(numbers_copy) - 1):
            numbers_copy[i] = max(numbers[i-1], numbers[i])
        else:
            numbers_copy[i] = max(numbers[i-1], numbers[i], numbers[i+1])

#Print the resulting list.
print("Output:", numbers_copy)