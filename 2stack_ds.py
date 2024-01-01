# 2. WAP to create a class representing a stack data structure. 
# Include methods for pushing and popping elements.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop.")

    def is_empty(self):
        return len(self.items) == 0

stack = Stack()

while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        item = input("Enter the element to push: ")
        stack.push(item)
        print(f"{item} pushed onto the stack.")

    elif choice == '2':
        popped_item = stack.pop()
        if popped_item is not None:
            print(f"Popped element: {popped_item}")

    elif choice == '3':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
