import numpy as np
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Graph

def load_csv(path):    #读取文件
    data_read = pd.read_csv(path,encoding='ISO-8859-1')
    list = data_read.values.tolist()
    data = np.array(list)
    print(data.shape)
    # print(data)
    return data

edges = []
nodes = []
RelationData = load_csv("F:\A_MyWork\Research\LungCancer\RelationGraph&Data\lungdata2\\tumour.csv")
# print(RelationData)
df = pd.read_csv("F:\A_MyWork\Research\LungCancer\RelationGraph&Data\lungdata2\\tumour.csv",encoding='gbk')
featureName= df.columns.tolist()
nodes = [{'name': ''+featureName[i],"symbolsize":2} for i in range(17)]
# print(nodes)
init_opts = opts.InitOpts(width="100%",  
                          height="900px",  
                          renderer="canvas",  
                          page_title="Feature Graph",  
                          js_host="" 
                          )
label_opts = opts.LabelOpts(is_show=True,position='right')
for i in range(17):
    for j in range(17):
        if RelationData[i,j] > 0.15 :
            linestyle_opts = opts.LineStyleOpts(is_show=True,
                                                    width=RelationData[i,j]*30,
                                                    opacity=0.6,
                                                    curve=0.3,
                                                    type_="solid",
                                                    color="orange"
                                                )
            edges.append({'source':i, 'target':j,"lineStyle": linestyle_opts})
c = Graph(init_opts)
c.add("", nodes, edges,
      repulsion=8000,
      edge_length=100,
      label_opts=label_opts,
      layout="circular",
      is_rotate_label=True,
      linestyle_opts=linestyle_opts
      )
c.set_global_opts(
    title_opts=opts.TitleOpts(title="TumourGraph")
)
c.render('LungResult\TumourGraph.html')