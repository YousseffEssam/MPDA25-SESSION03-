#r: networkx
#r: matplotlib

from typing import cast, Any
import networkx as nx # type: ignore
import matplotlib.pyplot as plt # type: ignore
import Rhino.Geometry as rg # type: ignore

# DECLARE INPUT VARIABLES
m = cast(rg.Mesh, m)  # type: ignore

def PlotGraph(G,filepath):
    # add position
    pos = nx.spring_layout(G)

    #draw serttings
    fig = plt.figure(figsize=(10,10))
    ax = plt.subplot()
    ax.set_title('Graph', fontsize=12)
    nx.draw(G, pos, node_size=1500, with_labels=True, node_color='pink', font_size=12)

    #draw the graph
    plt.tight_layout()

    # plt.show()
    plt.savefig(filepath, format="PNG")

def GraphFromMesh(mesh):

    G=nx.Graph()
    edges = mesh.TopologyEdges

    for e in range(edges.Count):
        v1 = edges.GetTopologyVertices(e)[0]
        v2 = edges.GetTopologyVertices(e)[1]

        #add information to node

        G.add_node(v1, edge = e)
        G.add_node(v2, edge = e)

        # G.add_node(v1, pos = mesh.Vertices[v1])
        # G.add_node(v2, pos = mesh.Vertices[v2])

        G.add_edge(v1, v2)

    return G

G= GraphFromMesh(m)

# Iterate through the nodes and print their attributes
for node in G.nodes(data=True):
    print(node)


# for node, atrr in G.nodes(data=True):
#     print(atrr['pos'])


G= GraphFromMesh(m)
print (G)

  
#plot
path= r"D:\MPDA25\Semester 2\At_Apy(Python)\Session 2\session02\images\MDPA_plot3.png"
PlotGraph(G, path)