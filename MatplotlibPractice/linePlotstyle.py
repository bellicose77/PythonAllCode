import matplotlib.pyplot as plt
import random as random

students = ["Jane","Joe","Beck","Tom","Sam",
			"Eva","Samuel","Jack","Dana","Ester",
			"Carla","Steve","Fallon","Liam","Culhane",
			"Candance","Ana","Mari","Steffi","Adam"]

marks=[]
for i in range(0,len(students)):
	marks.append(random.randint(0, 101))


plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("CLASS RECORDS")
plt.plot(students, marks, color = 'green',
		linestyle = 'solid', marker = 'o',
		markerfacecolor = 'red', markersize = 12)
plt.show()
