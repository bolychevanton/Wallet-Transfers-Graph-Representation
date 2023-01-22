# Wallet Transfers Graph Representation

In this project we will use [graphviz](https://graphviz.org/) package for wallet transfers visualization.  

## First of all, why?

Basically, as you've might noticed, working with blockchain data might be very tricky. If one is interested in particular data, he may struggle with searching of particular transactions that contain useful information.
Sometimes it can be useful due to existing of the so-called [mixers](https://en.wikipedia.org/wiki/Cryptocurrency_tumbler). It helps crypto enthusiasts to obscure their transactions history and make all transactions anonymous.
But some villains and hackers also use these services, for example all of them disguise their transactions and use it for money laundering. The most well-known transaction mixer on Ethereum is [Tornado Cash](https://en.wikipedia.org/wiki/Tornado_Cash). It was abused by hackers that have stolen billions of dollars exploiting vulnerabilities of smart-contracts so often, that the main developer of Tornado Cash was sued, and now this service [is being under OFAC pressure](https://medium.com/coinmonks/what-is-tornado-cash-and-why-was-it-blocked-5c95102c92b5).

The more data becomes complicated, the more interest it gains. It marked the beginning the fast evolution of on-chain [OSINT](https://en.wikipedia.org/wiki/Open-source_intelligence) technologies. These technologies are being developed in order to investigate financial crimes or represent and parse on-chain data to provide any insights about blockchain ecosystem. That's where we are going to dive a bit to see, what could be a possible solution that could help an OSINT specialist to deal with messy blockchain transactions.


## Let us start

Let's boil it down step by step on-chain data to provide any insights about blockchain ecosystem. That's where we are going to dive a bit to see, what could be a possible solution that could help an OSINT specialist to deal with messy blockchain transactions.

## Interface

In general, your perfect solution should be able to visualize a graph of transactions starting from any chosen wallet. So, 
we suggest you to implement the following CLI interface
```
python3 main.py \
--wallet-address 0xa6fac4a7b509d4d103a6c764b72a177e39a0136e \
--depth 2 \
--max-neighbours 3 
```
where 
- `--wallet-address` is the start wallet which transactions you are going to visualize
- `--depth` is the number of generations you are going to visualize
- `--max-neighbours` is the maximum number of neighbours for every vertex. If a vertex has several more that `max-neighbours` neighbours
then you need to select top `max-neighbours` vertexes with the greatest value of ETH transfered.

The project is fully executable. Run the command above and the code should render the example of graph for you.

## Architecure

Firstly, you need to get the list of transactions to visualize. See [`utils/query.py`](/utils/query.py) for the details. You need to do it
via running the sql query. We prepared [introductory video](https://disk.yandex.ru/i/PgzA6KHpTQdTNg) for your quick start. 
If you want to run sql queries from Python code it is reasonable to use [clickhouse-driver](https://clickhouse-driver.readthedocs.io/en/latest/) 
library. See the example of usage in [`utils/query.py`](/utils/query.py).

Then you need to vizualize the graph of extracted transactions. See [`visualize.py`](/visualize.py) for the details. 
We suggest you to use [graphviz](https://graphviz.org/) for graph visualization. 

Note that besides `pip install -r requirements.txt` you will possibly need to install graphvis package via
```
sudo apt install graphviz
```
if you are using Ubuntu operating system. Please, refer to [documentation](https://graphviz.org/download/) to understand how to install graphviz on other 
operating systems. Moreover, if you are experienced user of Windows we strongly recommend you to install [WSL](https://learn.microsoft.com/en-us/windows/wsl/install). It will save you loads of time in the future.
