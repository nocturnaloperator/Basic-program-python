import matplotlib.pyplot as plt
roll_no = [1, 2, 3, 4, 5]
marks = [72, 85, 90, 68, 88]
color = ['Red','magenta','brown']
plt.bar(roll_no, marks, color=color)
plt.xlabel("Roll Number")
plt.ylabel("Marks")
plt.title("Marks of Students")
plt.show()