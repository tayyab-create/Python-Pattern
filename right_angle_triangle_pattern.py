""" Program to print right triangle pattern """

""" Take input the number of rows """
numberOfRow = int(input("Enter number of rows: "))

for i in range(1, numberOfRow+1):
    for j in range (1,i+1):
        print("*", end = " ")
    print()
