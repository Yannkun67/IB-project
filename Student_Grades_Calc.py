def read_grades(filename):
    with open("grades.txt") as f:
        lines = f.readlines()
        for line in lines:
            name, *grades = line.strip().split(',')
            grade_list = [int(g) for g in grades]  # May raise ValueError
            avg = sum(grade_list) / len(grade_list)  # May raise ZeroDivisionError
            print(f"{name} - Average: {avg:.2f}")
read_grades("grades.txt")