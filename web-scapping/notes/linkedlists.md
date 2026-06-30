# Linked Lists
**Date:** June 29, 2026

## Definition
A **linked list** is a linear data structure consisting of *nodes*.  
Each node has:
- `data`: the value it stores
- `next`: a reference to the next node in the list

```
Head
 ↓
[10] ——→ [20] ——→ [30] ——→ None
```

## Time Complexity of Key Operations

| Operation            | Time Complexity |
|----------------------|----------------|
| Insert at beginning  | O(1)           |
| Insert at end        | O(n)           |
| Search               | O(n)           |
| Delete by value      | O(n)           |
| Reverse              | O(n)           |

## Reversing a Linked List (Algorithm)

```python
previous = None
current = head

while current:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node

head = previous
```

## Practice Summary
- ✅ Implemented `Node` and `LinkedList` classes
- ✅ Traversed a linked list
- ✅ Inserted nodes (beginning, end, by index)
- ✅ Searched and counted occurrences
- ✅ Deleted nodes (beginning, end, by value)
- ✅ Updated a node’s value
- ✅ Reversed the linked list

> **Note:** Linked lists excel at quick insertions and deletions, but direct access to elements always requires traversal from the head.