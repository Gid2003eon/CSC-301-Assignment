
# CSC 301 - Data Structures Assignment
# Program: Stack Implementation
# Principle: LIFO (Last In, First Out)


MAX_SIZE = 5

stack = []


# Function to add an element to the stack
def push():
    if len(stack) == MAX_SIZE:
        print("Stack Overflow! The stack is full.")
    else:
        value = int(input("Enter the value to push: "))
        stack.append(value)
        print(f"{value} pushed into the stack.")


# Function to remove the top element
def pop():
    if len(stack) == 0:
        print("Stack Underflow! The stack is empty.")
    else:
        removed = stack.pop()
        print(f"Removed element: {removed}")


# Function to view the top element
def peek():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Top element:", stack[-1])


# Function to display stack elements
def display():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("\nStack Elements (Top to Bottom):")

        for element in reversed(stack):
            print(element)


# Function to check if stack is empty
def is_empty():
    if len(stack) == 0:
        print("The stack is empty.")
    else:
        print("The stack is not empty.")


# Function to check if stack is full
def is_full():
    if len(stack) == MAX_SIZE:
        print("The stack is full.")
    else:
        print("The stack is not full.")


# Main program
while True:

    print("\n========== STACK IMPLEMENTATION ==========")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display Stack")
    print("5. Check if Empty")
    print("6. Check if Full")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        push()

    elif choice == "2":
        pop()

    elif choice == "3":
        peek()

    elif choice == "4":
        display()

    elif choice == "5":
        is_empty()

    elif choice == "6":
        is_full()

    elif choice == "7":
        print("Exiting Stack Program.")
        break

    else:
        print("Invalid choice! Please try again.")
