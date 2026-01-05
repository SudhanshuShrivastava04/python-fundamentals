print("\nSTUDENT PERFORMANCE ANALYZER\n")

names = input("\nEnter student names seperated by space\n")
marks = input("\nEnter students's marks in same order you entered names and seperated by space\n")
cut_off = float(input("\nEnter Passing Criteria\n"))

names = names.split()
marks = list(map(float, marks.split()))

if len(names) == len(marks):
    pass
else:
    print("Invalid Inputs")
    exit()

student_marks = dict(zip(names, marks))

print("\n STUDENT DATA \n")

for name, mark in student_marks.items():
    print(f"{name} : {mark}")

total_students = len(student_marks)
total_marks = sum(student_marks.values())
highest = max(student_marks.values())
lowest = min(student_marks.values())
average = round((total_marks/total_students), 2)

print("\n BASIC STATS \n")
print(f"Total Students: {total_students}")
print(f"Total Marks: {total_marks}")
print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")
print(f"Avg Marks: {average}")


print("\n RANKING \n")
sorted_students = sorted(student_marks.items(), key=lambda x: x[1], reverse=True)

for rank, (name, mark) in enumerate(sorted_students, start=1):
    print(f"Rank {rank}: {name} - {mark}")

print("\n PASS/FAIL ANALYSIS \n")

pass_std = dict(filter(lambda x: x[1] >= cut_off, student_marks.items()))
fail_std = dict(filter(lambda x: x[1] < cut_off, student_marks.items()))

pass_cnt = len(pass_std)
fail_cnt = len(fail_std)

pass_perc = round((pass_cnt/total_students) * 100, 2)
fail_perc = round((fail_cnt/total_students) * 100, 2)

print(f"Passed Students ({pass_cnt}): {list(pass_std.keys())}")
print(f"Failed Students ({fail_cnt}): {list(fail_std.keys())}")
print(f"Passing %: {pass_perc}%")
print(f"Failing %: {fail_perc}%")

choice = input("\nDo you want to give grace marks? (yes/no): ").lower()

if choice == "yes":
    grace = float(input("Enter grace marks to add: "))

    student_marks = dict(
        map(lambda x: (x[0], x[1] + grace), student_marks.items())
    )

    print("\nUPDATED MARKS AFTER GRACE\n")
    for name, mark in student_marks.items():
        print(f"{name} : {mark}")

    pass_std = dict(filter(lambda x: x[1] >= cut_off, student_marks.items()))
    fail_std = dict(filter(lambda x: x[1] < cut_off, student_marks.items()))

    pass_count = len(pass_std)
    fail_count = len(fail_std)

    pass_percent = round((pass_count / total_students) * 100, 2)
    fail_percent = round((fail_count / total_students) * 100, 2)

    print("\nPASS / FAIL AFTER GRACE\n")
    print(f"Passed Students ({pass_count}): {list(pass_std.keys())}")
    print(f"Failed Students ({fail_count}): {list(fail_std.keys())}")
    print(f"Passing %: {pass_percent}%")
    print(f"Failing %: {fail_percent}%")

else:
    print("\nNo grace marks applied.")

print("\nANALYSIS COMPLETE")


