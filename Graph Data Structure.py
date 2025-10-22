import matplotlib.pyplot as plt
import networkx as nx
from collections import deque


class graph_structure:
   def __init__(self):
       self.graph = {}


   def add_edge(self, node, neighbor):
       if node not in self.graph:
           self.graph[node] = []
       if neighbor not in self.graph:
           self.graph[neighbor] = []
       self.graph[node].append(neighbor)
       self.graph[neighbor].append(node)


   def show_graph(self):
       for node, neighbors in self.graph.items():
           print(f"{node} -> {neighbors}")


   def plot_graph(self, highlight_nodes=None, title="Graph Structure"):
       G = nx.Graph(self.graph)
       pos = nx.spring_layout(G, seed=42)
       plt.figure(figsize=(6, 4))


       node_colors = []
       for n in G.nodes():
           if highlight_nodes and n in highlight_nodes:
               node_colors.append("lightcoral")
           else:
               node_colors.append("skyblue")


       nx.draw(
           G, pos,
           with_labels=True,
           node_color=node_colors,
           node_size=1200,
           font_size=12,
           font_weight='bold',
           edge_color='gray'
       )
       plt.title(title)
       plt.show()


   def bfs(self, start):
       visited = set()
       queue = deque([start])
       order = []


       while queue:
           node = queue.popleft()
           if node not in visited:
               visited.add(node)
               order.append(node)
               for neighbor in self.graph[node]:
                   if neighbor not in visited:
                       queue.append(neighbor)


       print("BFS จ้า:", order)
       self.plot_graph(highlight_nodes=order, title="BFS")
       return order

   def dfs(self, start):
       visited = set()
       order = []

       def dfs_recursive(node):
           visited.add(node)
           order.append(node)

           if node in self.graph:
               for neighbor in self.graph[node]:
                   if neighbor not in visited:
                       dfs_recursive(neighbor)


       dfs_recursive(start)
       print("DFS จ้า:", order)
       self.plot_graph(highlight_nodes=order, title="DFS")
       return order


# ทดสอบการทำงาน
if __name__ == "__main__":
   g = graph_structure()
   g.add_edge('A', 'B')
   g.add_edge('A', 'C')
   g.add_edge('B', 'D')
   g.add_edge('C', 'D')
   g.add_edge('D', 'E')


   print("Graph Structure:")
   g.show_graph()


   g.bfs('A')
   g.dfs('A')
