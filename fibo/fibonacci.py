def recur_fibo(m):
   if n <= 1:
       return m
   else:
       return(recur_fibo(m-1) + recur_fibo(m-2))

nterms = int(input("enter number"))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))