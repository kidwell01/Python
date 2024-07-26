# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

count = 0
total_height = 0
avg = 0
for height in student_heights:
  total_height += height
  count += 1
  avg = round(total_height / count)
print(f"total height = {total_height}")
print(f"number of students = {count}")
print(f"average height = {avg}")
  