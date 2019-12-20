#temperatures is a list we fill with temperatures the user provides.
temperatures = []
new_temperature = input("What temperature would you like to add?: ")
#Keep adding temperatures until the user enters the character 'q'.
while(new_temperature != 'q'):
    temperatures.append(int(new_temperature))
    new_temperature = input("What temperature would you like to add?: ")

#The list of temperatures has been provided. Now we sort this list using the selection sort algorithm.
#See lecture 7 for more information on this algorithm and other sorting algorithms.
for i in range(len(temperatures)):
    #Find the position of the minimum value in the remaining unsorted part of the list of temperatures.
    min_pos = i
    for j in range(i+1, len(temperatures)):
        if temperatures[j] < temperatures[min_pos]:
            min_pos = j
    #Swap the i-th value and the minimum value of the unsorted part of the list.
    temp = temperatures[min_pos]
    temperatures[min_pos] = temperatures[i]
    temperatures[i] = temp
#Print the resulting sorted list.
print(temperatures)