courses = input()

courses_dict = {}

while not courses == "end":
    course_name, student_name = courses.split(" : ")
    if course_name not in courses_dict:
        courses_dict[course_name] = [student_name]
    else:
        courses_dict[course_name].append(student_name)
    courses = input()

for key, value in courses_dict.items():
    s_v = sorted(value)
    courses_dict[key] =s_v
sorted_courses = dict(sorted(courses_dict.items(), key=lambda kvp: len(kvp[1]), reverse=True))

for key, value in sorted_courses.items():
    print(f"{key}: {len(value)}")
    for every_el in value:
        print(f"-- {every_el}")



