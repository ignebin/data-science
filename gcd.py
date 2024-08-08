def gcd(a,b):
    while b!=0:
        a,b = b, a % b
    return a
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
result = gcd(num1,num2)
print(f"The GCD of {num1} and {num2} is {result}")

"""
Enter the first number:10
Enter the second number:50
The GCD of 10 and 50 is 10

"""
