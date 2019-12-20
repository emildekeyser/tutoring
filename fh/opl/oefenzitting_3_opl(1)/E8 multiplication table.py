LARGEST_NUMBER = 12

# print the first row
# \t stands for the tab character
print('', end='\t')
for column in range(1, LARGEST_NUMBER + 1):
    print(column, end='\t')
#go to the next line
print()

for row in range(1, LARGEST_NUMBER + 1):
    print(row, end='\t')
    for column in range(1, LARGEST_NUMBER + 1):
        print(row * column, end='\t')
    print()
