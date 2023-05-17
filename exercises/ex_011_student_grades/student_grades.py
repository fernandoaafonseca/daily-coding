student_scores = {'Harry': 81,
'Ron': 78,
'Harmione': 99,
'Draco': 74,
'Neville': 62}

student_grades = {}

for item in student_scores:
	if student_scores[item] >= 90:
		student_grades[item] = 'Oustanding'
	elif student_scores[item] >= 81:
		student_grades[item] = 'Exceeds expectations'
	elif student_scores[item] >= 71:
		student_grades[item] = 'Acceptable'
	else:
		student_grades[item] = 'Fail'

print(student_grades)