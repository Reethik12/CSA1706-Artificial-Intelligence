# Water Jug problem
from collections import deque
A=4  
B=3 
GOAL=2
visited=set()
def water_jug_problem():
    queue = deque()
    queue.append((0, 0))
    while queue:
        a,b=queue.popleft()
        if (a,b) in visited:
            continue
        print(f"Jug A:{a}L,Jug B:{b}L")
        visited.add((a, b))
        if a == GOAL or b == GOAL:
            print("Goal reached!")
            return
        next_states=[
            (A,b),      
            (a,B),      
            (0,b),      
            (a,0),     
            (min(a+b,A),b-(min(a+b,A)-a)),  
            (a-(min(a+b,B)-b),min(a+b,B))   
        ]
        for state in next_states:
            if state not in visited:
                queue.append(state)
water_jug_problem()
