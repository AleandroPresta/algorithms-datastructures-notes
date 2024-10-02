# Queues

## Table of Contents

1. [Introduction](#introduction)
2. [Types of Queues](#types-of-queues)
    - [Simple Queue](#simple-queue)
    - [Circular Queue](#circular-queue)
    - [Priority Queue](#priority-queue)
    - [Double-Ended Queue (Deque)](#double-ended-queue-deque)
3. [Operations and Complexities](#operations-and-complexities)
    - [Enqueue (Insertion)](#1-enqueue-insertion)
    - [Dequeue (Deletion)](#2-dequeue-deletion)
    - [Peek/Front](#3-peekfront)
    - [IsEmpty](#4-isempty)
    - [IsFull](#5-isfull)
    - [Size](#6-size)
4. [Summary Table](#summary-table)

## Introduction

A **queue** is a linear data structure that follows the First In First Out (FIFO) principle. This means that the first element added to the queue will be the first one to be removed.

## Types of Queues

### Simple Queue

Also known as a linear queue, where insertion happens at the rear and deletion at the front.

### Circular Queue

A more efficient queue where the last position is connected back to the first position, forming a circle.

### Priority Queue

A queue where elements are dequeued based on priority rather than the order they were enqueued.

### Double-Ended Queue (Deque)

A queue where insertion and deletion can happen from both ends (front and rear).

## Operations and Complexities

### 1. Enqueue (Insertion)

Adds an element to the end (rear) of the queue.

-   **Simple Queue**: O(1)
-   **Circular Queue**: O(1)
-   **Priority Queue**: O(log n) (if implemented with a binary heap)
-   **Deque**: O(1)

### 2. Dequeue (Deletion)

Removes an element from the front of the queue.

-   **Simple Queue**: O(1)
-   **Circular Queue**: O(1)
-   **Priority Queue**: O(log n) (if implemented with a binary heap)
-   **Deque**: O(1)

### 3. Peek/Front

Returns the front element of the queue without removing it.

-   **Simple Queue**: O(1)
-   **Circular Queue**: O(1)
-   **Priority Queue**: O(1)
-   **Deque**: O(1)

### 4. IsEmpty

Checks if the queue is empty.

-   **Simple Queue**: O(1)
-   **Circular Queue**: O(1)
-   **Priority Queue**: O(1)
-   **Deque**: O(1)

### 5. IsFull

Checks if the queue is full. This is mainly applicable to fixed-size queues.

-   **Simple Queue**: O(1)
-   **Circular Queue**: O(1)
-   **Priority Queue**: O(1)
-   **Deque**: O(1)

### 6. Size

Returns the number of elements in the queue.

-   **Simple Queue**: O(1)
-   **Circular Queue**: O(1)
-   **Priority Queue**: O(1)
-   **Deque**: O(1)
