#Load Data and N2V parameters
!pip install --upgrade networkx matplotlib
!pip install node2vec
!pip install umap-learn


import networkx as nx
import mathplotlib.pyplot as plt

gml_graph = nx.read_gml('/PATH/TO/File.gml')
