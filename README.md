# Snakes-and-Ladders-Implementation


This code is written for the purpose of returning the minimum number of steps required to complete the Snakes and Ladders game.  The build_graph, build_edges, and build_connected functions build the graph, edges, and adjacency list to model the snakes and ladders game based on the number of tiles and orientation of snakes and ladders on the board. In this model, the vertices of the graph are the individual game tiles, while the edges connect tiles to the other tiles that can be reached on each move.
The fewest_moves function is a dynamic programming BFS algorithm, used to find the min- imum steps from the initial tile to all other other tiles. The value returned is the minimum steps from the first tile to the last tile.
