# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
contador = 0
total = 0
for i in student_heights:
    contador += 1
    total += i

average = round(total / contador)

print(f"The average height of the students is {average}cm")

