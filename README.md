# Wallet Transfers Graph Representation

In this project we will use [graphvis](https://graphviz.org/) package for wallet transfers visualization.  

## First of all, why?

Basically, as you've might noticed, working with blockchain data might be very tricky. If one is interested in particular data, he may struggle with searching of particular transactions that contain useful information.
Sometimes it can be useful due to existing of the so-called [mixers](https://en.wikipedia.org/wiki/Cryptocurrency_tumbler). It helps crypto enthusiasts to obscure their transactions history and make all transactions anonymous.
But some villains and hackers also use these services, for example all of them disguise their transactions and use it for money laundering. The most well-known transaction mixer on Ethereum is [Tornado Cash](https://en.wikipedia.org/wiki/Tornado_Cash). It was abused by hackers that have stolen billions of dollars exploiting vulnerabilities of smart-contracts so often, that the main developer of Tornado Cash was sued, and now this service [is being under OFAC pressure](https://medium.com/coinmonks/what-is-tornado-cash-and-why-was-it-blocked-5c95102c92b5).

The more data becomes complicated, the more interest it gains. It marked the beginning the fast evolution of on-chain [OSINT](https://en.wikipedia.org/wiki/Open-source_intelligence) technologies. These technologies are being developed in order to investigate financial crimes or represent and parse on-chain data to provide any insights about blockchain ecosystem. That's where we are going to dive a bit to see, what could be a possible solution that could help an OSINT specialist to deal with messy blockchain transactions.

## Let us start

Let's boil it down step by step on-chain data to provide any insights about blockchain ecosystem. That's where we are going to dive a bit to see, what could be a possible solution that could help an OSINT specialist to deal with messy blockchain transactions.

First, let's briefly discuss what we are going to achieve by this project. In general, your perfect solution should be able to visualize a graph of transactions starting from any chosen wallet. So, your program will contain two main blocks:

* **Data selector**
* **Data visualizer**

### Data selector

#### Configuration
- set the **depth** parameter which specifies the amount of levels of child nodes. We will elaborate on that further
- set the **wallet_address** - an address from which the tracing is intended to start

#### Tracing process
- connect to the transaction database
- select all transactions that represent the information about a graph of transfers of desired depth: retrieve nodes and edges in a suitable for [graphvis](https://graphviz.readthedocs.io/en/stable/manual.html) format and save transfer amounts to label corresponding edges (as we're interested not only in the direction of money but also in amounts)

### Visualization

#### Configuration 
- set the **depth** parameter which specifies the amount of levels of child nodes. We will elaborate on that further
- set the **wallet_address** - an address from which the tracing is intended to start

#### Tracing process
- connect to the transaction database
- select all transactions that represent the information about a graph of transfers of desired depth: retrieve nodes and edges in a suitable for [graphvis](https://graphviz.readthedocs.io/en/stable/manual.html) format and save transfer amounts to label corresponding edges (as we're interested not only in the direction of money but also in amounts)