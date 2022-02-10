from  matplotlib import  pyplot as plt
x = ['A', 'B', 'C', 'D']

y1 = [10, 20, 10, 30]

y2 = [20, 25, 15, 25]
plt.bar(x, y1, color='r')
plt.bar(x, y2, bottom=y1, color='b')
plt.show()