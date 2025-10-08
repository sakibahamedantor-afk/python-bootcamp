#Ask the user for a number, and calculate the sum of all even numbers up to that number.
#user input
num=int(input("Input the number you want: "))

#set counter to 0
total=0

#Looping
for i in range(0,(num+1)):
    if i % 2 == 0:
        total = total + i

#output
print(f"Sum of All the even numbers in range of {num}, is {total}")