numberOfRows = int(input("Enter the number of Rows: "))
for i in range(0,numberOfRows):
    
    for j in range(0, numberOfRows-i-1):
        print(end=" ")
    
    for j in range(0, i+1):
        print("*", end = " ")

    print()

