# ARRAY OPERATIONS USING PYTHON

## CSC 301 – Data Structures Assignment

### 1. Introduction

This project demonstrates the implementation of fundamental array operations using Python. An array is a data structure used to store multiple elements in an organised manner, where each element can be accessed through its index.

The program allows users to perform different operations on an array through an interactive, menu-driven interface.

### 2. Programming Language

- Python 3

### 3. Operations Implemented

The following array operations have been implemented:

| Operation | Description |
|---|---|
| Display | Displays all elements currently stored in the array. |
| Insert | Adds a new element at a specified position. |
| Delete | Removes a specified element from the array. |
| Search | Searches for an element and returns its index if found. |
| Sort | Arranges array elements in ascending order using Bubble Sort. |

### 4. Initial Array

The program begins with the following array:

```python
numbers = [45, 12, 78, 23, 56]
```

Users can modify the array by performing the available operations.

### 5. How to Run the Program

**Prerequisites:**

- Python 3 must be installed on your computer.
- A terminal, Command Prompt, VS Code, or PyCharm.

**Step 1: Open the project folder**

Navigate to the `CSC-301-Data-Structures-Assignment` project directory.

**Step 2: Open the terminal**

Open a terminal in the main project directory.

**Step 3: Execute the program**

Run the following command:

```bash
python 01_Array_Operations/array_operations.py
```

Alternatively, on Windows, use:

```bash
py 01_Array_Operations/array_operations.py
```

### 6. How to Test the Program

When the program starts, the following menu is displayed:

```text
========== ARRAY OPERATIONS ==========

1. Display Array
2. Insert Element
3. Delete Element
4. Search Element
5. Sort Array
6. Exit

Enter your choice:
```

The following test cases can be used to verify the program.

**Test 1: Display Array**

Input:

```text
1
```

Expected Output:

```text
Current Array: [45, 12, 78, 23, 56]
```

**Test 2: Search for an Element**

Input:

```text
4
78
```

Expected Output:

```text
Element 78 found at index 2.
```

**Test 3: Insert an Element**

Input:

```text
2
99
2
```

Expected Output:

```text
Element inserted successfully.
```

The array becomes:

```text
[45, 12, 99, 78, 23, 56]
```

**Test 4: Sort the Array**

Input:

```text
5
```

Expected Output:

```text
Array sorted successfully.
```

The sorted array becomes:

```text
[12, 23, 45, 56, 78, 99]
```

**Test 5: Delete an Element**

Input:

```text
3
45
```

Expected Output:

```text
Element deleted successfully.
```

The array becomes:

```text
[12, 23, 56, 78, 99]
```

### 7. Error Handling

The program also handles invalid operations, including:

- Searching for an element that does not exist.
- Deleting an element that is not present.
- Inserting an element at an invalid position.
- Entering an invalid menu option.

### 8. Learning Objectives

This implementation demonstrates an understanding of:

- Array creation and indexing.
- Array traversal.
- Insertion and deletion.
- Linear searching.
- Bubble Sort algorithm.
- Python functions and conditional statements.

### 9. Project File

`array_operations.py` – Contains the complete Python implementation of the array operations.

---

**Course:** CSC 301 – Data Structures  
**Assignment:** Array Operations  
**Language:** Python 3