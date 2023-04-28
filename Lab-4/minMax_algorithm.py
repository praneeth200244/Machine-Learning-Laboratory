# Python program to implement Min-Max algorithm

class Tree :
    def __init__(self,value,children=[]):
        self.value = value
        self.children = children
    
    def __repr__(self):
        return 'Tree({0},{1})'.format(self.value,self.children)

# Define the game tree using the Tree data structure
gameTree = Tree (0,[
    Tree (0,[
        Tree(3),
        Tree(12)
    ]),
    Tree (0,[
        Tree(8),
        Tree(2)
    ])
])

# Define the minimax algorithm function with solution path
def minimax (node, depth, maximizingPlayer):
    # Check if the node is leaf or if the maximum depth has been reached
    if depth == 0 or not node.children :
        return node.value, [node.value]
    
    if maximizingPlayer:
        maxValue = float('-inf')
        maxPath = []
        for childNode in node.children:
            childValue,childPath = minimax(childNode,(depth-1),False)
            if childValue > maxValue:
                maxValue = childValue
                maxPath = [node.value] + childPath
        return maxValue,maxPath
    else:
        minValue = float('inf')
        minPath = []
        for childNode in node.children:
            childValue,childPath = minimax(childNode,(depth-1),True)
            if childValue < minValue:
                minValue = childValue
                minPath = [node.value] + childPath
        return minValue,minPath

optimalValue,optimalPath = minimax(gameTree,2,True)
print("Optimal value: ",optimalValue)
print("Optimal path: ",optimalPath)
