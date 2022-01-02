import matplotlib.pyplot as plt
import numpy as np


labels = ['G1', 'G2', 'G3', 'G4', 'G5']women_means = [25, 32, 34, 20, 25]


x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects2 = ax.bar(x + width/2, women_means, width, label='')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Vaccinations')
ax.set_title('Vaccinations per 100 in SEARO')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()