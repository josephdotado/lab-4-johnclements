import sys
import unittest
from typing import *
from dataclasses import dataclass
import math
import matplotlib.pyplot as plt
import numpy as np
import random
sys.setrecursionlimit(10**6)

from bst import *

TREES_PER_RUN : int = 10000

def example_graph_creation() -> None:
 # Return log-base-2 of 'x' + 5.
 def f_to_graph( x : float ) -> float:
    return math.log2( x ) + 5.0
 # here we're using "list comprehensions": more of Python's
 # syntax sugar.
 x_coords : List[float] = [ float(i) for i in range( 1, 100 ) ]
 y_coords : List[float] = [ f_to_graph( x ) for x in x_coords ]
 # Could have just used this type from the start, but I want
 # to emphasize that 'matplotlib' uses 'numpy''s specific array
 # type, which is different from the built-in Python array
 # type.
 x_numpy : np.ndarray = np.array( x_coords )
 y_numpy : np.ndarray = np.array( y_coords )

 plt.plot( x_numpy, y_numpy, label = 'log_2(x)' )
 plt.xlabel("X")
 plt.ylabel("Y")
 plt.title("Example Graph")
 plt.grid(True)
 plt.legend() # makes the 'label's show up
 plt.show()


#Create a BinarSearchTree with n nodes with floats from 0.0 to 1.0
def random_tree(n: int) -> BinarySearchTree:
    def comes_before(x: float, y: float) -> bool:
        return x < y

    bst: BinarySearchTree = BinarySearchTree(comes_before, None)
    for _ in range(n):
        bst = insert(bst, random.uniform(0.0, 1.0))
    return bst

#tree height function
def tree_height(bt: BinTree) -> int:
    match bt:
        case None:
            return 0
        case Node(_, left, right):
            return 1 + max(tree_height(left), tree_height(right))


#Create a graph of average height of BSTs with n nodes
def average_height_graph(n: int) -> None:
    heights: List[float] = []
    node_counts: List[float] = []
    for i in range(1, n + 1):
        total_height: int = 0
        for _ in range(TREES_PER_RUN):
            bst: BinarySearchTree = random_tree(i)
            total_height += tree_height(bst.BinaryTree)
        average_height: float = total_height / TREES_PER_RUN
        heights.append(average_height)
        node_counts.append(float(i))

    x_numpy: np.ndarray = np.array(node_counts)
    y_numpy: np.ndarray = np.array(heights)

    plt.plot(x_numpy, y_numpy, label='Average Height of BSTs')
    plt.xlabel("Number of Nodes")
    plt.ylabel("Average Height")
    plt.title("Average Height of Random BSTs vs Number of Nodes")
    plt.grid(True)
    plt.legend()
    plt.show()
   

if (__name__ == '__main__'):
    average_height_graph(15)
    unittest.main()

