# Abstract Data Type
Can represent one thing and do something but how your implement it has your discretion.

Like queues.

# Stacks & Queues
## Queues
* **FIFO:** First in first out.
  * **Enqueue:** enter queue.
  * **Dequeue:** exit queue.

## Stacks
* **LIF0:** Last in first out.
  * **Push:** add to top.
  * **Pop:** take from top.


**Example**:
```
  typedef struct
  {
    person people[CAPACITY];
    int size;
  }
  stack;
  ```

# Linked Lists


The simplicity of linear lists accompanied by their capacity to handle dynamic datasets with unknown length, make them ideal candidates for manipulating more complicated data structures like graphs and trees. 

Additionally, their efficient insertion and deletion, makes them great for building stacks and queues. 


## What are linked lists?! 
Before getting into details for how linked lists work, there is one VERY important question that must be answered. What are they?

Linked List Structure
Anatomically speaking, a linked list is a data structure consisting of nodes. Each node contains a:

* **Data element:** This can be any data type (ex. integers, strings, and booleans) 

* **Pointer element:** A reference to the address of the next node in the chain. 
The first node in the list is called the head. We access all other nodes from the head. In non-circular lists (more on these at the end), you can traverse each node until an address points to null; this is our last node in the list.



# Trees
Grows down and has width and height
# Binary Search Trees
Lend themselves well to binary search.

Has nodes with 0, 1, or 2 pointers.

# Dictionaries
Holy grail of algorithms. 

key: value

# Hash Tables
Take inputs and outputting a simpler version.

**Hashing:** "bucketize" the data from larger domain to a smaller range.

**Hash Tables ( O(n/k) ):** leverage arrays and linked lists. Use array filled with either pointers or null values to get to buckets then stitch groups together with linked lists if needed. But uses a huge amount of memory.

# Tries
Truly constant time
Tree and each node is an array.