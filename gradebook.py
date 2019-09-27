grade_list = []
max_grade = 100
grade_counter = 0
grade_sum = 0

while True:
    grade = input("Enter a grade, type -1 to quit: ")

    if garde == -1:
            break
    else:
        if grade <= max_grade:
            grade_sum += grade
            grade_list.append(grade)
            grade_counter += 1
        else:
            print("Invalid grade, please try.")