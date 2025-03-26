
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import xlabel, ylabel

# কিছু মক ডেটা তৈরি করুন
t = np.arange(0.01, 10.0, 0.01)  # np.arrange() এর পরিবর্তে np.arange() ব্যবহার করুন
data1 = np.exp(t)
data2 = np.sin(2 * np.pi * t)

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')  # set এবং xlabel এর মধ্যে স্পেস ছিল, ঠিক করা হয়েছে
ax1.set_ylabel('exp', color=color)  # set এবং ylabel এর মধ্যে স্পেস ছিল, ঠিক করা হয়েছে
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)  # tick এবং params এর মধ্যে স্পেস ছিল, ঠিক করা হয়েছে

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('sin', color=color)  # set এবং ylabel এর মধ্যে স্পেস ছিল, ঠিক করা হয়েছে
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)  # tick এবং params এর মধ্যে স্পেস ছিল, ঠিক করা হয়েছে

fig.tight_layout()
plt.show()
