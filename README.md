# DSCI404-Uninformed-Search-Find-Path
![image](https://github.com/pingzhang1004/DSCI404-Uninformed-Search-Find-Path/blob/main/Uninformed_Search_Find_Path.png)

### Using dictionary data structure to build the tree search framework named city_expanded. There are several steps in this procedure:  
#### 1. Using Priority Queue pop the smallest value（the smallest path cost）in the queue.
#### 2. Using a dictionary data structure named city_expanded to build the search by loops of the key of the city_neighbors. 
#### 3. Updating the cost value in the search path, and putting the path cost value into the Priority Queue. 
#### 4. Do the steps above by a while loop until the Priority Queue is empty.

### Traceback_route(origin_city,destination_city,city_expanded,city_neighbors):
#### Trace backing the search tree to find the shortest path from the origin_city to destination_city by a while loop in city_expanded and city_neighbors. The return of this function is the distance value and list of cities that build the shortest path.
