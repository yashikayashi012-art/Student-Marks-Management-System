name = input("Enter student name: ")

marks1 = int(input("Enter marks in Subject 1: "))
marks2 = int(input("Enter marks in Subject 2: "))
marks3 = int(input("Enter marks in Subject 3: "))

total = marks1 + marks2 + marks3
average = total / 3

print("\n--- Student Report ---")
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", round(average, 2))

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 35:
    print("Grade: D")
else:
    print("Grade: F")
