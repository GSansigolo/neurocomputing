import matplotlib.pyplot as plt
import numpy as np


data_b = [[0.972,0.9651,0.9672,0.9704,0.973,0.9736,0.9699,0.9693,0.9704,0.9699]]
data_c = [[0.9715,0.9704,0.973,0.9741,0.9683,0.9746,0.9783,0.9741,0.972,0.9767]]
data_d = [[0.9741,0.972,0.9741,0.973,0.972,0.9704,0.9757,0.9693,0.9757,0.9746]]
data_e = [[0.9767,0.9736,0.9715,0.9762,0.9762,0.9804,0.9693,0.9773,0.9778,0.9746]]
data_f = [[0.9767,0.9826,0.9789,0.9783,0.9757,0.9736,0.9636,0.9616,0.972,0.9789]]

data_g = [[0.9815,0.9804,0.9826,0.9804,0.9773,0.9804,0.982]]
data_h = [[0.9815,0.9804,0.9799,0.9757,0.9841,0.9847,0.9799]]
data_i = [[0.9868,0.9847,0.9852,0.9857,0.9836,0.9836,0.9868]]
data_j = [[0.9836,0.9868,0.9878,0.9815,0.9894,0.9847,0.9847]]
data_k = [[0.9868,0.9873,0.9884,0.9921,0.9894,0.9815,0.9836]]

ticks = ['', '', '', '','', '', '', '','', '', '', '', '', '']

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

plt.figure()

bpl = plt.boxplot(data_b, positions=np.array(range(len(data_b)))*2.0-1.0, sym='', widths=0.8)
bpr = plt.boxplot(data_c, positions=np.array(range(len(data_c)))*2.0+0.5, sym='', widths=0.8)
bps = plt.boxplot(data_d, positions=np.array(range(len(data_d)))*2.0+2.0, sym='', widths=0.8)
bpt = plt.boxplot(data_e, positions=np.array(range(len(data_e)))*2.0+3.6, sym='', widths=0.8)
bpu = plt.boxplot(data_f, positions=np.array(range(len(data_f)))*2.0+5.2, sym='', widths=0.8)
bpv = plt.boxplot(data_g, positions=np.array(range(len(data_g)))*2.0+6.8 , sym='', widths=0.8)
bpx = plt.boxplot(data_h, positions=np.array(range(len(data_h)))*2.0+8.4, sym='', widths=0.8)
bpw = plt.boxplot(data_i, positions=np.array(range(len(data_i)))*2.0+10.0, sym='', widths=0.8)
bpy = plt.boxplot(data_j, positions=np.array(range(len(data_j)))*2.0+11.6, sym='', widths=0.8)
bpz = plt.boxplot(data_k, positions=np.array(range(len(data_k)))*2.0+13.2, sym='', widths=0.8)

set_box_color(bpl, '#D7191C') 
set_box_color(bpr, '#2C7BB6')
set_box_color(bps, '#2ca25f') 
set_box_color(bpt, '#8856a7')
set_box_color(bpu, '#43a2ca')
set_box_color(bpv, '#a6bddb')
set_box_color(bpx, '#1c9099')
set_box_color(bpw, '#dd1c77')
set_box_color(bpy, '#000080')
set_box_color(bpz, '#00cccc')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#D7191C', label='Euclidean 30x30')
plt.plot([], c='#2C7BB6', label='Euclidean 32x32')
plt.plot([], c='#2ca25f', label='Euclidean 34x34')
plt.plot([], c='#8856a7', label='Euclidean 36x36')
plt.plot([], c='#43a2ca', label='Euclidean 38x38')
plt.plot([], c='#a6bddb', label='Manhattan 30x30')
plt.plot([], c='#1c9099', label='Manhattan 32x32')
plt.plot([], c='#dd1c77', label='Manhattan 34x34')
plt.plot([], c='#000080', label='Manhattan 36x36')
plt.plot([], c='#00cccc', label='Manhattan 38x38')
plt.legend()

plt.xticks(range(0, len(ticks) * 2, 2), ticks)
plt.xlim(-2, len(ticks)*2)
plt.ylim(0.94, 1)
plt.tight_layout()
plt.savefig('boxcompare.png')
