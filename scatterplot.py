import matplotlib.pyplot as plt
import numpy as np
w=np.array(["Jan","feb","marc","apr","may","jun ","jul","aug","sep","oct","nov","dec",])
x=np.array([300,400,500,600,700,800,900,100,1100,1200,1300,1400])
y=np.array([3000,4000,5000,6000,7000,8000,9000,1000,11000,12000,13000,14000])
z=np.array([30000,40000,50000,60000,70000,80000,90000,10000,110000,120000,130000,140000])

plt.scatter(w,x,color="r",marker="*")

plt.scatter(w,y,color="g",marker="*")
plt.scatter(w,z,color="b",marker="*")

plt.xlabel("Month of the year")
plt.ylabel("Sales of segment")
plt.title("Sales Data")
