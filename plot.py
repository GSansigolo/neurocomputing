import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('iris2.csv')
t = df['inte']
s = df['erro']

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='Interações', ylabel='Erro')
ax.grid()

plt.show()
