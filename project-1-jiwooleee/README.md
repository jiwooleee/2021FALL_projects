# README

## Description of the algorithm

<<Follows the algorithm using DFS as described in Section 6.2 and 6.3 of Erickson Textbook>>

1. In read_graph(), get the list of vertices & the adjacency list of the reversed graph
  so that every edge (U, V) => V is dependent on U
2. Start by unmarking all the vertices. Keep two data structures to check if
  (i) the vertex is added to the topological sorting, a stack S
  (ii) the vertex is contained in a cycle
      => if a cycle is found, print it
3. For all vertices in the graph, if the vertex U is unmarked (i), loop through
  its outgoing edges and check (i) & (ii).
4. Append V before appending U's (its dependencies) so that when we pop from S,
  the order is preserved

## Time efficiency of the algorithm

Since this algorithm is DFS algorithm with a few added data structures, the time
efficiency is the same as DFS = O(E+V)
