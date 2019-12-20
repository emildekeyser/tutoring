set_A, set_B = set(), set()
num_N, num_M = 0, 0

while num_M >= num_N:
    print("Please input two integer numbers m < n.")
    num_M = int(input("m: "))
    num_N = int(input("n: "))


for num in range(num_M + 1, num_N):
    if num % 2 == 0:
        set_A.add(num)
    if num % 3 == 0:
        set_B.add(num)

print("There are",len(set_A.intersection(set_B)),"numbers are divisible by 6 between", num_M, "and", num_N)

print("There are",len(set_B.difference(set_A)),"odd numbers are divisible by 3 between",num_M,"and",num_N)

print("There are",len(set_A.union(set_B)),"numbers either divisible by 2 or by 3 between",num_M,"and", num_N)
