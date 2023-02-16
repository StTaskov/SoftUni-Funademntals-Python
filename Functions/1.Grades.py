def corresponding_grade_in_words(grades_with_num):
    if 2.00 <= grades_with_num <= 2.99:
        return 'Fail'
    elif 3.00 <= grades_with_num <= 3.49:
        return "Poor"
    elif 3.50 <= grades_with_num <= 4.49:
        return "Good"
    elif 4.50 <= grades_with_num <= 5.49:
        return "Very good"
    elif 5.50 <= grades_with_num <= 6.00:
        return "Excellent"


grade_like_num = float(input())
result = corresponding_grade_in_words(grade_like_num)
print(result)
