import random
#new_dict = {new_key:new_value for (key, value) in dict.items() if this_is_true}
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student:random.randint(1, 100) for student in names}
passed_students = {student:score for (student, score) in student_scores.items() if score > 59}
print(student_scores)
print(passed_students)