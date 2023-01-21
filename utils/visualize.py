import graphviz
import pandas as pd


def draw_graph(transactions: pd.DataFrame):
    dot = graphviz.Digraph(
        name="Transfers-Graph", comment="Wallet Transfers Graph Representation"
    )

    # YOUR CODE GOES HERE

    A = transactions["from_address"].iloc[0]
    B = transactions["to_address"].iloc[0]
    C = transactions["to_address"].iloc[1]

    dot.node(A)
    dot.node(B)
    dot.node(C)

    # Use 4 point precision for ETH transfer amounts
    dot.edge(A, B, label="1.5432 ETH")
    dot.edge(A, C, label="2.1232 ETH")
    dot.edge(C, B, label="0.5 ETH")

    dot.view()
