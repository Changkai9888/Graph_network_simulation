import networkx as nx
import matplotlib.pyplot as plt
import EoN
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['font.family'] = 'Arial'
def SIS(G,tau = 0.5,gamma = 0.2,tmax=20, comment=""):
    ####SIS仿真
    #tau：传播到达率
    #gamma：节点治愈率
    #tmax：仿真时间长度
    t, S, I = EoN.fast_SIS(G, tau=tau, gamma=gamma, tmax = tmax)
    if comment=="":
        plt.plot(t, S, color = 'r', label='S')
        plt.plot(t, I, color = 'b', label='I')
    else:
        plt.plot(t, S, label='S'+"/ "+comment)
        plt.plot(t, I, label='I'+"/ "+comment)
    plt.legend(loc=0)
    plt.xlabel("Time")
    plt.ylabel("individuals")
def SIR(G,tau = 0.5,gamma = 1.0,rho = 0.05, tmax=20, comment=""):
    ####SIR仿真
    #tau = 0.5           # transmission rate
    #gamma = 1.0    # recovery rate
    #rho = 0.05      # random fraction initially infected
    t, S, I, R = EoN.fast_SIR(G, tau, gamma, rho=rho, tmax = tmax)
    if comment=="":
        plt.plot(t, S, color = 'r', label='S')
        plt.plot(t, I, color = 'b', label='I')
        plt.plot(t, R, color = 'g', label='R')
    else:
        plt.plot(t, S, label='S'+"/ "+comment)
        plt.plot(t, I, label='I'+"/ "+comment)
        plt.plot(t, R, label='R'+"/ "+comment)
    plt.legend(loc=0)
    plt.xlabel("Time")
    plt.ylabel("individuals")
####创建仿真图结构
N = 1000
M = 4
####ER均匀图创建
ER = nx.gnm_random_graph(N, M*N)
####BA异质图创建
BA=nx.barabasi_albert_graph(N, M)
#nx.draw(ER, with_labels=True)
#SIR(ER,comment='ER')
SIR(BA,comment='')
plt.show()

