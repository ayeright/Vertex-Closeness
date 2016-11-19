## Vertex-Closeness

Overview
---------------------
Ranks vertices in an unweighted, undirected graph by their closeness centrality http://en.wikipedia.org/wiki/Centrality#Closeness_centrality.

Documentation
---------------------

## Dependencies

Requires Python 2.7. Should work with Python 3.5 but has not been tested.

## Installation

1.  Clone this repo with `git clone https://github.com/ayeright/Vertex-Closeness.git`.
2.  Switch to the repo folder with `cd Vertex-Closeness`.
    
## Usage

You can run `python rank_vertex_closeness.py` to rank the vertices in `edges.dat` by their closeness centrality. You can pass one optional argument, the path to a file which specifies the edges. Each line of the file must consist of two vertex names separated by a single space, representing an edge between those two nodes. Results will be printed to the command line.
