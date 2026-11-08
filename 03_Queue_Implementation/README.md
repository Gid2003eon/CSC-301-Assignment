# QUEUE IMPLEMENTATION USING PYTHON

## CSC 301 – Data Structures Assignment

### 1. Introduction

This project demonstrates the implementation of a Queue data structure using Python.

A queue is a linear data structure that follows the FIFO (First In, First Out) principle. This means that the first element added to the queue is the first element removed.

A practical example is a line of people waiting to receive service at a bank. The person who arrives first is served first.

### 2. Programming Language

- Python 3

### 3. Queue Operations Implemented

The program supports the following operations:

| Operation | Description |
|---|---|
| Enqueue | Adds a new element to the rear of the queue. |
| Dequeue | Removes an element from the front of the queue. |
| Front | Displays the first element in the queue. |
| Rear | Displays the last element in the queue. |
| Display | Displays all elements from front to rear. |
| IsEmpty | Checks whether the queue contains any elements. |
| IsFull | Checks whether the queue has reached its maximum capacity. |

### 4. Queue Configuration

The program implements a Circular Queue using a fixed-size Python list.

```python
MAX_SIZE = 5
queue = [None] * MAX_SIZE

front = -1
rear = -1
```

A circular queue allows previously occupied positions to be reused after elements have been removed.

This implementation uses modular arithmetic to manage the circular movement of the front and rear positions.

### 5. How to Run the Program

**Prerequisites:**

- Python 3 installed on your computer.
- A terminal, Command Prompt, VS Code, or PyCharm.

**Step 1: Open the project folder**

Navigate to the `CSC-301-Data-Structures-Assignment` project directory.

**Step 2: Open the terminal**

Open a terminal in the main project directory.

**Step 3: Execute the program**

Run:

```bash
python 03_Queue_Implementation/queue.py
```

Alternatively, on Windows:

```bash
py 03_Queue_Implementation/queue.py
```

### 6. How to Test the Program

When executed, the program displays the following menu:

```text
========== QUEUE IMPLEMENTATION ==========

1. Enqueue
2. Dequeue
3. View Front
4. View Rear
5. Display Queue
6. Check if Empty
7. Check if Full
8. Exit

Enter your choice:
```

The following test cases demonstrate how the queue operates.

**Test 1: Enqueue Elements**

Input:

```text
1
10
1
20
1
30
```

Expected Output:

```text
10 added to the queue.
20 added to the queue.
30 added to the queue.
```

The queue now contains:

```text
FRONT -> 10 -> 20 -> 30 <- REAR
```

**Test 2: Display Queue**

Input:

```text
5
```

Expected Output:

```text
Queue Elements (Front to Rear):
10
20
30
```

**Test 3: View Front Element**

Input:

```text
3
```

Expected Output:

```text
Front element: 10
```

**Test 4: View Rear Element**

Input:

```text
4
```

Expected Output:

```text
Rear element: 30
```

**Test 5: Dequeue an Element**

Input:

```text
2
```

Expected Output:

```text
Removed element: 10
```

The queue now contains:

```text
FRONT -> 20 -> 30 <- REAR
```

**Test 6: Check if the Queue is Empty**

Input:

```text
6
```

Expected Output:

```text
The queue is not empty.
```

**Test 7: Check if the Queue is Full**

Input:

```text
7
```

Expected Output:

```text
The queue is not full.
```

### 7. Error Handling

The program handles the following special conditions:

**Queue Overflow:** Occurs when an attempt is made to insert an element into a full queue.

**Queue Underflow:** Occurs when an attempt is made to remove an element from an empty queue.

To test these conditions:

- Enqueue six elements to test Queue Overflow.
- Dequeue all elements and attempt another Dequeue operation to test Queue Underflow.

### 8. Learning Objectives

This implementation demonstrates an understanding of:

- Queue data structure.
- FIFO principle.
- Enqueue and Dequeue operations.
- Front and Rear pointers.
- Circular Queue implementation.
- Modular arithmetic.
- Queue Overflow and Underflow.

### 9. Project File

`queue.py` – Contains the complete Python implementation of the Circular Queue data structure.

---

**Course:** CSC 301 – Data Structures  
**Assignment:** Queue Implementation  
**Language:** Python 3