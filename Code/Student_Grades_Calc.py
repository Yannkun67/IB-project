def read_grades():
    with open("grades.txt") as f:
        lines = f.readlines()
        for line in lines:
            name, *grades = line.strip().split(',')

            try:
                grade_list = [int(g) for g in grades]  # May raise ValueError
                avg = sum(grade_list) / len(grade_list)  # May raise ZeroDivisionError

            except ValueError:
                print(f"Grading error found for {name}.")
                continue
            
            except ZeroDivisionError:
                print(f"No grades for {name}.")
                continue
            print(f"{name} - Average: {avg:.2f}")

read_grades()