#!/usr/bin/env python
# coding: utf-8

# In[20]:


import matplotlib.pyplot as plt 
import networkx as nx 
import numpy as np
import scipy.stats

G = nx.karate_club_graph()
plt.figure(figsize =(15, 10)) 
nx.draw_networkx(G, with_labels = True) 


# In[21]:


deg_centrality = nx.degree_centrality(G) 
  
# G is the Karate Club Graph 
print(deg_centrality) 
de_centrality = list(deg_centrality.values())

plt.figure(figsize =(8, 6)) 
plt.plot(de_centrality)
plt.show()


# In[22]:


close_centrality = nx.closeness_centrality(G) 

# G is the Karate Social Graph 
print(close_centrality) 
cl_centrality = list(close_centrality.values())

plt.figure(figsize =(8, 6)) 
plt.plot(cl_centrality)
plt.show()


# In[13]:


bet_centrality = nx.betweenness_centrality(G, normalized = True, endpoints = False) 

# G is the Karate Social Graph, parameters normalized 
# and endpoints ensure whether we normalize the value 
# and consider the endpoints respectively. 
print(bet_centrality) 
bt_centrality = list(bet_centrality.values())

plt.figure(figsize =(8, 6)) 
plt.plot(bt_centrality)
plt.show()


# In[23]:


plt.figure(figsize =(15, 8)) 
plt.plot(de_centrality, 'r', label = 'Degree centrality')
plt.plot(cl_centrality, 'b' , label = 'Close centrality')
plt.plot(bt_centrality, 'g' , label = 'Betweenness centrality')
plt.title('Copmarsion')
plt.xlabel('Number of Nodes')  
plt.ylabel('centrality')
plt.legend(loc='upper center')
plt.show()


# In[15]:


r_cl,bt = np.corrcoef(cl_centrality, bt_centrality)
print(r_cl,bt)

r_cl,de = np.corrcoef(cl_centrality, de_centrality)
print(r_cl,de)

r_bt,de = np.corrcoef(bt_centrality, de_centrality)
print(r_bt,de)
scipy.stats.pearsonr(bt_centrality, cl_centrality)[0]    # Pearson's r


# In[24]:


plt.figure(figsize =(15, 8)) 
plt.plot(de_centrality,cl_centrality, 'o')
plt.title('Copmarsion degree centrality & close centrality')
plt.xlabel('degree centrality')  
plt.ylabel('close centrality')
plt.show()


# In[25]:


plt.figure(figsize =(15, 8)) 
plt.plot(de_centrality,bt_centrality, 'o')
plt.title('Copmarsion degree centrality & between centrality')
plt.xlabel('degree centrality')  
plt.ylabel('between centrality')
plt.show()


# In[26]:


plt.figure(figsize =(15, 8)) 
plt.plot(cl_centrality,bt_centrality, 'o')
plt.title('Copmarsion close centrality & between centrality')  
plt.xlabel('close centrality')
plt.ylabel('between centrality')
plt.show()

