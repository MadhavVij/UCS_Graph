import sys
#from Queue import Queue
from queue import PriorityQueue
from heapq import heappush, heappop
import time
start_time = time.time()

#as PriorityQueue is not present in python 2.4 so, a class was created
# class PriorityQueue(Queue):
#     def _init(self, maxsize):
#         self.maxsize = maxsize
#         self.queue = []
#     def _put(self, item):
#         return heappush(self.queue, item)
#     def _get(self):
#         return heappop(self.queue)

#from queue import PriorityQueue
def create_graph(filename):
  graph = {}
  file = open(filename, 'r')
  for line in file:
    if 'END OF INPUT' in line:
      return graph
    nodeA, nodeB, d = line.split()
    graph.setdefault(nodeA, []).append((nodeB, d))
    graph.setdefault(nodeB, []).append((nodeA, d))


def uniformed_cost_search(graph, start, goal): 
  visited = set() #keeps track of all visited nodes
  path = [] #stores the path for each iteration
  queue = PriorityQueue() #stores and sorts all neighbours
  queue.put((0, [start]))
  while queue:

    #if there is no path between two nodes
    if queue.empty():
      print ('distance: infinity\nroute:\nnone')
      print(f"--- {time.time() - start_time} seconds ---")
      return 

    cost, path = queue.get()
    node = path[len(path)-1]
    if node not in visited:
      visited.add(node)
      if node == goal:
        path.append(cost) #the shortest path is found
        return path

      for x in neighbors(graph, node):
        if x not in visited:
          total_cost = cost + int(get_cost(graph, node, x))
          temporary = path[:]
          temporary.append(x)
          queue.put((total_cost, temporary)) #creating queue such that it has all the values for path

def neighbors(graph,node):
  #finding neighbors in graph
  elements = graph[node]
  return [x[0] for x in elements]

def get_cost(graph, from_node, to_node):
  #calc. cost of each edge
  position = [x[0] for x in graph[from_node]].index(to_node)
  return graph[from_node][position][1]

def display_path(graph,path):
  #display in proper format
  distance = path[-1]
  print(f'distance: {distance}')
  print ('route: ')
  for x in path[:-2]:
    y = path.index(x)
    position = [z[0] for z in graph[x]].index(path[y+1])
    cost = graph[x][position][1]
    print(f'{x} to {path[y + 1]}, {cost} km')
  print(f"--- {time.time() - start_time} seconds ---")

def main():
  #reading all arguments
  filename = sys.argv[1]
  start = sys.argv[2]
  goal = sys.argv[3]

  #create Graph (from input file)
  graph = {}
  graph = create_graph(filename)
  print(graph)

  #checking for exceptions
  if start not in graph.keys():
    print ('Improper start node')
    sys.exit()
  if goal not in graph.keys():
    print ('Improper goal node')
    sys.exit()  

  #finding path and cost using Uniformed Cost Search
  path = []
  if path := uniformed_cost_search(graph, start, goal):
    display_path(graph,path)


if __name__ == '__main__': 
  main()