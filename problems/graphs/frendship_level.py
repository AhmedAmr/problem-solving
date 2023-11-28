from collections import deque
from typing import List

def get_friendship_level(arr: List[List[int]], src:int, dest:int) -> int:
    visited = {}
    queue = deque([(src, 0)])

    while queue:
        node, distance = queue.popleft()

        if node in visited:
            continue

        visited[node] = True

        if node == dest:
            return distance
        
        for i in range(len(arr)):
            if arr[node][i]:
                queue.append((i, distance+1))
    return -1


