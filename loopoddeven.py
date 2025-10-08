#Add only the even number from 0 to 100
total=0

#loop input
for i in range (0,101):
    #check if the number is even
    if i % 2 == 0:
        #print even numbers
        print(i)
        #add even number to total
        total = total+i

#output
print(f"Sum of all the even numebers from 0 to 100 is {total}")

#Add only the Odd number from 0 to 100
total=0

#loop input
for i in range (0,101):
    #check if the number is odd
    if i % 2 != 0:
        #print odd numbers
        print(i)
        #add even number to total
        total = total+i

#output
print(f"Sum of all the odd numebers from 0 to 100 is {total}")