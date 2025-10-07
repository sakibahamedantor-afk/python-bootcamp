#take 2 numbers as input
a=int(input("First Number: "))
b=int(input("Second Number: "))

#Swapping Logic
temp=a
a=b
b=temp

print(f"Before the number was {b}, {a}")
print(f"Now the number is {a}, {b}")