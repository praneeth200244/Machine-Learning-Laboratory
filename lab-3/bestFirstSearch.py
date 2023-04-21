# Python program to implement Best First Search algorithm

import heapq

def bestFirstSearch(graph, start, goal) :
    # Initialize the priority queue with start node
    frontier = [(0,start)]

    # Initialize the explored set
    explored = set()

    #Loop until frontier is empty
    while frontier :
        #Pop the node with highest priority
        (cost, currentNode) = heapq.heappop(frontier)

        # Check if the current node is goal
        if currentNode == goal :
            return cost

        #Add the current node to tthe explored set
        explored.add(currentNode)
        print(f"Explored node: {currentNode}")

        # Explore the neighbour of the current node
        for neighbour, neighbourCost in graph[currentNode]:
            #Check if the neighbour is not in the explored set and not in the frontier
            if neighbour not in explored and neighbour not in [node[1] for node in frontier]:
                # Add the neighbour to the frontier with its priority being its heuristic cost
                heapq.heappush(frontier,(cost + neighbourCost,neighbour))
                print(f"Added node {neighbour} to frontier with cost {neighbourCost}")
    # If the goal cannot be reacged, return None
    return None

# Example graph
graph = {
    'A' : [('B',5),('C',6)],
    'B' : [('D',4),('E',7)],
    'C' : [('F',9),('G',8)],
    'D' : [('H',3)],
    'E' : [('I',6)],
    'F' : [('J',5)],
    'G' : [('K',7)],
    'H' : [('L',1)],
    'I' : [('M',2)],
    'J' : [('N',3)],
    'K' : [('O',4)],
    'L' : [],
    'M' : [],
    'N' : [],
    'O' : [('P',1)],
    'P' : []
}

# Get start and goal nodes from the user
start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

# Run the Best First Search algorithm
result = bestFirstSearch(graph, start, goal)

# Print the result
if result is not None:
    print(f"The minimum cost from {start} to {goal} is {result}")
else:
    print(f"There is no path from {start} to {goal}")