# CSC 301 - Data Structures Assignment
# Program: Array Operations
# Operations: Insert, Delete, Search, Sort and Display


# Initial array
numbers = [45, 12, 78, 23, 56]


# Function to display array elements
def display_array():
    print("\nCurrent Array:", numbers)


# Function to insert an element
def insert_element():
    value = int(input("Enter the value to insert: "))
    position = int(input("Enter the position (starting from 0): "))

    if 0 <= position <= len(numbers):
        numbers.insert(position, value)
        print("Element inserted successfully.")
    else:
        print("Invalid position!")


# Function to delete an element
def delete_element():
    value = int(input("Enter the value to delete: "))

    if value in numbers:
        numbers.remove(value)
        print("Element deleted successfully.")
    else:
        print("Element not found!")


# Function to search for an element
def search_element():
    value = int(input("Enter the value to search for: "))

    for index in range(len(numbers)):
        if numbers[index] == value:
            print(f"Element {value} found at index {index}.")
            return

    print("Element not found!")


# Function to sort the array using Bubble Sort
def sort_array():
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print("Array sorted successfully.")


# Main program
while True:

    print("\n========== ARRAY OPERATIONS ==========")
    print("1. Display Array")
    print("2. Insert Element")
    print("3. Delete Element")
    print("4. Search Element")
    print("5. Sort Array")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_array()

    elif choice == "2":
        insert_element()

    elif choice == "3":
        delete_element()

    elif choice == "4":
        search_element()

    elif choice == "5":
        sort_array()

    elif choice == "6":
        print("Exiting Array Operations Program.")
        break

    else:
        print("Invalid choice! Please try again.")
