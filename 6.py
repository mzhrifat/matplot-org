
import matplotlib.pyplot as plt
import numpy as np

# Data setup
data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)

# Currency formatter
def currency(x, pos):
    """Format ticks as currency"""
    if x >= 1e6:
        return f'${x*1e-6:1.1f}M'
    else:
        return f'${x*1e-3:1.0f}K'

# Second plot with vertical line for mean
fig, ax = plt.subplots(figsize=(8, 8))
ax.barh(group_names, group_data)
plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

# Adding a vertical line for group mean
ax.axvline(group_mean, ls='--', color='r')

# Annotate new companies
for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize=10,
            verticalalignment="center")

# Adjust title position and plot formatting
ax.title.set(y=1.05)
ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')
ax.xaxis.set_major_formatter(currency)
ax.set_xticks([0, 25e3, 50e3, 75e3, 100e3, 125e3])
fig.subplots_adjust(right=.95)  # Adjust the right margin slightly

# Show the plot
plt.show()
