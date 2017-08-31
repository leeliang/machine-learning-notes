#!/usr/bin/env python
# coding: utf-8
"""
Created on 2017-08
@author:  LI Liang
"""

import networkx as nx
import matplotlib.pyplot as plt 

def binary_tree_layout(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, 
                  pos = None, parent = None):
    '''If there is a cycle that is reachable from root, then this will see infinite recursion.
       G: the graph
       root: the root node of current branch
       width: horizontal space allocated for this branch - avoids overlap with other branches
       vert_gap: gap between levels of hierarchy
       vert_loc: vertical location of root
       xcenter: horizontal location of root
       pos: a dict saying where all nodes go if they have been assigned
       parent: parent of this branch.
       each node has an attribute "left: or "right"'''
    if pos == None:
        pos = {root:(xcenter,vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)
    neighbors = G.neighbors(root)
    if parent != None:
        neighbors.remove(parent)
    if len(neighbors)!=0:
        dx = width/2.
        leftx = xcenter - dx/2
        rightx = xcenter + dx/2
        for neighbor in neighbors:
            if G.node[neighbor]['child_status'] == 'left':
                pos = binary_tree_layout(G,neighbor, width = dx, vert_gap = vert_gap, 
                                    vert_loc = vert_loc-vert_gap, xcenter=leftx, pos=pos, 
                    parent = root)
            elif G.node[neighbor]['child_status'] == 'right':
                pos = binary_tree_layout(G,neighbor, width = dx, vert_gap = vert_gap, 
                                    vert_loc = vert_loc-vert_gap, xcenter=rightx, pos=pos, 
                    parent = root)
    return pos
#
def plotPoint(p):
  plt.ylim([0,10])
  plt.xlim([0,10])
  for i in range(len(p)):
    x = p[i][0]
    y = p[i][1]
    plt.plot(x,y, 'o', fillstyle='none', ms=10, color='b')
    text = chr(65+i) 
    plt.annotate(text, xy=p[i], xytext=(5,5), textcoords='offset points',color='b')
  plt.xticks([])
  plt.yticks([])

def plotTree(G):
  for node in G.nodes():
    if node in ["B","D","F"]:
        G.node[node]['child_status'] = 'left'  #assign even to be left
    else:
        G.node[node]['child_status'] = 'right' #and odd to be right
  pos = binary_tree_layout(G,"A")
  color_list = ["lightcoral","lightgrey","lightgrey","lightcoral","lightcoral","lightcoral"]
  nx.draw(G, pos=pos, with_labels=True, node_size=1600, node_color=color_list[:len(G)])
  return pos
# Data from wikipedia
c = [(7,2), (5,4), (9,6), (2,3), (4,7), (8,1)]
#
plt.figure(figsize=[10,10])
plt.subplot(321)
plotPoint(c)
plt.axvline(x = c[0][0],lw=2,color='r')
#
plt.subplot(322)
G= nx.Graph()
G.add_node("A")
pos = plotTree(G)
plt.text( pos["A"][0]*1.15, pos["A"][1],'$X^{(0)}$',color='r')
#
plt.subplot(323)
plotPoint(c)
plt.axvline(x = c[0][0],lw=2,color='r')
plt.axhline(y=c[1][1], xmin=0, xmax=c[0][0]/10., color='k',lw=1.5)
plt.axhline(y=c[2][1], xmin=c[0][0]/10., xmax=1, color='k',lw=1.5)
#
plt.subplot(324)
G.add_edges_from([("A","B"),("A","C")])
pos = plotTree(G)
plt.text( pos["C"][0]*1.15, pos["A"][1],'$X^{(0)}$',color='r')
plt.text( pos["C"][0]*1.15, pos["C"][1],'$X^{(1)}$')
#
plt.subplot(325)
plotPoint(c)
plt.axvline(x = c[0][0],lw=2,color='r')
plt.axhline(y=c[1][1], xmin=0, xmax=c[0][0]/10., color='k',lw=1.5)
plt.axhline(y=c[2][1], xmin=c[0][0]/10., xmax=1, color='k',lw=1.5)
plt.axvline(ymin=0, ymax=c[1][1]/10., x=c[3][0], color='r', ls='--')
plt.axvline(ymin=c[1][1]/10., ymax=1, x=c[4][0], color='r', ls='--')
plt.axvline(ymin=0, ymax=c[2][1]/10., x=c[5][0], color='r', ls='--')
#
plt.subplot(326)
G.add_edges_from([("B","D"), ("B","E"), ("C","F")])
pos = plotTree(G)
plt.text( pos["C"][0]*1.15, pos["A"][1],'$X^{(0)}$',color='r')
plt.text( pos["C"][0]*1.15, pos["C"][1],'$X^{(1)}$')
plt.text( pos["C"][0]*1.15, pos["F"][1],'$X^{(0)}$',color='r')

plt.savefig('kdtree.png')