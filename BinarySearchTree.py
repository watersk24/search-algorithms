# Author: Kevin Waters
# Date: 10 June 2020
# Description: This program implements a Binary Search Tree ADT. The structure of the Binary Search Tree is
# is the same as a Binary Tree. To utilize the Binary Tree as a method to search data, the Binary Search Tree
# organizes data in a specific manner where the root node of the tree is larger than all values in the left subtree
# and smaller than all values in the right subtree.

from BinaryTree import BinaryTree


class BinarySearchTree(BinaryTree):
    def __init__(self, payload=None, leftChild=None, rightChild=None):
        """
        Class constructor for BinarySearchTree. This constructor is overloaded to add functionality to the class that
        measures the height of a Binary Tree.

        :param payload: User entered value.
        :param leftChild: Node on Binary Tree. Default: None
        :param rightChild: Node on Binary Tree. Default: None
        """
        BinaryTree.__init__(self, payload, leftChild, rightChild)
        if self.getPayload() is None:
            self.__height = -1
        else:
            self.__height = 0

    def getHeight(self):
        """

        :return: Returns the height of a Binary Tree. Height is measured as the longest path from
                 a root node to a leaf node.
        """
        return self.__height

    def computeHeight(self):
        """
        Calculates the height of a Binary Tree.
        :return: None
        """
        height = -1

        if self.getLeftChild() is not None:
            height = max(height, self.getLeftChild().getHeight())

        if self.getRightChild() is not None:
            height = max(height, self.getRightChild().getHeight())

        self.__height = height + 1

    def setPayload(self, payload):
        """
        Setter for payload. Overloads the setPayload to add height.

        :param payload:
        :return: None
        """
        BinaryTree.setPayload(self, payload)
        self.computeHeight()

    def insert(self, x):
        """
        Inserts user entered value at the appropriate position in the BinarySearchTree.

        :param x: User entered value.
        :return: None
        """
        if self.isEmpty():  # base case for empty tree
            self.setPayload(x)

        elif x < self.getPayload():
            # If <= operator is used a duplicate of a payload will be
            # inserted before the original. < operator is used to maintain
            # the ordering.
            if self.getLeftChild() is None:
                # If there is no left subtree one is created with value x
                self.setLeftChild(BinarySearchTree(x))
                self.computeHeight()

            else:  # Recursively insert into left subtree
                self.getLeftChild().insert(x)
                self.computeHeight()

        else:  # base case for x >= self.payload
            if self.getRightChild() is None:
                # If there is no right subtree one is created with value x
                self.setRightChild(BinarySearchTree(x))
                self.computeHeight()

            else:  # Recursively insert into right subtree
                self.getRightChild().insert(x)
                self.computeHeight()

    def find(self, x):
        """
        Performs a search of the tree to find a user entered value.

        :param x: User entered value.
        :return: Returns the user entered value if value is in the search tree.
        """
        if self.isEmpty():
            return None

        elif x == self.getPayload():
            return self.getPayload()

        elif x < self.getPayload():
            if self.getLeftChild() is None:
                return None
            else:
                return self.getLeftChild().find(x)

        else:
            if self.getRightChild() is None:
                return None
            else:
                return self.getRightChild().find(x)

    def minValue(self):
        """
        
        :return: Returns the minimum value of the tree.
        """
        if self is None:
            return None
        elif self.getLeftChild() is None:
            return self.getPayload()
        else:
            return self.getLeftChild().minValue()

    def maxValue(self):
        """

        :return: Returns the maximum value of the tree.
        """
        if self is None:
            return None
        elif self.getRightChild() is None:
            return self.getPayload()
        else:
            return self.getRightChild().maxValue()

    def inorderTraversal(self):
        """
        Performs an inorder list traversal on a Binary Tree.
        :return: Returns value of leftChild of root node before returning root node.
        """
        result = ""
        if self.isEmpty():
            return result
        else:
            # Visit left node
            if self.getLeftChild() is not None:
                result += self.getLeftChild().inorderTraversal()

            # Visit root node
            result += " " + str(self.getPayload()) + "(" + str(self.getHeight()) + ")"

            # Visit right node
            if self.getRightChild() is not None:
                result += " " + self.getRightChild().inorderTraversal()

            return result


def main():
    BST = BinarySearchTree()
    print("isEmpty() = " + str(BST.isEmpty()))
    BST.setPayload(12)
    print("Binary Search Tree=", BST)
    print("isEmpty() = " + str(BST.isEmpty()))
    BST.insert(4)
    print("Binary Search Tree=", BST)
    BST.insert(6)
    print("Binary Search Tree=", BST)
    BST.insert(15)
    print("Binary Search Tree=", BST)
    print("Minimum value for this subtree is:", BST.minValue())
    BST.insert(165)
    print("Binary Search Tree=", BST)
    BST.insert(44)
    print("Binary Search Tree=", BST)
    print("Maximum value for this subtree is:", BST.maxValue())
    print("Height of Binary Search Tree is: ", BST.getHeight())
    print("Inorder traversal=", BST.inorderTraversal())


if __name__ == "__main__":
    main()
