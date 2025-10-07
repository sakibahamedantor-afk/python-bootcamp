#grading system Write a program that:
#Takes a marks input from the user (0–100).
#Prints:
#“A+” if marks ≥ 80
#“A” if marks ≥ 70
#“B” if marks ≥ 60
#“C” if marks ≥ 50
#“Fail” otherwise.
#Use if / elif / else and comparison operators.

#taking input of marks
marks=float(input("Enter your Marks: "))

#funcotion
if marks>=80:
    print(f"A+")
elif marks>=70 and marks<80:
    print(f"A")
elif marks>=60 and marks<70:
    print(f"B")
elif marks>=50 and marks<60:
    print(f"C")
else:
    print(f"You have failed your Parents")