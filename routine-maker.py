# Makes Routine automatically
# each duration is in mins

# defining the duration variables

class_duration = 30
break_duration = 60
lab_duration = 3 * class_duration

name_of_the_subjects = []
name_of_the_teachers = []

total_subjects = int(raw_input("How many subjects? "))
for i in range(total_subjects):
    name_of_the_subjects.append(raw_input("Names of these subjects? "))

total_teachres = int(raw_input("How many teachers? "))
for i in range(total_teachres):
    name_of_the_teachers.append(raw_input("Names of the teachers? "))

teacher_subject_pair = []

for i in range(total_teachres):
    for j in range(total_subjects):
        while True:
            ability = False
            ability = raw_input("Can " + name_of_the_teachers[i] + " teach " + name_of_the_subjects[j] + " [y/n] ? : ")
            print(ability)
            if ability == 'y':
                teacher_subject_pair.append(True)
                break
            elif ability == 'n':
                teacher_subject_pair.append(False)
                break
            else:
                continue

print(teacher_subject_pair)
