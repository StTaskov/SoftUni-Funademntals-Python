student_grade = int(input())

class_dict = {}

for _ in range(student_grade):
    student = input()
    grade = float(input())
    if student not in class_dict:
        class_dict[student] = []
        class_dict[student].append(grade)
    else:
        class_dict[student].append(grade)

filtered_students = {}
for each_student in class_dict:
    avg_grade_for_current_student = sum(class_dict[each_student]) / len(class_dict[each_student])
    if avg_grade_for_current_student >= 4.50:
        filtered_students[each_student] = avg_grade_for_current_student

filtered_students = dict(sorted(filtered_students.items(), key=lambda kvp: kvp[1], reverse=True))

for key, value in filtered_students.items():
    print(f'{key} -> {value:.2f}')