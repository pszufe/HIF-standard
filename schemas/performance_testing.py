"""
Datasets to use:  

1. http://bigg.ucsd.edu/models/e_coli_core    (xgi.load_big_data ecoli dataset from this website)]
2. https://github.com/HGX-Team/data/tree/main/contacts/high-school
"""

import datetime as dtm
import json
import sys
import timeit
import warnings
from time import perf_counter

import fastjsonschema
import hypernetx as hnx
import pandas as pd
import xgi

warnings.simplefilter("ignore")
sys.stdout = open("performance_testing_output.txt", "a")


def marktime(msg=None):
    temp = dtm.datetime.now()
    print(temp.strftime("%d/%m/%y %H:%M:%S"), ": ", msg, flush=True)
    return temp


schema = json.load(open("hif_schema_v0.1.0.json", "r"))
validator = fastjsonschema.compile(schema)

### high_school data as dataframes for hnx;
hs = json.load(open(f"../examples/contacts-high-school.json", "r"))
hs_df = pd.DataFrame(hs["hyperedges"]).fillna("")
hs_df["edge"] = hs_df.interaction.map(lambda x: x[0])
hs_df["node"] = hs_df.interaction.map(lambda x: x[1])
hs_df = hs_df[["edge", "node", "time"]]

hs_nodedf = pd.DataFrame(hs["nodes"])
hs_nodedf = hs_nodedf.set_index("id").reset_index().fillna("")


### HNX constructors
def hnx_hypergraph(df, nodedf=None, edgedf=None):
    return hnx.Hypergraph(df, node_properties=nodedf)


def hnx_to_hif(hg):
    edgj = hg.edges.to_dataframe
    edid = edgj.index._name or "index"
    nodj = hg.nodes.to_dataframe
    ndid = nodj.index._name or "index"
    edgj = edgj.reset_index().rename(columns={edid: "edge"}).to_dict(orient="records")
    nodj = nodj.reset_index().rename(columns={ndid: "node"}).to_dict(orient="records")
    incj = (
        hg.incidences.to_dataframe.reset_index()
        .rename(columns={"nodes": "node", "edges": "edge"})
        .to_dict(orient="records")
    )
    hif = {"edges": edgj, "nodes": nodj, "incidences": incj}
    return hif


def hnx_from_hif(hif):
    edges = pd.DataFrame(hif["edges"])
    nodes = pd.DataFrame(hif["nodes"])
    incidences = pd.DataFrame(hif["incidences"])
    return hnx.Hypergraph(incidences, node_properties=nodes, edge_properties=edges)


marktime("Begin Run")

start = perf_counter()
h = hnx_hypergraph(hs_df, nodedf=hs_nodedf)
finish = perf_counter()
print("hnx_high_school ", f"{finish - start:.5f} ns", flush=True)

start = perf_counter()
hif = hnx_to_hif(h)
finish = perf_counter()
print("hnx_to_hif high_school ", f"{finish - start:.5f} ns", flush=True)

start = perf_counter()
newh = hnx_from_hif(hif)
finish = perf_counter()
print("hnx_from_hif high_school ", f"{finish - start:.5f} ns", flush=True)

marktime("Run Complete \n")
