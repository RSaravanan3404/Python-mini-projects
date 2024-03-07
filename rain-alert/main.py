class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
def pre_order_trav(curr, pre_order_result):
    if not curr:
        return
    pre_order_result.append(curr.data)
    pre_order_trav(curr.left, pre_order_result)
    pre_order_trav(curr.right, pre_order_result)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(8)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.right.left = Node(9)
    root.right.right.right = Node(10)

    pre_order_result = []
    pre_order = pre_order_trav(root, pre_order_result)

    print("The preOrder Traversal is:", end=" ")
    print(*pre_order_result)