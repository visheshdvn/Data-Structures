# Given a binary tree, print all nodes that don’t have a sibling.
# Edit : Print the elements in different lines. And order of elements doesn't matter.
# Input format :
# Elements in level order form (separated by space). If any node does not have left or right child, take -1 in its place.
# Output format :
# Print nodes separated by new line.
# Sample Input :
# 5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
# Sample Output :
# 9

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def nodesWithoutSibling(root):
    if root == None:
        return False
    
    left_sib = nodesWithoutSibling(root.left)
    right_sib = nodesWithoutSibling(root.right)
    
    if (left_sib is False) and (right_sib is not False):
        print(root.right.data)
    
    if (right_sib is False) and (left_sib is not False):
        print(root.left.data)

    return True

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
nodesWithoutSibling(root)
