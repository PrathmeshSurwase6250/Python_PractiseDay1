# Print "Hello World".
print("Hello World")
# Take your name as input and print a welcome message.
name = input("Enter Your name :")
# Take two numbers and print their sum.
num1 = int(input("Enter The 1st No. :"))
num2 = int(input("Enter The 2st No. :"))
# Take two numbers and perform +, -, *, /, %, //, **.
operator = input("Enter the Operator +, -, *, /, %, //, ** :")
match operator :
    case '+':
        print(num1+num2)
    case '-':
        print("num1-num2")
    case '/' :
        print(num1 /num2)
    case '*' : 
        print(num1 * num2)
    case '%' :
        print(num1 % num2)
    case '**':
        print(num1**num2)
    case '//':
        print(num1 //num2)
    case _ :
        print("invalid input")
        
        
# Convert Celsius to Fahrenheit.
celsius = 7
print('Fahrenheit' , (celsius *1.8)+32)

# Convert seconds into hours, minutes, and seconds.
second =20000
print('hrs :', second //3600  )
remaining_seconds = second % 3600
print('min:',  remaining_seconds / 60)
print('second :', remaining_seconds %60)
# Calculate the area of a circle.
print("Area of circle :" , 3.14*(num1*num1))
# Calculate the area and perimeter of a rectangle.
print("perimeter :" , 2*(num1 + num2))
# Calculate simple interest.
num3 = int(input("Enter the 3 No. :"))
print("Simple Interset : " , (num1 * num2 *num3) // 100)
# Swap two numbers.
swap1 = int(input("Enter the Swap Number 1:"))
swap2 = int(input("Enter the Swap Number 2:"))
swap1 = swap1 + swap2
swap2 = swap1 - swap2 
swap1 = swap1 - swap2 
print(swap1 , swap2)

# Check whether a number is positive, negative, or zero.
print('positive' if num1 > 0 else 'negative' if   num1 < 0 else 'zero' ) 

# Check whether a number is even or odd.
print('even' if num1 %2==0 else 'odd')
# Find the largest of two numbers.
print('num1' if num1 > num2 else 'num2')
# Find the largest of three numbers.
print('num1' if num1 > num2 and num1 > num3 else 'num2'if num2 > num3 and num2 > num1 else 'num3' )
# Check whether a year is a leap year.
leaf = int(input("Enter the year to check leaf year or not :"))
print('leaf' if leaf % 400 == 0 or (leaf % 4 == 0 and leaf % 100 != 0) else 'notLeaf')
# Check whether a person is eligible to vote.
vote = int(input("Enter the Age to Check Eligible or not :"))

print("You Can Vote" if vote > 18 else "You Can't Vote")
# Calculate grade based on marks.
marks1 = int(input("Enter the marks 1:"))
marks2 = int(input("Enter the marks 2:"))
marks3 = int(input("Enter the marks 3:"))
print('grade :' ((marks1+marks2+marks3)/100)*100)
# Check whether a character is a vowel or consonant.
char = 'a'
print('vowel' if 'a' ==char.lower() or 'o' == char.lower() or 'i' ==char.lower() or 'u' ==char.lower() or 'e' ==char.lower() else 'Consonant')

# Check whether a number is divisible by 5 and 11.
print('divisible' if num1 % 5 == 0 or num1 % 11 == 0 else 'Not Divisible'  )
# Create a simple calculator.
operator = input("Enter the Operator +, -, *, /, %, //, ** , C:")

match operator :
    case '+':
        print(num1+num2)
    case '-':
        print("num1-num2")
    case '/' :
        print(num1 /num2)
    case '*' : 
        print(num1 * num2)
    case '%' :
        print(num1 % num2)
    case '**':
        print(num1**num2)
    case '//':
        print(num1 //num2)
    case C :
        num1 = 0 
        num2 = 0
        
# Calculate electricity bill based on units.
wattage = int(input("Enter the wattage :"))
hrs = int(input("Enter the hrs :"))
print("bills : " (wattage + hrs)*3.14)
# Calculate BMI and categorize it.
weigth = int(input("Enter the weigth :"))
heigth = int(input("Enter the heigth :"))
print('BMI :'(weigth)//heigth*heigth)

# Check whether a number is a multiple of another number.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Multiple" if num1 % num2 == 0 else "Not multiple")
