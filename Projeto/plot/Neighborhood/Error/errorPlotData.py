import matplotlib.pyplot as plt
import numpy as np

data_b = [[8,11,11,9,10,9,12]]
data_c = [[7,12,10,7,10,11,11]]

data_d = [[12,11,11,10,13,9,16]]
data_e = [[8,7,10,11,9,10,12]]

ticks = ['', '', '', '','', '', '', '','', '', '', '', '', '']

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

plt.figure()

bpl = plt.boxplot(data_b, positions=np.array(range(len(data_b)))*2.0+2.0, sym='', widths=1.1)
bpr = plt.boxplot(data_c, positions=np.array(range(len(data_c)))*2.0+4.0, sym='', widths=1.1)
bps = plt.boxplot(data_d, positions=np.array(range(len(data_d)))*2.0+6.0, sym='', widths=1.1)
bpt = plt.boxplot(data_e, positions=np.array(range(len(data_e)))*2.0+8.0, sym='', widths=1.1)

set_box_color(bpl, '#D7191C') 
set_box_color(bpr, '#2C7BB6')
set_box_color(bps, '#2ca25f') 
set_box_color(bpt, '#8856a7')


# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#D7191C', label='Gaussian Manhattan 34x34')
plt.plot([], c='#2C7BB6', label='Gaussian Manhattan 38x38')
plt.plot([], c='#2ca25f', label='Bubble Manhattan 34x34')
plt.plot([], c='#8856a7', label='Bubble Manhattan 38x38')

plt.legend()

plt.xticks(range(0, len(ticks) * 2, 2), ticks)
plt.xlim(-2, len(ticks)*2)
plt.ylim(2, 16)
plt.tight_layout()
plt.savefig('boxcompare.png')
