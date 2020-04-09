import networkx as nx

# 创建有向图
G = nx.DiGraph()
# 有向图之间边的关系
edges = [("A", "B"), ("A", "C"), ("A", "D"), ("B", "A"), ("B", "D"), ("C", "A"), ("D", "B"), ("D", "C")]

for edge in edges:
    G.add_edge(edge[0], edge[1])
pagerank_list = nx.pagerank(G, alpha=1)
print('pagerank值是：', pagerank_list)

# 假设用户有 15% 的概率随机跳转
pagerank_list_15 = nx.pagerank(G, alpha=0.85)
print('假设用户有 15% 的概率随机跳转时的 pagerank 值是：', pagerank_list_15)
