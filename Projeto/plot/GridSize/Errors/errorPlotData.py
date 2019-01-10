import matplotlib.pyplot as plt
import numpy as np

data_a = [[20,20,21,18,16,23,22,19,19,16]]
data_b = [[19,23,21,24,16,23,22,21,23,20]]
data_c = [[18,16,17,18,19,21,18,21,21,22]]
data_d = [[20,23,20,19,19,24,18,17,18,19]]
data_e = [[21,16,19,17,18,16,18,17,14,18]]
data_f = [[16,18,16,15,19,18,19,16,14,18]]
data_g = [[21,15,17,14,15,15,19,19,17,18]]
data_h = [[15,18,16,19,16,16,18,18,20,19]]
data_i = [[18,21,16,14,16,17,17,19,11,14]]
data_j = [[17,19,11,15,15,17,16,17,20,21]]
data_k = [[14,16,16,16,15,17,15,15,17,18]]
data_l = [[14]]
#data_m = [[3,1,5]]
#data_n = [[4,1,3]]
#data_o = [[4,1,2]]

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
#bpc = plt.boxplot(data_m, positions=np.array(range(len(data_m)))*2.0+18.0, sym='', widths=0.8)
#bpd = plt.boxplot(data_n, positions=np.array(range(len(data_n)))*2.0+19.6, sym='', widths=0.8)
#bpe = plt.boxplot(data_o, positions=np.array(range(len(data_o)))*2.0+21.2, sym='', widths=0.8)

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
#set_box_color(bpc, '#e34a33')
#set_box_color(bpd, '#fdbb84')
#set_box_color(bpe, '#9ebcda')

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
#plt.plot([], c='#e34a33', label='ABC13')
#plt.plot([], c='#fdbb84', label='ABC14')
#plt.plot([], c='#', label='ABC15')

plt.legend()

plt.xticks(range(0, len(ticks) * 2, 2), ticks)
plt.xlim(-2, len(ticks)*2)
plt.ylim(0, 26)
plt.tight_layout()
plt.savefig('boxcompare.png')
