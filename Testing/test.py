for row in range(11):
    for i in range(10 - row):
        print(" ", end=' ')
    for i in range(1, row ):
        print(i, end= " ")
    for i in range(i - 1, 0, -1):
        print(i, end=" ")
   
    print()
    
    

       