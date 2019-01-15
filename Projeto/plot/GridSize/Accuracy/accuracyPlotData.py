import matplotlib.pyplot as plt
import numpy as np

data_a = [[0.9212,0.9128,0.917,0.9212,0.9212,0.9128,0.917,0.9212,0.9244,0.9186]]
data_b = [[0.9255,0.9249,0.9228,0.9339,0.9186,0.9239,0.9323,0.9276,0.9355,0.9234]]
data_c = [[0.9387,0.9371,0.9408,0.9329,0.9397,0.9345,0.9292,0.9477,0.9434,0.9255]]
data_d = [[0.9397,0.9403,0.9392,0.9477,0.9434,0.9424,0.9487,0.9434,0.9424,0.944]]
data_e = [[0.9445,0.9556,0.9514,0.9567,0.9503,0.9493,0.9482,0.9477,0.9641,0.9487]]
data_f = [[0.9641,0.9567,0.9582,0.9593,0.9535, 0.9487,0.9556,0.9619,0.9535,0.953]]
data_g = [[0.9561,0.9619,0.9625,0.9672,0.9609,0.9567,0.9556,0.9598,0.9598,0.9572]]
data_h = [[0.9609,0.9582,0.9688,0.9635,0.9651,0.9646,0.9588,0.9667,0.9598,0.9593]]
data_i = [[0.963,0.9567,0.963,0.9678,0.9662, 0.9704,0.9688,0.9593,0.9656,0.9651]]
data_j = [[0.9672,0.9683,0.9704,0.972,0.972,0.9678,0.9752,0.9604,0.9651,0.9683]]
data_k = [[0.972,0.9651,0.9672,0.9704,0.973,0.9736,0.9699,0.9693,0.9704,0.9699]]
data_l = [[0.9715,0.9704,0.973,0.9741,0.9683,0.9746,0.9783,0.9741,0.972,0.9767]]
data_m = [[0.9741,0.972,0.9741,0.973,0.972,0.9704,0.9757,0.9693,0.9757,0.9746]]
data_n = [[0.9767,0.9736,0.9715,0.9762,0.9762,0.9804,0.9693,0.9773,0.9778,0.9746]]
data_o = [[0.9767,0.9826,0.9789,0.9783,0.9757,0.9736,0.9636,0.9616,0.972,0.9789]]

ticks = ['', '', '', '','', '', '', '','', '', '', '', '', '']

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

plt.figure()

bpl = plt.boxplot(data_a, positions=np.array(range(len(data_a)))*2.0-1.0, sym='', widths=0.8)
bpr = plt.boxplot(data_b, positions=np.array(range(len(data_b)))*2.0+0.5, sym='', widths=0.8)
bps = plt.boxplot(data_c, positions=np.array(range(len(data_c)))*2.0+2.0, sym='', widths=0.8)
bpt = plt.boxplot(data_d, positions=np.array(range(len(data_d)))*2.0+3.6, sym='', widths=0.8)
bpu = plt.boxplot(data_e, positions=np.array(range(len(data_e)))*2.0+5.2, sym='', widths=0.8)
bpv = plt.boxplot(data_f, positions=np.array(range(len(data_f)))*2.0+6.8 , sym='', widths=0.8)
bpx = plt.boxplot(data_g, positions=np.array(range(len(data_g)))*2.0+8.4, sym='', widths=0.8)
bpw = plt.boxplot(data_h, positions=np.array(range(len(data_h)))*2.0+10.0, sym='', widths=0.8)
bpy = plt.boxplot(data_i, positions=np.array(range(len(data_i)))*2.0+11.6, sym='', widths=0.8)
bpz = plt.boxplot(data_j, positions=np.array(range(len(data_j)))*2.0+13.2, sym='', widths=0.8)
bpa = plt.boxplot(data_k, positions=np.array(range(len(data_k)))*2.0+14.8, sym='', widths=0.8)
bpb = plt.boxplot(data_l, positions=np.array(range(len(data_l)))*2.0+16.4, sym='', widths=0.8)
bpc = plt.boxplot(data_m, positions=np.array(range(len(data_m)))*2.0+18.0, sym='', widths=0.8)
bpd = plt.boxplot(data_n, positions=np.array(range(len(data_n)))*2.0+19.6, sym='', widths=0.8)
bpe = plt.boxplot(data_o, positions=np.array(range(len(data_o)))*2.0+21.2, sym='', widths=0.8)

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
set_box_color(bpa, '#fa9fb5')
set_box_color(bpb, '#636363')
set_box_color(bpc, '#e34a33')
set_box_color(bpd, '#fdbb84')
set_box_color(bpe, '#9ebcda')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#D7191C', label='10x10')
plt.plot([], c='#2C7BB6', label='12x12')
plt.plot([], c='#2ca25f', label='14x14')
plt.plot([], c='#8856a7', label='16x16')
plt.plot([], c='#43a2ca', label='18x18')
plt.plot([], c='#a6bddb', label='20x20')
plt.plot([], c='#1c9099', label='22x22')
plt.plot([], c='#dd1c77', label='24x24')
plt.plot([], c='#000080', label='26x26')
plt.plot([], c='#00cccc', label='28x28')
plt.plot([], c='#fa9fb5', label='30x30')
plt.plot([], c='#636363', label='32x32')
plt.plot([], c='#e34a33', label='34x34')
plt.plot([], c='#fdbb84', label='36x36')
plt.plot([], c='#9ebcda', label='38x38')
plt.legend()

plt.xticks(range(0, len(ticks) * 2, 2), ticks)
plt.xlim(-2, len(ticks)*2)
plt.ylim(0.91, 0.99)
plt.tight_layout()
plt.savefig('boxcompare.png')
