#Generate Fibonacci series of N terms
n=int(input("Enter the number ="))
n1, n2 = 0, 1
count=0
print("Fibonacci Series:")
while count<n:
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    count+=1
    
    