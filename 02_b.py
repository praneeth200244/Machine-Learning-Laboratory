
# Question 2b
# Write a program to implement the A* algorithm


import heapq


def aStar(graph, heuristic, start, goal):
    openQueue = [(start, (0+heuristic[start]))]
    parent = {start: None}
    closedQueue = set()
    cost = {start: 0}

    while openQueue:
        (currentNode, fvalue) = heapq.heappop(openQueue)

        if currentNode == goal:
            path = []
            while currentNode is not None:
                path.append(currentNode)
                currentNode = parent[currentNode]

            path.reverse()

            return (path, cost[goal])

        closedQueue.add(currentNode)

        for neighbor, neighborCost in graph[currentNode]:
            distanceValue = cost[currentNode] + neighborCost

            if neighbor in closedQueue:
                if distanceValue >= cost.get(neighbor, float('inf')):
                    continue

            if neighbor not in [node[0] for node in openQueue] or distanceValue < cost.get(neighbor, float('inf')):
                cost[neighbor] = distanceValue
                parent[neighbor] = currentNode
                heapq.heappush(
                    openQueue, (neighbor, (heuristic[neighbor] + distanceValue)))

    return None


# Example graph
graph = {
    'A': [('B', 5), ('C', 6)],
    'B': [('D', 4), ('E', 7)],
    'C': [('F', 9), ('G', 8)],
    'D': [('H', 3)],
    'E': [('I', 6)],
    'F': [('J', 5)],
    'G': [('K', 7)],
    'H': [('L', 1)],
    'I': [('M', 2)],
    'J': [('N', 3)],
    'K': [('O', 4)],
    'L': [],
    'M': [],
    'N': [],
    'O': [('P', 1)],
    'P': []
}

# Heuristic function
heuristic = {
    'A': 10,
    'B': 8,
    'C': 7,
    'D': 6,
    'E': 8,
    'F': 3,
    'G': 2,
    'H': 5,
    'I': 6,
    'J': 3,
    'K': 2,
    'L': 1,
    'M': 4,
    'N': 2,
    'O': 4,
    'P': 0
}

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

result = aStar(graph, heuristic, start, goal)

if result is None:
    print(f"There is no path from {start} to {goal}")
else:
    path, cost = result
    print(f"The minimum cost from {start} to {goal} is {cost}")
    print("The path is: ", "->".join(path))
