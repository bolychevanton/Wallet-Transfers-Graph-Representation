from utils.query import get_transactions
from utils.visualize import draw_graph
import argparse

parser = argparse.ArgumentParser(
    prog="Arbitrage Scanner for block range",
    description="The application enables users find arbitrage opportunities in evm blockchains in specific block range",
)
parser.add_argument("--depth", type=int, default=None, required=True)
parser.add_argument("--wallet-address", type=str, default=None, required=True)
parser.add_argument("--max-neighbours", type=int, default=None, required=True)
args = parser.parse_args()


transactions = get_transactions(args.wallet_address, args.depth, args.max_neighbours)
draw_graph(transactions)
