import sys
from queue import PriorityQueue


def parse_input(filename): # Parses through the input file and creates a dictionary with locations and respective costs
  # the key of city_neighbors : each city in the map, for example city a, b, c, ......
  # the value of city_neighbors : all linked cities to the key of city_neighbors , for example the linked cities to city a are city m, city n, city w.
  city_neighbors = {}
  file = open(filename, 'r')
  lines = file.readlines()
  file.close()
  for line in lines[:-1]:
    data = line.split()
    city = data[0]
    linked_city = data[1]
    # the path cost between two linked cites
    cost_cities = data[2]
    if data == 'END OF INPUT':
      return city_neighbors
    else:    #
      if city in city_neighbors:
          city_neighbors[city][linked_city] = float(cost_cities)
      else:
          city_neighbors[city] = {linked_city: float(cost_cities)}   #if city a link to city b, city a is the key of city_neighbors. Then , add city b as a value of the key(city a) 
      if linked_city in city_neighbors:
          city_neighbors[linked_city][city] = float(cost_cities)    #if city a link to city b, city b is the key of city_neighbors, Then , add city a as a value of the key(city b) 
      else:
          city_neighbors[linked_city] = {city: float(cost_cities)}
  return city_neighbors

def uninformed_search(origin_city, destination_city, city_neighbors): # Implements a graph based uniform cost search
    fringe_queue = PriorityQueue()  # Priority Queue pop the smallest value（the smallest path cost）in the queue when get the element from it
    fringe_queue.put((0, origin_city))    # put the path cost of betwwen the current city and the origin_city
    city_expanded = {}
    city_expanded[origin_city] = ("", 0)
    track_smallestPathNode = []
    max_node = 0
    while not fringe_queue.empty():
      if len(fringe_queue.queue) > max_node:
        max_node = len(fringe_queue.queue)
      cost_smallestPath, city_smallestPath = fringe_queue.get()
      if city_smallestPath == destination_city:
        break
      if city_smallestPath in track_smallestPathNode:
        continue
      track_smallestPathNode.append(city_smallestPath)  # 
      for city in city_neighbors[city_smallestPath]:   # expand all of the linked cities of the city which has smallestPath until now
        # igenerated += 1
        fringe_queue.put((city_neighbors[city_smallestPath][city]+city_expanded[city_smallestPath][1], city))
        if city not in city_expanded:
          city_expanded[city] = (city_smallestPath, city_neighbors[city_smallestPath][city]+city_expanded[city_smallestPath][1])
    return city_expanded
    
def traceback_route(origin_city,destination_city,city_expanded,city_neighbors):
    route = []
    distance = "infinity"
    if destination_city in city_expanded:
      distance = 0.0
      city_smallestPath = destination_city
      while city_smallestPath != origin_city:
          distance += city_neighbors[city_expanded[city_smallestPath][0]][city_smallestPath]
          route.append(city_smallestPath)
          city_smallestPath = city_expanded[city_smallestPath][0]
    return route,distance

# Defining main function
def main():
  if len(sys.argv) == 4:
      file_name = sys.argv[1]
      origin_city = sys.argv[2]
      destination_city = sys.argv[3]
      city_neighbors = parse_input(file_name)
      city_expanded = uninformed_search(origin_city, destination_city, city_neighbors)
      route, distance= traceback_route(origin_city,destination_city,city_expanded,city_neighbors)
      print("distance: {} km".format(distance))
      print("route:")
      if distance == 0:
        print("{} to {}, {} km".format(origin_city, origin_city, 0))  
      else:
        city_passed = origin_city
        if len(route) == 0:
          print("none")
        else:
          for city in route[::-1]:
            print("{} to {}, {} km".format(city_passed, city, city_neighbors[city_passed][city]))
            city_passed = city
  else:
    print("Please input correct commands, for example: find_route input1.txt London Frankfurt ")

if __name__=="__main__":
   main()