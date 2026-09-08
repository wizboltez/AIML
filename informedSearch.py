# search algo -> locate specific target data within collection of info
# 2 types of search algo 
# 1. uninformed search -> no info about how to reach , so it explores every possible path
# 2. informed search -> additional info that is a deciding factor of which path looks most promising
# additional info is called heuristic -> solving problem using practical approach and past exp
# heuristic -> h(n)
# where:
# n = current node/state
# h(n) = estimated cost from current node to goal
# a* star algo combines 2 things -> g(n)(actual cost how much we spent travelling)+h(n)(estimated future cost how much we think remains)

# location acts as nodes
# roads acts as edges

# what makes a* informed 
# A* is called an informed search algorithm because it uses heuristic information h(n) to estimate the remaining cost from a state to the goal. This additional knowledge helps it prioritize more promising states instead of exploring blindly


# we're using a star algo in this
import heapq #we select the node with smallest f val 
#heapq is priority queue
#below is a dict 
#key -> val
#basically its location -> connected loc
graph={
    'hosp':[('a',4),('c',2)],
    'a':[('hosp',8),('b',4),('c',1)],
    'b':[('a',4),('d',3)],
    'c':[('hosp',2),('a',1),('d',2)],
    'd':[('b',3),('c',2),('acc',1)],
    'acc':[('d',1)]
}
#[] -> list , mutable 
#() -> tuple , immutable raises type error later on
heuristic={
    'hosp':7,
    'a':5,
    'b':3,
    'c':4,
    'd':1,
    'acc':0
}#node -> estimated cost to the goal 
# A* Search
# f(n) = g(n) + h(n)
# g(n) = actual cost from start
# h(n) = estimated cost to goal

def a_star(start ,end) :
    open_list=[(heuristic[start], start)]#contains nodes that have been discovered but still need to be explored
    g_cost={start:0}#stores cost from start node
    parent={start:None}#stores prev node
    while open_list:#runs as logn as there are unexplored nodes left in open_list
        f, current=heapq.heappop(open_list)#get the smallest element from the heap
        if current == end:
            break

        for neighbour, cost in graph[current]:#we look at every neighbour of current node
            new_g=g_cost[current]+cost#g(new)=g(current)+edge cost
            if neighbour not in g_cost or new_g<g_cost[neighbour]:
                g_cost[neighbour]=new_g#update new latest travel cost for this node
                f=new_g+heuristic[neighbour]#calculate cost spent and estimated cost remaining 
                parent[neighbour]=current#store node where we came from 
                heapq.heappush(open_list,(f,neighbour))#add the val so far of that node for future calc in priority queue

    # Safety Check: If the goal node is missing from our parent dictionary, 
    # it means there is no possible connected path from the start to the goal.
    if end not in parent:
        return None, None

    #reconstrcut path now
    path = []#store sequence of nodes along with routes
    current = end#start backtracking
    while current is not None:
        path.append(current)#add curret to route 
        current=parent[current]#shift pointer back to the parent

    path.reverse()#we've stored list from end to start so we reverse it in order to traverse from strat to end

    return path, g_cost[end]#return sequential path list and total accum cost

# Define operational variables for the beginning and endpoint of the journey
start = "Hospital"
end = "Accident"

path ,cost=a_star(start,end)#invoke function and return tuple into path and cost var
print("optimal route: ","-> ".join(path))# example : Optimal Route: Hospital -> C -> D -> Accident
print("total cost : ",cost,"km")