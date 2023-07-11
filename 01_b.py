# Question 1b
# Write a Python program to implement the Best First Search (BFS) algorithm.

import heapq


def bestFirstSearch(graph, start, goal):
    openQueue = [(start, 0)]
    closed = set()
    path = {start: []}

    while openQueue:
        currentNode, cost = heapq.heappop(openQueue)

        if currentNode == goal:
            return cost, path[currentNode] + [currentNode]

        closed.add(currentNode)
        print(f"Explored Node: {currentNode}")

        for neighbor, neighborCost in graph[currentNode]:
            if neighbor not in closed and neighbor not in [node[0] for node in openQueue]:
                heapq.heappush(openQueue, (neighbor, cost+neighborCost))
                print(
                    f"Added {neighbor} to the openQueue with cost {neighborCost}")
                path[neighbor] = path[currentNode] + [currentNode]

    return None


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

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

result = bestFirstSearch(graph, start, goal)

if result is None:
    print(f"There is no path from {start} to {goal}")
else:
    cost, path = result
    print(f"The cost from {start} to {goal} is {cost}")
    print("The path is", "->".join(path))
