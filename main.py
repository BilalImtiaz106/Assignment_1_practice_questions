#Calculate the area of rectangle
length=int(input("Enter the length"))
width=int(input("Enter the width"))
area=length*width
print("Area of rectangle is",area)

#Check number is even or odd
num = int(input("Enter the number"))
if num%2 == 0:
    print ("even")
else:
    print ("odd")

#Reversing the string 
a = input("Enter string:")
print (a[-1::-1])

#factorial of a number 
i = int(input("Enter number:"))
fac = 1
while (i>0):
    fac = fac*i
    i = i-1
print ("factorial=",fac)

#palindrome
a = input("Enter string:")
b =a[-1::-1]
if (a==b):
    print ("Palindrome string")
else:
    print ("Non- palindrome string ")

#Fibonacci series 
n = int(input("Enter the number:"))
x = 0
y = 1
z = 0
while (z<=n):
    print (z)
    x = y
    y = z
    z = x + y

# Largest number among 3 numbers 
a = int(input("Enter 1st num"))
b = int(input("Enter 2nd num"))
c = int(input("Enter 3rd num"))
if a > b and b > c:
    largest = a
elif b > a and b > c:
    largest = b
else:
    largest = c
print("largest among {} {} and {} is {}".format(a,b,c,largest))

#Simple interest 
a = int(input("Enter principle amount"))
b = float(input("Enter rate of interest"))
c = float(input (" Enter time in year"))
d = (a*b*c)/100
print ("Simple interest is",d)

# Celsius to Fahrenheit 
Celsius = int(input("Enter the temperature in Celsius "))
Fahrenheit = (Celsius*1.8) + 32
print ("Temperature in Fahrenheit is", Fahrenheit,"F")

# Median among three numbers 
a = int(input ("Enter the 1st num"))
b = int(input ("Enter the 2nd num"))
c = int(input ("Enter the 3rd num"))
print ("Median of the three numbers above is ")
if b<a and a<c:
    print (a)
elif c<a and a<b:
    print (a)
elif c<b and b<a:
    print (b)
elif a<b and b<c:
    print (b)
else:
    print (c)

# Count No.of words in string 
a = input ("Enter the string ")
strlist=a.split()
print(len(strlist))

# Sum of digits of a given number 
a = int(input ("Enter the number"))
sum = 0
while (a>0):
    sum = sum+a%10
    a=a//10
print ("sum of digits=",sum)

# Prime number:
n = int(input ("Enter number "))
count=0
i = 1
while (i<=n):
    if (n%i==0):
        count=count+1
    i= i+1
if count==2:
print("Prine number")
else:
    print("Not a prime number");