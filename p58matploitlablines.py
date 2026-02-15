import matplotlib.pyplot as plt
roll_no = [1, 2, 3, 4, 5, 6]
marks = [55, 68, 72, 80, 85, 90]
plt.scatter(roll_no, marks)
plt.xlabel("Roll Number")
plt.ylabel("Marks")
plt.title("Scatter Plot of Roll No vs Marks")
plt.show()