import networkx as nx

# 使用 Barabási-Albert 模型创建无标度网络
n = 100  # 节点数
m = 3    # 每个新节点连接到现有节点的边数
G = nx.barabasi_albert_graph(n, m)

# 可视化无标度网络
import matplotlib.pyplot as plt
nx.draw(G, with_labels=True)
plt.show()
