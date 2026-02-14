import matplotlib.pyplot as plt
marks = [45, 55, 60, 62, 65, 70, 72, 75, 78, 80, 82, 85, 88, 90]
plt.hist(marks, bins=5)
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")
plt.title("Histogram of Marks")
plt.show()