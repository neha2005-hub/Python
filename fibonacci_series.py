num = int(input("Enter number of terms : "))

n1, n2 = 0, 1
count = 0

if num <= 0:
   print("Please enter a positive integer!")

else:
   print("Fibonacci series : ", end=" ")
   while count < num:
       print(n1, end=" ")
       nth = n1 + n2 
       n1 = n2
       n2 = nth
       count += 1
