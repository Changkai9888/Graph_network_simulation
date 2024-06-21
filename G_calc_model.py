import networkx as nx
import random,copy
####
#####计算下一个结点状态
def sis_step(G0,recovery_probability=0.02,contact_infec_Prob=0.05):
    #介绍：SIS模型：输入图，输出传播一步的结果图
    #recovery_probability: 康复概率
    #contact_infec_Prob: 接触传染概率
    G1=copy.deepcopy(G0)#放结果
    for n in G0.nodes():#遍历结点
        if G0.nodes[n]['state']=='i':#如果已经感染
            if random.random()<recovery_probability:#有概率康复
                G1.nodes[n]['state']='s'
        if G0.nodes[n]['state']=='s':#如果未被感染
            Neibor_infec_num=0#邻居的感染数
            for i in G0[n]:#遍历结点的邻位点
                if G0.nodes[i]['state']=='i':
                    Neibor_infec_num+=1
            if random.random()>(1-contact_infec_Prob)**Neibor_infec_num:#被传染的概率
                G1.nodes[n]['state']='i'
    return G1

#####
def count_infection(G):
    #介绍：得到病患比例
    num=0
    for n in G.nodes():#遍历结点
        if G.nodes[n]['state']=='i':#状态为感染
            num+=1
    return num/G.number_of_nodes()
####
def statis_people_label(G,state_labels=['s','i']):
    #介绍：各类人群统计
    total=G.number_of_nodes()
    num=[0]*len(state_labels)
    for n in G.nodes():#遍历结点
        for i in range(len(state_labels)):
            if G.nodes[n]['state']==state_labels[i]:#状态为感染
                num[i]+=1
    return num
