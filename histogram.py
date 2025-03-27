
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import yticks

np.random.seed(1)
x=4+np.random.normal(0,1.5,200)

fig,ax=plt.subplots()

ax.hist(x,bins=8,linewidth=0.5,edgecolor="white")

ax.set(xlim=(0,8),xticks=np.arange(1,8),
        ylim=(0,56),yticks=np.linspace(0,56,9))

plt.show()