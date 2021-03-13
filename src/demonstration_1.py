"""
You are given a binary tree.

Write a function that can find the **maximum depth** of the binary tree. The
maximum depth can be defined as the number of nodes found along the longest
path from the root down to the furthest leaf node. Remember, a leaf node is a
node that has no children.

Example:

Given the following binary tree

    5
   / \
  12  32
     /  \
    8    4

your function should return the depth = 3.
"""


class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        new_node = BinaryTreeNode(value)
        if value < self.value:
            if self.left is None:
                self.left = new_node
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = new_node
            else:
                self.right.insert(value)

    def search(self, target):
        if self.value == target:
            return True
        if self.value > target:
            if self.left is None:
                return False
            else:
                found = self.left.search(target)
                return found
        else:
            if self.left is None:
                return False
            else:
                return self.right.search(target)

    def find_minimum_value(self):
        if self.left is None:
            return self.value
        else:
            return self.left.find_minimum_value()

    def delete(self, value):
        if self.value > value:
            self.left = self.left.delete(value)
        elif self.value < value:
            self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is not None and self.right is None:
                return self.left
            elif self.right is not None and self.left is None:
                return self.right
            else:
                next_min_value = self.right.find_minimum_value()
                self.value = next_min_value
                self.right = self.right.delete(next_min_value)
        return self

    def maxDepth(self):
        if self.left is None and self.right is None:
            return 1
        left_height = 0
        right_height = 0
        if self.left is not None:
            left_height = self.left.maxDepth()
            print(left_height)
        if self.right is not None:
            right_height = self.right.maxDepth()
            print(right_height)
        max_depth = max(left_height, right_height)
        return max_depth + 1
    # //PRE_ORDER
    def print_tree_pre_order(self):
        # between these commented out lines is the code 
        print(self.value)
        # that is the reason you are looking at this tree
        # in this case we are just wanting to see the values 
        # in our console
        if self.left is not None:
            self.left.print_tree_depth_first_traversal()
        if self.right is not None:
            self.right.print_tree_depth_first_traversal()
    
    # //IN_ORDER_LOW_TO_HIGH
    def print_tree_in_order_low(self):
        # evaluating the current node
        if self.left is not None:
            self.left.print_tree_in_order_low()
        print(self.value)
        if self.right is not None:
            self.right.print_tree_in_order_low()

    # //IN_ORDER_HIGH_TO_LOW
    def print_tree_in_order_high(self):
        # evaluating the current node
        if self.right is not None:
            self.right.print_tree_in_order_high()  
        print(self.value)
        if self.left is not None:
            self.left.print_tree_in_order_high()
   
#    POST_ORDER_TRAVERSAL
    def print_tree_post_order(self):
        # evaluating the current node
        if self.left is not None:
            self.left.print_tree_post_order()

        if self.right is not None:
            self.right.print_tree_post_order()  
        print(self.value)
# iterative pre-order traversal
def print_tree_iterative_dft(start_node):
    # THE ESSENTIAL SET-UP PHASE
    # here we create a stack to keep track of nodes
    stack =[]
    # add the first node onto the stack
    stack.append(start_node)
    # THE ESSENTIAL WHILE LOOP
    while len(stack) > 0:
        # THE ESSENTIAL POP
        current_node = stack.pop()
        # BELOW IS THE NON ESSENTIAL CODE 
        # WHERE YOU DO WHAT YOU 
        # CREATED THIS FUNCTION FOR
        print(current_node.value)
        # THE FINAL ESSENTIAL PART
        # ADD THE CHILDREN TO THE STACK
        if current_node.right is not None:
            stack.append(current_node.right)
        if current_node.left is not None:
            stack.append(current_node.left)

# bredth first traversal
def print_tree_iterative_bft(start_node):
    # here we create a stack to keep track of nodes
    queue =[]
    # add the first node onto the stack
    queue.append(start_node)
    while len(queue) > 0:
        # evaluate the top node on the queue
        current_node = queue.pop(0)
        # evaluate the current node
        print(current_node.value)
        # add all children to the queue
        if current_node.left is not None:
            queue.append(current_node.left)

        if current_node.right is not None:
            queue.append(current_node.right)

# find every path in the tree and put it somewhere
all_paths = []
def find_paths_to_leaves(current_node, current_path):
    new_path = current_path + [current_node.value]
    if current_node.left is None and current_node.right is None:
        all_paths.append(new_path)
    if current_node.left is not None:
        find_paths_to_leaves(current_node.left, new_path.copy())
    if current_node.right is not None:
        find_paths_to_leaves(current_node.right, new_path.copy())


root = BinaryTreeNode(8)
root.insert(5)
root.insert(4)
root.insert(7)
root.insert(12)
root.insert(11)
root.insert(13)
find_paths_to_leaves(root, [])
print(all_paths)