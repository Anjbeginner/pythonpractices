# Check if a number entered by the user is odd or even.
num=int(input("Enter a value: "))
if(num%2==0):
    print("Even number")
else:
    print("odd number")
-----------------------------------------------------------------

#Swap the values of two variables without using a temporary variable.
a=90
b=770
a,b=b,a
print(a,b)
-------------------------------------------------------------------

#Write a program to check if a year is a leap year.
def isleapyear(year):
    if(year.lstrip('-').isnumeric()):
        year=int(year)
        if year%400==0:
            print("Leap year")
        elif (year%4==0 and year%100!=0):
            print("Leap year")
        else:
            print("Not a  leap year")
    else:
        print("Invalid Input!")
        
year=input("Enter a year :")   
print("The given year to check is : ", year)
isleapyear(year) 

-----------------------------------------------------------------------

#Print numbers from 1 to 10 using a for loop.
def printnum(num):
    if(num<=0):
        print("Invalid input")
    else:
        for i in range(1,num+1):
         print(i)

num=int(input("Enter a value: "))
printnum(num)
--------------------------------------------------------------------------
    
#Print all even numbers between 1 and input using a while loop.

#method1
def printevennum(num):
    if(num<=0):
        print("Invalid input")
    else:
        i=1
        while i<=num:
            if(i%2==0):
                print(i)
            i+=1
num=int(input("Enter a value: "))
printevennum(num)
#method2
def printevennum1(num):
    if(num<=0):
        print("Invalid input")
    else:
        i=2
        while i<=num:
                print(i) 
                i+=2
num1=int(input("Enter a value: "))
printevennum1(num1)
-------------------------------------------------------------------------

#Print the multiplication table of a number entered by the user.
def tables(value, num):
    i=1
    j=1
    if(value<=0 or num<=0):
        print("Invalid input")
    else:
        while i<=num:
            print(f"{value} * {i} = {value*i} ")
            i+=1

value=int(input("Which number table do you want? "))
num=int(input("Until which number you want the table to be? "))
tables(value, num)

----------------------------------------------------------------------
#Write a program to count the number of digits in a given number.

def numofdigits(num):
    print(len(str(abs(num))))

num=int(input())
numofdigits(num)

-----------------------------------------------------------------------
#Reverse a given number using a loop.

def reversenum(num):
    reverse=0
    while num!=0:
        dig=num%10
        reverse=(reverse*10)+dig
        num =num//10
    print(str(reverse))


num=int(input())
reversenum(num)

--------------------------------------------------------------------

#Check if a given string is a palindrome.

def palindrome(string):
    string=string.lower()
    rev=string[::-1]
    if string==rev:
        print("Palindrome")
    else:
        print("Not palindrome")



string=input("Enter string : ")
palindrome(string)

---------------------------------------------------------------------
#Count the number of vowels in a given string.







