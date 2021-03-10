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
        if self.right is not None:
            left_height = self.right.maxDepth()
        max_depth = max(left_height, right_height)
        return max_depth + 1


root = BinaryTreeNode(8)
root.insert(5)
root.insert(11)
root.insert(2)
root.insert(6)
root.insert(7)
root.insert(10)
root.insert(12)

print(root.search(5))
root.delete(5)
print(root.search(5))
print(root.search(6))
print(root.search(7))