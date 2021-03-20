# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:00:06 2021

@author: HP
"""
import networkx as nx
import matplotlib.pyplot as plt

#Function to draw graph with nodes and edges 
def draw(G,pos,measures, measure_name):
    
    nodes = nx.draw_networkx_nodes(G, pos, node_size=50, cmap=plt.cm.plasma, 
                                   node_color=list(measures.values()),
                                   nodelist=measures.keys())
    edges = nx.draw_networkx_edges(G, pos)
    plt.title(measure_name)
    plt.colorbar(nodes)
    plt.axis('off')
    plt.show()
    

#function to draw histogram
def draw_plot(measure, measure_name):
    vd=measure.values()
    plt.hist(vd, bins=10)
    plt.title(measure_name)
    plt.xlabel(' Centrality Value')
    plt.ylabel ('Number of nodes')
    plt.show()
    
 
#########################################################    
    
#using networkx library on youtube dataset
G=nx.DiGraph()
edges=[]

lines=open('com-youtube.ungraph.txt','r').readlines()
for line in lines:
    if(line[0]!='#'):
       edges.append((int(line.split()[0]),int(line.split()[1])))

G.add_edges_from(edges[:100])


pos = nx.spring_layout(G, seed=675)

#plotting for degree centrality
draw_plot(nx.degree_centrality(G),'Degree Centrality')
draw(G,pos,nx.degree_centrality(G),'Degree Centrality')

#plotting for Closeness centrality
draw_plot(nx.closeness_centrality(G),'Closeness Centrality')
draw(G,pos,nx.closeness_centrality(G),'Closeness Centrality')

#plotting for Betweennees centrality
draw_plot(nx.betweenness_centrality(G),'Betweennees Centrality')
draw(G,pos,nx.betweenness_centrality(G),'Betweennees Centrality')

#plotting for EigenVector centrality
draw_plot(nx.eigenvector_centrality(G,max_iter=1000),'EigenVector Centrality')
draw(G,pos,nx.eigenvector_centrality(G,max_iter=1000),'EigenVector Centrality')

#plotting for Katz centrality
draw_plot(nx.katz_centrality(G, alpha=0.1, beta=1.0), ' Katz Centrality')
draw(G,pos, nx.katz_centrality(G, alpha=0.1, beta=1.0), ' Katz Centrality')

#plotting for PageRank centrality
draw_plot(nx.pagerank(G, alpha=0.85), 'PageRank')
draw(G, pos, nx.pagerank(G, alpha=0.85), 'PageRank')

###################
#Finding Average clustring coeffecient, Global Clustering Coeffecient,Reciprocity and Transitivity


G2=nx.DiGraph()
edges=[]

lines=open('com-youtube.ungraph.txt','r').readlines()
for line in lines:
    if(line[0]!='#'):
       edges.append((int(line.split()[0]),int(line.split()[1])))

G2.add_edges_from(edges)
print("Average Clustering Coefficient:", nx.average_clustering(G2)) 
print("Global clustering Coefficient: ", nx.transitivity(G2)) 
print("Reciprocity:",nx.algorithms.reciprocity(G2))
print("Transitivity:",nx.algorithms.transitivity(G2))

############################################################################
############################################################################
############################################################################
############################################################################

#using networkx library on Twitter dataset


G=nx.DiGraph()
edges=[]

lines=open('twitter_combined.txt','r').readlines()
for line in lines:
    if(line[0]!='#'):
       edges.append((int(line.split()[0]),int(line.split()[1])))

G.add_edges_from(edges[:100])


pos = nx.spring_layout(G, seed=675)

#plotting for degree centrality
draw_plot(nx.degree_centrality(G),'Degree Centrality')
draw(G,pos,nx.degree_centrality(G),'Degree Centrality')

#plotting for Closeness centrality
draw_plot(nx.closeness_centrality(G),'Closeness Centrality')
draw(G,pos,nx.closeness_centrality(G),'Closeness Centrality')

#plotting for Betweennees centrality
draw_plot(nx.betweenness_centrality(G),'Betweennees Centrality')
draw(G,pos,nx.betweenness_centrality(G),'Betweennees Centrality')

#plotting for EigenVector centrality
draw_plot(nx.eigenvector_centrality(G,max_iter=1000),'EigenVector Centrality')
draw(G,pos,nx.eigenvector_centrality(G,max_iter=1000),'EigenVector Centrality')

#plotting for Katz centrality
draw_plot(nx.katz_centrality(G, alpha=0.1, beta=1.0), ' Katz Centrality')
draw(G,pos, nx.katz_centrality(G, alpha=0.1, beta=1.0), ' Katz Centrality')

#plotting for PageRank centrality
draw_plot(nx.pagerank(G, alpha=0.85), 'PageRank')
draw(G, pos, nx.pagerank(G, alpha=0.85), 'PageRank')

###################

#Finding Average clustring coeffecient, Global Clustering Coeffecient,Reciprocity and Transitivity
G2=nx.DiGraph()
edges=[]

lines=open('twitter_combined.txt','r').readlines()
for line in lines:
    if(line[0]!='#'):
       edges.append((int(line.split()[0]),int(line.split()[1])))

G2.add_edges_from(edges)
print("Average Clustering Coefficient:", nx.average_clustering(G2)) 
print("Global clustering Coefficient: ", nx.transitivity(G2)) 
print("Reciprocity:",nx.algorithms.reciprocity(G2))
print("Transitivity:",nx.algorithms.transitivity(G2))


############################################################################
############################################################################
############################################################################
############################################################################

N=500
x =list()
y =list()

for i in range(51):
    plt.figure(figsize=(10,100)) 
    plt.subplot (51,2,2*i+1)
    k = i/10
    G = nx.erdos_renyi_graph(N,k/(N-1), seed=5)
    nx.draw(G, node_size=2)
    plt.title("value of <k>: "+str(k))
    plt.subplot(51,2,2*i+2)
    Giant=G. subgraph(sorted(nx.connected_components(G), key=len,reverse=True)[0])
    x.append(k)
    nx.draw(Giant,node_size=2)
    plt.title("Biggest component at <k>: "+str(k)) 
    y.append(len(Giant.nodes())/N)

plt. figure(figsize=(10,5))
plt.plot(x,y, 'bo--')
plt.title("variance of size of Giant component with changing <k>")
plt.xlabel("<k>")
plt.ylabel("Ng/N")

