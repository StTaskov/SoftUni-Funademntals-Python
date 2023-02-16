count_of_students = int(input())
count_of_lectures = int(input())
start_bonus = int(input())

max_bonus_points = 0
# {total max_bonus_points} = {student attendances} / {course lectures} * (5 + {additional bonus})
current_student_attendances = 0


for student in range(1, count_of_students+1):
    student_attendances = int(input())
    current_bonus_point_for_student = student_attendances / count_of_lectures * (5 + start_bonus)
    if current_bonus_point_for_student > max_bonus_points:
        max_bonus_points = current_bonus_point_for_student
    if student_attendances > current_student_attendances:
        current_student_attendances = student_attendances

print(f"Max Bonus: {round(max_bonus_points)}.")
print(f"The student has attended {current_student_attendances} lectures.")
