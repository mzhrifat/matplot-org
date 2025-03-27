import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

x=np.arange(0,10,2)
a=[1,1.25,2,2.75,3]
b=[1,1,1,1,1]
c=[2,1,2,1,2]
y=np.vstack([a,b,c])

fig,ax=plt.subplots()
ax.stackplot(x,y)

ax.set(xlim=(0,8),xticks=np.arange(1,8),
       ylim=(0,8),yticks=np.arange(1,8))
fig.savefig('stackplot.png',format='png')
#plt.show()