from matplotlib import  pyplot as plt
import numpy as np
from matplotlib import style
data = np.random.randn(50)
#plt.style.use('Solarize_Light2')
#plt.style.use("dark_background")
plt.style.use('ggplot')
plt.plot(data,':',1)
plt.show()