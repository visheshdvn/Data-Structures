# Given a binary tree, find and return the sum of all nodes.
# Input format :

# Elements in level order form (separated by space). If any node does not have left or right child, take -1 in its place.

# Sample Input :
# 5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
# Sample Output :
# 35

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sumOfAllNodes(root):
    if root == None:
        return 0
    
    return root.data + sumOfAllNodes(root.left) + sumOfAllNodes(root.right)

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
print(sumOfAllNodes(root))
