# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
        # print(highest_score)

print(f"the hightest score in the calls is:{highest_score}")