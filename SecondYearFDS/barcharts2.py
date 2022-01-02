import matplotlib.pyplot as plt

data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(15, 4), sharey=True)
axs[0].bar(names, values)

fig.suptitle('Categorical Plotting')
plt.show()