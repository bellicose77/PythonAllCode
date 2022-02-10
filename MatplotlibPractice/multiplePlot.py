import matplotlib.pyplot as plt
# data to display on plots
x = [2, 4, 4, 8]
y = [3, 6, 7, 9]
plt.plot(x,y)
x1=[2, 4, 6, 8]
y1=[3, 5, 7, 9]
plt.plot(x1,y1,'m-.')
#plt.fill_between(y,y1,x,color='red',alpha=0.5)
plt.show()
