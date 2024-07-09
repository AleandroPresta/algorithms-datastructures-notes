# Trees

## Table of Contents
1. [Introduction and Nomenclature](#introduction-and-nomenclature)
2. [Types of Trees](#types-of-trees)
    - [Binary Trees](#binary-trees)
    - [Binary Search Trees](#binary-search-tree)

## Introduction and Nomenclature
The tree data structure is a type of graph. A tree has a **root node** (top node) that will have a relationship with its child nodes. The path that connects the root node to the child nodes is called a **branch**. The **leaf node** is the node that doesn’t have any children and is not the root node.

**Height** in trees is the number of nodes from the highest branch to the root node. The **depth** of a tree is the count of nodes from a specific node to the root node.

![alt text](images/tree_diagram.png)

## Types of Trees
### Binary Trees
A **binary tree** is a tree that has up to 2 child nodes:

![alt text](images/binary_tree.png)

### Binary Search Trees
A **binary search tree** is a binary tree with one additional property: *given a parent node with his two children, the value of the child on the left is always less then the value of the father and the value of the child on the right is always greater then the value of the father*.

