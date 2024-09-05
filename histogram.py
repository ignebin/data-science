import matplotlib.pyplot as plt
import numpy as np
age=np.array([5,12,18,20,21,25,27,28,35,32,34,37,40,54,58,66,62,67,69,71,74, 80])
bins=[0,10,20,35,40,50,60,70]
plt.hist(age,bins=bins,edgecolor='r')
#plt.hist(age,bins=5,edgecolor='r')
plt.title("Age Distribution")
plt.xlabel("Age Ranges")
plt.ylabel("Frequency")
plt.show()
