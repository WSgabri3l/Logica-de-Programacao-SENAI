def fat (n):

    if n <= 1:

        return 1 
    
    else:

        return n * fat (n - 1)
    
fat_num = int(input("Número: "))
print(fat(fat_num))