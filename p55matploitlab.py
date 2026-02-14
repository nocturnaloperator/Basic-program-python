import matplotlib.pyplot as plt
subjects = ['Maths', 'Science', 'English', 'Computer']
marks = [85, 90, 75, 95]
colors = ['cyan','purple','magenta','brown']
plt.pie(marks, labels=subjects, autopct='%1.1f%%',colors = colors)
plt.title("Marks Distribution of Student")
plt.show()