#check how many numbers are odd and how many numbers are even

odd_count=0
even_count=0

#loop started
for i in range(0,100):
    if i % 2 ==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1

#output
print(f"number of Odd numbers {odd_count} & number of Even Numbers {even_count}")