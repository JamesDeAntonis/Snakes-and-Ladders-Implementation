
# coding: utf-8

# This code is written for the purpose of returning the minimum number of steps required to complete the Snakes and Ladders game.  The build_graph, build_edges, and build_connected functions build the graph, edges, and adjacency list to model the snakes and ladders game based on the number of tiles and orientation of snakes and ladders on the board.  In this model, the vertices of the graph are the individual game tiles, while the edges connect tiles to the other tiles that can be reached on each move.
# 
# The fewest_moves function is a dynamic programming BFS algorithm, used to find the minimum steps from the initial tile to all other other tiles.  The value returned is the minimum steps from the first tile to the last tile.

# In[5]:

#Initialize

# Make the list of vertices
A = []
for i in range(1,101):
    A.append(i)

# Sample set of ladders
B = [(3,42),(8,54),(24,86),(50,93),(58,65),(59,81)]
#Sample set of snakes
C = [(27,17),(67,10),(79,40),(95,71),(98,6)]


# In[6]:

def build_graph(l):
    
    #building V, the set of vertices
    
    V = []
    for i in range(1,l):
        V.append(i)
    return V


# In[7]:

def build_edges(Ladders,Snakes,l): #building Edges, the set of edges
    #necessary for termination.  Ladders and Snakes are both sorted
    Ladders.append((l+1,l+1)) 
    Snakes.append((l+1,l+1))
    Edges = [] #initialize the set of edges
    #pointer for marking the first ladder whose bottom rung is not below i
    lcounter = 0 
    #pointer for marking the first snake whose top rung is not below i
    scounter = 0 
    #pointer for temporarily tracking the ladders beyond the ladder at index lcounter
    lcounter2 = 1 
    #pointer for temporarily tracking the snakes beyond the snake at index scounter
    scounter2 = 1 
    #iterates through the possible vertices where an edge can start
    for i in range(1,l): 
        #possible vertices where an edge can end except snakes and ladders
        for j in range(i+1,min(l+1,i+7)): 
            #checking whether we need to update the indexing of ladders and/or snakes
            #if top rung of the current snake is below i, adjust snake pointers
            if Snakes[scounter][0] <= i: 
                scounter += 1
                scounter2 = scounter + 1
            #if top rung of the current ladder is below i, adjust ladder pointers
            if Ladders[lcounter][0] <= i: 
                lcounter += 1
                lcounter2 = lcounter + 1
            #checking whether we need to check future indices beyond the current counters for ladders and/or snakes
            if Ladders[lcounter][0] < j:
                while Ladders[lcounter2][0] < j:
                    lcounter2 += 1
                #this is the lcounter we will use on this iteration of j
                lcounterfinal = lcounter2 
            else:
                #this is the lcounter we will use on this iteration of j
                lcounterfinal = lcounter 
            if Snakes[scounter][0] < j:
                while Snakes[scounter2][0] < j:
                    scounter2 += 1
                #this is the scounter we will use on this iteration of j
                scounterfinal = scounter2 
            else:
                #this is the scounter we will use on this iteration of j
                scounterfinal = scounter 
            #checking to see if we are adding a situation with a snake, 
            #ladder, or neither, and adding them to the graph
            if Snakes[scounterfinal][0] == j: #if there is a snake at j
                Edges.append((i,Snakes[scounterfinal][1]))
            elif Ladders[lcounterfinal][0] == j: #if there is a ladder at j
                Edges.append((i,Ladders[lcounterfinal][1]))
                Edges.append((i,j))
            else: #if there is no snake or ladder
                Edges.append((i,j))
            lcounter2 = lcounter + 1 #reset the lcounter2 for the next iteration
            scounter2 = scounter + 1 #reset the scoutner2 for the next iteration
    return Edges


# In[8]:

def build_connected(V,E): #build the adjacency list
    rch = []
    for vertex in V: #create a slot for each vertex
        rch.append([])
    for edge in E: #add the destination to the appropriate adjancy list
        rch[edge[0]-1].append(edge[1])
    return rch


# In[9]:

def fewest_moves(G,rch,l): #decide the fewest number of moves to the destination
    Visited = [] #dynamic programming on the steps to each vertex
    for i in range(1,l+2):
        #all vertices are unvisited to start.  Use l+2 to afford direct indexing
        Visited.append(-1) 
    ToExplore = [1] #this is a running list of the elements still to be explored
    Visited[1] = 0 #mark the first index as 0 because it is visited in 0 steps
    while len(ToExplore) >= 1:
        #initialize a list of the future elements to be added to ToExplore
        OnDeck = [] 
        for x in ToExplore: #iterate through the elements in ToExplore
            #iterate through the elements of the adjacency list of x
            for y in rch[x-1]: 
                if Visited[y] == -1: #if the destination hasn't yet been visited
                    if y != 100:
                        #if the destination isn't 100, add to on deck
                        OnDeck.append(y) 
                    #it can be visited in one more step than x
                    Visited[y] = Visited[x] + 1 
        ToExplore = OnDeck
    return Visited[l]


# In[10]:

def main(Ladders,Snakes,l):
    V = build_graph(l)
    E = build_edges(Ladders,Snakes,l)
    rch = build_connected(V,E)
    return fewest_moves(V,rch,l)
print main(B,C,100)


# In[ ]:



