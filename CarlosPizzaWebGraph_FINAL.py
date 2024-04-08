import pandas as pd
import openpyxl

df = pd.read_excel("C:/HOZIO/CARLOS_all_inlinks.xlsx")
list_inlinks = df.values.tolist()

listwithtuples = []

for x in list_inlinks:
    if x[0] == "Hyperlink" and x[1].count("/") <= x[2].count("/") and "https://www.carlospizzaoven.com/" in x[2]:
        tuple_links = (x[1], x[2])
        listwithtuples.append(tuple_links)

noduplicates = list(dict.fromkeys(listwithtuples))

import networkx as nx

G=nx.Graph()
G.add_edges_from(noduplicates)

from matplotlib import pyplot as plt
import numpy as np

pos = nx.spring_layout(G, k=0.3*1/np.sqrt(len(G.nodes())), iterations=20)
plt.figure(3, figsize=(30, 30))
nx.draw(G,pos, with_labels=True)

plt.savefig("CARLOS_data1.png")

plt.show()

df = pd.read_excel("C:/HOZIO/CARLOS_internal_html.xlsx")
list_all = df.values.tolist()

list_colors = []
for y in G.nodes:
    match = False
    for x in list_all:
        if y == x[0]:
            match = True
            if x[4] == "Non-Indexable":
                list_colors.append("red")
            else:
                list_colors.append("blue")
    if match == False:
        list_colors.append("yellow")

dictionary_degree = dict(G.degree)

sort_dictionary_degree = dict(sorted(dictionary_degree.items(), key=lambda item: item[1], reverse = True))

counter = 0

for key, value in sort_dictionary_degree.items():
    if counter < 5:
        sort_dictionary_degree[key] = key
    else:
        sort_dictionary_degree[key] = ""

    counter = counter + 1

pos = nx.spring_layout(G, k=0.3*1/np.sqrt(len(G.nodes())), iterations=20)
plt.figure(3, figsize=(30,30))
dictionary_degree = dict(G.degree)

nx.draw(G,pos, with_labels=False, node_size = [10 + v * 300 for v in dictionary_degree.values()],node_color = list_colors, font_size = 15)
nx.draw_networkx_labels(G,pos,sort_dictionary_degree,font_size=25,font_color='r')

plt.savefig("CARLOS_data2.png")

plt.show()

listwithtuplescontent = []

for x in list_inlinks:
    if x[0] == "Hyperlink" and "https://www.carlospizzaoven.com/" in x[2] and x[13] == "Content" and x[11] == "Absolute":
        
        tuple_links = (x[1],x[2])
        listwithtuplescontent.append(tuple_links)

noduplicatescontent = list(dict.fromkeys(listwithtuplescontent))

G=nx.Graph()
G.add_edges_from(noduplicatescontent)

pos = nx.spring_layout(G, k=0.3*1/np.sqrt(len(G.nodes())), iterations=20)
plt.figure(3, figsize=(30, 30))
dictionary_degree = dict(G.degree)

nx.draw(G,pos, with_labels=True, node_size = [10 + v * 300 for v in dictionary_degree.values()], font_size = 20)

plt.savefig("CARLOS_data3.png")

plt.show()
