graph= {
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

def dfs_search(graph, start_city, destination_city):
    stack = [start_city]
    visited = {}
    came_from = {}
    visited[start_city] = True
    came_from[start_city] = None
    
    while stack:
        current = stack.pop()
        
        if current == destination_city:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited[neighbor] = True
                came_from[neighbor] = current
                stack.append(neighbor)
    
    return None

start = 'Arad'
destination = 'Bucharest'
path = dfs_search(graph, start, destination)
if path:
    print("Path from", start, "to", destination, ":", path)
else:
    print("No path found from", start, "to", destination)
