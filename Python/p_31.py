n=int(raw_input("Enter a number:"))
for i in range(1, n + 1):
    for j in range(i):
        print "*", 
    print  
for i in range(n - 1, 0, -1):
    for j in range(i):
        print "*",  
    print  
