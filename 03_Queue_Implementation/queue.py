
# CSC 301 - Data Structures Assignment
# Program: Queue Implementation
# Principle: FIFO (First In, First Out)


MAX_SIZE = 5

queue = [None] * MAX_SIZE

front = -1
rear = -1


# Function to add an element
def enqueue():
    global front, rear

    if (rear + 1) % MAX_SIZE == front:
        print("Queue Overflow! The queue is full.")

    else:
        value = int(input("Enter the value to enqueue: "))

        if front == -1:
            front = 0

        rear = (rear + 1) % MAX_SIZE

        queue[rear] = value

        print(f"{value} added to the queue.")


# Function to remove an element
def dequeue():
    global front, rear

    if front == -1:
        print("Queue Underflow! The queue is empty.")

    else:
        removed = queue[front]

        print(f"Removed element: {removed}")

        if front == rear:
            front = -1
            rear = -1

        else:
            front = (front + 1) % MAX_SIZE


# Function to view the front element
def view_front():
    if front == -1:
        print("Queue is empty.")
    else:
        print("Front element:", queue[front])


# Function to view the rear element
def view_rear():
    if rear == -1:
        print("Queue is empty.")
    else:
        print("Rear element:", queue[rear])


# Function to display queue elements
def display():
    if front == -1:
        print("Queue is empty.")

    else:
        print("\nQueue Elements (Front to Rear):")

        index = front

        while True:
            print(queue[index])

            if index == rear:
                break

            index = (index + 1) % MAX_SIZE


# Function to check if queue is empty
def is_empty():
    if front == -1:
        print("The queue is empty.")
    else:
        print("The queue is not empty.")


# Function to check if queue is full
def is_full():
    if (rear + 1) % MAX_SIZE == front:
        print("The queue is full.")
    else:
        print("The queue is not full.")


# Main program
while True:

    print("\n========== QUEUE IMPLEMENTATION ==========")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. View Front")
    print("4. View Rear")
    print("5. Display Queue")
    print("6. Check if Empty")
    print("7. Check if Full")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        enqueue()

    elif choice == "2":
        dequeue()

    elif choice == "3":
        view_front()

    elif choice == "4":
        view_rear()

    elif choice == "5":
        display()

    elif choice == "6":
        is_empty()

    elif choice == "7":
        is_full()

    elif choice == "8":
        print("Exiting Queue Program.")
        break

    else:
        print("Invalid choice! Please try again.")
