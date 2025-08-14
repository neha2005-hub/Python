num = int(input("Enter a number : "))

a, b = 0, 1
found = False

while a <= num:
    if a == num:
        found = True
        break
    a, b = b, a + b

if found:
    print(num, "is in the Fibonacci series.")

else:
    print(num, "is not in the Fibonacci series.")
