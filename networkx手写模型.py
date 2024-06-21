import networkx as nx
import matplotlib.pyplot as plt
import EoN
import random,copy
import fc
import G_calc_model as gcalc
####创建仿真图结构
N = 100
M = 3
####ER均匀图创建
ER = nx.gnm_random_graph(N, M*N)
####BA异质图创建
BA=nx.barabasi_albert_graph(N, M)
####二维方格图创建
Grid=nx.grid_2d_graph(10,10, periodic=False)
####
#SIS(ER,comment='ER')
#nx.draw(ER,alpha=0.6, with_labels=True)
#plt.show()

G=ER
#初始化
Initial_infection_rate=0.1
for n in G.nodes():#遍历结点
    if random.random()<Initial_infection_rate:
        G.nodes[n]['state']='i'#初始状态为感染
    else:
        G.nodes[n]['state']='s'#初始状态为健康

G0=copy.deepcopy(G)#放结果
timex=200
pop_rate=[]
for i in range(timex):
    pop_rate+=[gcalc.statis_people_label(G0)]
    G0=gcalc.sis_step(G0,recovery_probability=0.2,contact_infec_Prob=0.05)

fc.plot(pop_rate,k=1)

