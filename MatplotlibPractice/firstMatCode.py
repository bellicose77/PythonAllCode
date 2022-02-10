# line chart
import matplotlib.pyplot
from matplotlib import pyplot as plt
x=[5,2,9,4,1,6]
y=[10,8,4,2,9,7]
print(type(x))
#plt.plot(x,y)
#plt.show()

# bar chart
#plt.bar(x,y)
#plt.show()


# Histogram chart
# plt.hist(y)
# plt.show()

# Scarter Chart
# plt.scatter(x,y)
# plt.show()

# chart including labeling
plt.title("Tanscom Ltd.")
plt.xlabel("Number of Sales")
plt.ylabel("Time(Hour)")
# plt.scatter(x,y)
# plt.show()
#plt.plot(x,y)
plt.plot(x,y,'-.')
plt.show()
