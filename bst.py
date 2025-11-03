import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

#Data Defintions

BinTree: TypeAlias = Union[None, "Node"]


@dataclass(frozen = True)
class BinarySearchTree:
    comes_before: Callable[[Any,Any], bool]
    BinaryTree: BinTree


@dataclass (frozen = True)
class Node:
    val: Any
    left: BinTree
    right: BinTree


#Examples 
bst1: BinTree = Node(10, Node(5, None, None), Node(15, None, None))
bst2: BinTree = None


#Functions


#Return True if tree is empty, False otherwise
def is_empty(bst: BinarySearchTree) -> bool:
    match bst.BinaryTree:
        case None:
            return True
        case Node():
            return False

#Insert value into a BinarySearchTree
def insert(bst:BinarySearchTree, new_val: Any) -> BinarySearchTree:
    def insert_helper(bt: BinTree, new_val: Any) -> BinTree:
        match bt:
            case None:
                return Node(new_val, None, None)
            case Node(v, left, right):
                if bst.comes_before(new_val, v):
                    return Node(v, insert_helper(left, new_val), right)
                else:
                    return Node(v, left, insert_helper(right, new_val))
    new_tree = insert_helper(bst.BinaryTree, new_val)
    return BinarySearchTree(bst.comes_before, new_tree)

#Look up a value in a BinarySearchTree
def lookup(bst: BinarySearchTree, val: Any) -> bool:
    def lookup_helper(bt: BinTree, val: Any) -> bool:
        match bt:
            case None: 
                return False
            case Node(v, left, right):
                if v == val:
                    return True
                elif bst.comes_before(val, v):
                    return lookup_helper(left, val)
                else:
                    return lookup_helper(right,val)
    return lookup_helper(bst.BinaryTree, val)

#Delete a value from a BinarySearchTree
def delete(bst: BinarySearchTree, val: Any) -> BinarySearchTree:
    def delete_helper(bt: BinTree, val: Any) -> BinTree:
        match bt:
            case None:
                return None
            case Node(v, left, right):
                if v == val:
                    if left is None and right is None:
                        return None
                    elif left is None:
                        return right
                    elif right is None:
                        return left
                    else:
                        # Find the minimum value in the right subtree
                        min_larger_node = right
                        while min_larger_node.left is not None:
                            min_larger_node = min_larger_node.left
                        # Replace value with the minimum value from the right subtree
                        new_right = delete_helper(right, min_larger_node.val)
                        return Node(min_larger_node.val, left, new_right)
                elif bst.comes_before(val, v):
                    return Node(v, delete_helper(left, val), right)
                else:
                    return Node(v, left, delete_helper(right, val))
    new_tree = delete_helper(bst.BinaryTree, val)
    return BinarySearchTree(bst.comes_before, new_tree)

#Test Cases

class MyTests(unittest.TestCase):


if __name__ == "__main__":
    unittest.main()