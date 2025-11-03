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
bt1: BinTree = Node(10, Node(5, None, None), Node(15, None, None))
bt2: BinTree = None

bst1: BinarySearchTree = BinarySearchTree(comp, bt1)
bst2: BinarySearchTree = BinarySearchTree(comp, bt2)


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
    new_tree: BinTree = insert_helper(bst.BinaryTree, new_val, bst.comes_before)
    return BinarySearchTree(bst.comes_before, new_tree)


#Helper function to insert value into BinTree
def insert_helper(bt: BinTree, new_val: Any, comes_before: Callable[[Any,Any], bool]) -> BinTree:
    match bt:
        case None:
            return Node(new_val, None, None)
        case Node(val, left, right):
            if comes_before(new_val,val):
                return Node(val, insert_helper(left, new_val, comes_before), right)
            else:
                return Node(val, left, insert_helper(right, new_val, comes_before))


#Look up a value in a BinarySearchTree
def lookup(bst: BinarySearchTree, val: Any) -> bool:
    return lookup_helper(bst.BinaryTree, val, bst.comes_before)


#Helper function to look up value in BinTree
def lookup_helper(bt: BinTree, val: Any, comes_before: Callable[[Any,Any], bool]) -> bool:
    match bt:
        case None:
            return False
        case Node(v, left, right):
            if v == val:
                return True
            elif comes_before(val, v):
                return lookup_helper(left, val, comes_before)
            else:
                return lookup_helper(right, val, comes_before)


#Delete a value from a BinarySearchTree
def delete(bst: BinarySearchTree, val: Any) -> BinarySearchTree:
    new_tree: BinTree = delete_helper(bst.BinaryTree, val, bst.comes_before)
    return BinarySearchTree(bst.comes_before, new_tree)


#Helper function to delete a value from a BinTree
def delete_helper(bt: BinTree, val: Any, comes_before: Callable[[Any,Any], bool]) -> BinTree:
    match bt:
        case None:
            return None
        case Node(v, left, right):
            if v == val:
                # Case 1: No children
                if left is None and right is None:
                    return None
                # Case 2: One child
                elif left is None:
                    return right
                elif right is None:
                    return left
                # Case 3: Two children
                else:
                    # Find the minimum value in the right subtree
                    min_val = find_min(right)
                    # Replace current node's value with min_val
                    new_right = delete_helper(right, min_val, comes_before)
                    return Node(min_val, left, new_right)
            elif comes_before(val, v):
                new_left = delete_helper(left, val, comes_before)
                return Node(v, new_left, right)
            else:
                new_right = delete_helper(right, val, comes_before)
                return Node(v, left, new_right)


#Helper function to find the minimum value in a BinTree
def find_min(bt: BinTree) -> Any:
    match bt:
        case None:
            raise ValueError("Tree is empty")
        case Node(v, None, _):
            return v
        case Node(_, left, _):
            return find_min(left)

#Comparison function
def comp(n1: int, n2: int) -> bool:
    return n1 < n2


#Test Cases


class MyTests(unittest.TestCase):
    def test_is_empty1(self):
        self.assertEqual(is_empty(bst1), False)
    
    def test_is_empty2(self):
        self.assertEqual(is_empty(bst2), True)
    
    def test_insert1(self):
        self.assertEqual(insert(bst1, 7), BinarySearchTree(comp, Node(10, Node(5, Node(7, None, None), None), Node(15, None, None))))
    
    def test_lookup1(self):
        self.assertEqual(lookup(bst1, 5), True)
    
    def test_delete1(self):
        self.assertEqual(delete(bst1, 5), BinarySearchTree(comp, Node(10, None, Node(15, None, None))))
    
    




if __name__ == "__main__":
    unittest.main()