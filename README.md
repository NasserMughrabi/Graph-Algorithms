# Graphs & Graphs Algorithms

# Graphs

#### A graph is a list of vertices and edges. A graph can be connected, diconnected, cyclic, ascyclic, directed, and undirected. Graphs is a big topic and diving too deep can get us lost and confused, so we will just focus on the basics and most common graphs that we might need to use for real life problems.

## A graph can be represented in two ways:

1. Adjacency List : represented using Hashmap or an array of linkedlists (Hashmap has faster operations)
2. Adjacency Matrix : represented using two dimentional array (2D array) - a grid

## There are four main graph algorithms used to check for reachability, search, and shortest path operations:

1. Breadth First Search - uses QUEUE data structure
2. Depth First Search - uses STACK data structure - can be implemented with recursion (more elegant solution)
3. Best First Search - uses PRIORITY QUEUE data structure
4. Dijekstra Algorithm - does not follow whatever first search

## Common uses of each graph algorithm:

- Breadth First Search :
  1. Guarantees the shortest path between two vertices
  2. Checks whether two vertices are connected or not
- Depth First Search :
  1. Checks whether two vertices are connected or not
- Best First Search :
  1. Checks whether two vertices are connected or not
- Dijekstra Algorithm : 1. Guarantees the shortest path between two vertices in a weighted and non weighted graph 2. Checks whether two vertices are connected or not
  NOTE: All four algorithms can traverse and search a graph and they all can be adjusted to do more things than what's been mentioned
