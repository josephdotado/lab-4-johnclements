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


#Functions

#Return True if tree is empty, False otherwise
def is_empty(bst: BinarySearchTree) -> bool:
    if bst.BinaryTree == None:
        return True
    return False

#Insert into a BinarySearchTree
def insert(bst: BinarySearchTree, val: Any) -> BinarySearchTree:
    if bst.comes_before(val,NodeVal) == True:
        

def insert_helper()


#Check if value is in the Binary Search Tree
def lookup(bst: BinarySearchTree, val: Any) -> BinarySearchTree:

#Delete a value from Binary Search Tree
def delete(bst: BinarySearchTree, val: Any) -> BinarySearchTree:


#Test Cases
class MyTests(unittest.TestCase):


if __name__ == "__main__":
    unittest.main()
