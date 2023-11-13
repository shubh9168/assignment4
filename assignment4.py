'''
#1 wap to print numbers from a given range
n1 = int(input("Start="))
n2 = int(input("End="))
n = n1+n2
for n in range (100,110):
    print(n)

#2 write a program to print all even numbers from a given range
n1 = int(input("Start="))
n2 = int(input("End="))
n = n1+n2
for n in range (10,20):
    if n%2==0:
        print(n)
    else:
        print(end=" ")

#3 wap to print the sum of all numbers from a given range
n1 = int(input("Start: "))
n2 = int(input("End: "))
sum_of_numbers = 0
for num in range(n1, n2 ,+ 1):
    sum_of_numbers += num
print(sum_of_numbers)

#4 wap to print all the character values of the given ascii value range from the user 
n1 = int(input("enter the start of range:"))
n2 = int(input("enter end of range:"))
if n1 < 0 or n2 < 0 or n1 > 90 or n2 > 90 or n1>n2:
    print("wrong input")
else:
    for ascii_num in range(n1,n2 + 1):
        character = chr(ascii_num)
        print("The character of ASCII values is ",ascii_num,character)

#5wap to print the number divisible by 7 but not divisible by 3 between 1 to 100
start_range=int(input("enter start of range:"))
end_range=int(input("enter end of range:"))
for i in range(start_range,end_range):
    if i%7==0 and i%3 !=0:
        print(i)

#6 wap to print all the ASCII value from a given character range.
start_range=input("enter start of range:")
end_range=input("enter end of range:")
start_ascii=ord(start_range)
end_ascii=ord(end_range)
if start_ascii > end_ascii:
    print("on output",end="")
else:
    for i in range(start_ascii,end_ascii, + 1):
        character=chr(i)
        print("ASCII value of",character,i)

#7 wap that print all positive number from a given range 
num1 = int(input("start="))
num2 = int(input("end="))
for i in range(num1,num2,+1):
    if i > 0:
        print(i)
    else:
        print(end="")

#8 wap to prints numbers which are divisible by 3 and 5 both in a given range 
num1 = int(input("start="))
num2 = int(input("end="))
for i in range(num1,num2,+1):
    if i%3==0 and i%5==0:
        print(i)
    else:
        print(end="")

#9 wap to print the count of all negative from a given range 
num1 = int(input("start="))
num2 = int(input("end="))
negative_num=0

for i in range(num1,num2 + 1):
    
    if i < 0:
        
        negative_num +=1
        
        print(negative_num)
'''
#10 wap program to calculate and print the product of the count of odd numbers within a given range
num1 = int(input("start="))
num2 = int(input("end="))
odd_count=0
product=1
for i in range(num1,num2):
    if i%2 != 0:
        odd_count += 1
for _ in range(odd_count):
    product *= odd_count
    print(product)

    
  
