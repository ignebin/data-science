import matplotlib.pyplot as plt
import numpy as np
x=np.array(['Walking','Cycling','Car','Bus','Train'])
y=np.array([250,150,230,300,400])
plt.title("Student Transportation")
plt.xlabel("Mode of Transport")
plt.ylabel("Frequency")
plt.bar(x,y,width=0.4)
plt.show()
