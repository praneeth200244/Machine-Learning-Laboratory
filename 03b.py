# Question 3b
# Write a program to implement Min-Max algorithm.
class Tree:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

    def __repr__(self):
        return 'Tree({0},{1})'.format(self.value, self.children)


def minimax(node, depth, maximizing_player):
    # Check if the node is a leaf or if the maximum depth has been reached
    if depth == 0 or not node.children:
        return node.value, [node.value]
    # Apply the Minimax algorithm
    if maximizing_player:
        max_value = float("-inf")
        max_path = []
        for child_node in node.children:
            child_value, child_path = minimax(child_node, depth - 1, False)
            if child_value > max_value:
                max_value = child_value
                max_path = [node.value] + child_path
        return max_value, max_path
    else:
        min_value = float("inf")
        min_path = []
        for child_node in node.children:
            child_value, child_path = minimax(child_node, depth - 1, True)
            if child_value < min_value:
                min_value = child_value
                min_path = [node.value] + child_path
        return min_value, min_path


game_tree = Tree(0, [
    Tree(0, [
        Tree(3, [Tree(4), Tree(6)]),
        Tree(12, [Tree(9), Tree(15)])
    ]),
    Tree(0, [
        Tree(8, [Tree(10), Tree(7)]),
        Tree(2, [Tree(1), Tree(3)])
    ])
])

optimal_value, optimal_path = minimax(game_tree, 3, True)
print("Optimal value:", optimal_value)
print("Optimal path:", optimal_path)
