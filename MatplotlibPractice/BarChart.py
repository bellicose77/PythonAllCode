from  matplotlib import  pyplot as plt
y=['one','two','three','four','five','six']
x=[5, 24, 35, 67, 12,18]
plt.title("Horizontal Graph")
#plt.bar(x,y)

plt.barh(y,x)
plt.show()
