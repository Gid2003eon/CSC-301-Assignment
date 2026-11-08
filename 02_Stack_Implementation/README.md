# STACK IMPLEMENTATION USING PYTHON

## CSC 301 – Data Structures Assignment

### 1. Introduction

This project demonstrates the implementation of a Stack data structure using Python.

A stack is a linear data structure that follows the LIFO (Last In, First Out) principle. This means that the last element added to the stack is the first element removed.

A common example is a stack of plates, where the last plate placed on top is the first one removed.

### 2. Programming Language

- Python 3

### 3. Stack Operations Implemented

The program supports the following operations:

| Operation | Description |
|---|---|
| Push | Adds a new element to the top of the stack. |
| Pop | Removes the top element from the stack. |
| Peek | Displays the top element without removing it. |
| Display | Displays all elements in the stack from top to bottom. |
| IsEmpty | Checks whether the stack contains any elements. |
| IsFull | Checks whether the stack has reached its maximum capacity. |

### 4. Stack Configuration

The stack is implemented using a Python list with a maximum capacity of five elements.

```python
MAX_SIZE = 5
stack = []
```

This allows the program to demonstrate stack overflow and stack underflow conditions.

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
python 02_Stack_Implementation/stack.py
```

Alternatively, on Windows:

```bash
py 02_Stack_Implementation/stack.py
```

### 6. How to Test the Program

When executed, the program displays the following menu:

```text
========== STACK IMPLEMENTATION ==========

1. Push
2. Pop
3. Peek
4. Display Stack
5. Check if Empty
6. Check if Full
7. Exit

Enter your choice:
```

The following test cases demonstrate how the stack operates.

**Test 1: Push Elements**

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
10 pushed into the stack.
20 pushed into the stack.
30 pushed into the stack.
```

The stack now contains:

```text
TOP -> 30
       20
       10
```

**Test 2: Display Stack**

Input:

```text
4
```

Expected Output:

```text
Stack Elements (Top to Bottom):
30
20
10
```

**Test 3: Peek at the Top Element**

Input:

```text
3
```

Expected Output:

```text
Top element: 30
```

The element remains in the stack.

**Test 4: Pop an Element**

Input:

```text
2
```

Expected Output:

```text
Removed element: 30
```

The stack now contains:

```text
TOP -> 20
       10
```

**Test 5: Check if the Stack is Empty**

Input:

```text
5
```

Expected Output:

```text
The stack is not empty.
```

**Test 6: Check if the Stack is Full**

Input:

```text
6
```

Expected Output:

```text
The stack is not full.
```

### 7. Error Handling

The program handles the following special conditions:

**Stack Overflow:** Occurs when an attempt is made to insert an element into a full stack.

**Stack Underflow:** Occurs when an attempt is made to remove an element from an empty stack.

To test these conditions:

- Push six elements into the stack to test Stack Overflow.
- Remove all elements and attempt another Pop operation to test Stack Underflow.

### 8. Learning Objectives

This implementation demonstrates an understanding of:

- Stack data structure.
- LIFO principle.
- Push and Pop operations.
- Peek operation.
- Stack traversal.
- Stack Overflow and Underflow.
- Python lists and functions.

### 9. Project File

`stack.py` – Contains the complete Python implementation of the Stack data structure.

---

**Course:** CSC 301 – Data Structures  
**Assignment:** Stack Implementation  
**Language:** Python 3