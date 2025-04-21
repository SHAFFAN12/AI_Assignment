romania_map = {
    'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
    'Zerind': ['Oradea', 'Arad'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras','Rimnicu Vilcea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}


from queue import Queue

def Breath_First_Search(starting_node, destination_node):
    visited = {} #Tracking City is visited or not
    distance = {} # keep track of distance
    parent = {} # parent node of specific graph
    bfs_traversal_output = []
    queue = Queue() 

    for City in romania_map.keys():
        # since intially no city is visited so there will be nothing in visited list
        visited[City] = False
        parent[City] = None
        distance[City] = [-1]

    # starting from 'Arad'
    starting_city = starting_node
    visited[starting_city] = True
    distance[starting_city] = 0
    queue.put(starting_city) # put the starting city in queue

    while not queue.empty():
        current_city = queue.get() # first element of the queue, here it will be 'arad'
        bfs_traversal_output.append(current_city)

        for neighbour_city in romania_map[current_city]:
            if not visited[neighbour_city]:
                visited[neighbour_city] = True
                parent[neighbour_city] = current_city
                distance[neighbour_city] = distance[current_city] + 1
                queue.put(neighbour_city)

    # reaching our destination city i.e 'bucharest'
    destination_city = destination_node
    path = []

    while destination_city is not None:
        path.append(destination_city)
        destination_city = parent[destination_city]

    path.reverse() # reverse the path to get the correct order  
    # printing the path to our destination city
    print(path)


# Starting City & Destination City
Breath_First_Search('Oradea', 'Bucharest')