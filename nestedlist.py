#nestedlist practice

mark=[
    [85, 90, 78],
    [88, 76, 92],
    [90, 91, 85]
]

#Print all marks of the second student (the 2nd inner list).
print(mark[1])

#Print the first subject’s mark of the third student.
print(mark[2][0])

#Change one mark (any one).
mark[2][2]=78
print(mark)

#Print the entire list again.
for row in mark:
    for value in row:
        print(value, end = " ")
print()