name = input("Enter student name: ")

marks = []

for i in range(1, 4):
    while True:
        try:
            mark = int(input(f"Enter marks for Subject {i} (0-100): "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Invalid marks! Enter a value between 0 and 100.")

        except ValueError:
            print("Please enter a valid whole number.")

total = sum(marks)
average = total / len(marks)

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
