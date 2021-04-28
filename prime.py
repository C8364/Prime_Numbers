   ### Prime Numbers

n = int(input("Enter a number to learn if it is a 'Prime Number': "))
count = 0

for i in range(1, n+1) :
    if n % i == 0 :
        count += 1
if (n == 0) or (n == 1) or (count >=3) :
    print(n, "is NOT a 'Prime Number'.")
else:
    print(n, "is a 'Prime Number'.")
