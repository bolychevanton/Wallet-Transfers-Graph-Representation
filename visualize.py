import graphviz
import pandas as pd


def draw_graph(edges: pd.DataFrame):
    dot = graphviz.Digraph(
        name="Wallet Transfers", comment="Wallet Transfers Graph Representation"
    )

    A = edges["from_address"].iloc[0]
    B = edges["to_address"].iloc[0]
    C = edges["to_address"].iloc[1]

    dot.node(A)
    dot.node(B)
    dot.node(C)

    # Use 4 point precision for graph render
    dot.edge(A, B, label="1.5432 ETH")
    dot.edge(A, C, label="2.1232 ETH")
    dot.edge(C, B, label="0.5 ETH")

    dot.view()
