#Implementing BFS
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
def bfs(start):
    visited = []          
    queue = [start]      
    while queue:
        node = queue.pop(0)     
        if node not in visited:
            print(node)         
            visited.append(node)
            queue += graph[node] 
bfs('A')
