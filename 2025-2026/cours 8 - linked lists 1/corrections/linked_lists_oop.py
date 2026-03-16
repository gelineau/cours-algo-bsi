from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LinkedList:
    value: int
    next: LinkedList | None = None

    def get_last_element(self) -> int:
        """Return the value of the last element in the list."""
        current = self
        while current.next is not None:
            current = current.next
        return current.value

    def get_last_element_recursive(self) -> int:
        """Recursively return the value of the last element."""
        if self.next is None:
            return self.value
        return self.next.get_last_element_recursive()

    def get_element_by_index(self, index: int) -> int:
        """Return the element at the specified index (iterative)."""
        current = self
        for _ in range(index):
            if current.next is None:
                raise IndexError("linked list is not long enough")
            current = current.next
        return current.value

    def get_element_by_index_rec(self, index: int) -> int:
        """Return the element at the specified index (recursive)."""
        if index == 0:
            return self.value
        if self.next is None:
            raise IndexError("linked list is not long enough")
        return self.next.get_element_by_index_rec(index - 1)

    def append(self, value: int):
        """Append a new element at the end (iterative)."""
        current = self
        while current.next is not None:
            current = current.next
        current.next = LinkedList(value)

    def append_recursive(self, value: int):
        """Append a new element at the end (recursive)."""
        if self.next is None:
            self.next = LinkedList(value)
        else:
            self.next.append_recursive(value)

    def sum_recursive(self) -> int:
        """Calculate the sum of all elements recursively."""
        if self.next is None:
            return self.value
        return self.value + self.next.sum_recursive()

    def sum(self) -> int:
        """Calculate the sum of all elements iteratively."""
        total = 0
        current = self
        while current is not None:
            total += current.value
            current = current.next
        return total

    def find_recursive(self, value: int) -> bool:
        """Recursively search for a value."""
        if self.value == value:
            return True
        if self.next is None:
            return False
        return self.next.find_recursive(value)

    def find(self, value: int) -> bool:
        """Iteratively search for a value."""
        current = self
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def replace(self, value1: int, value2: int):
        """Replace all occurrences of value1 with value2 (iterative)."""
        current = self
        while current is not None:
            if current.value == value1:
                current.value = value2
            current = current.next

    def replace_recursive(self, value1: int, value2: int):
        """Replace all occurrences of value1 with value2 (recursive)."""
        if self.value == value1:
            self.value = value2
        if self.next is not None:
            self.next.replace_recursive(value1, value2)

    def clone(self) -> LinkedList:
        """Create a shallow copy of the list (iterative)."""
        cloned_list = LinkedList(self.value)
        current_new = cloned_list
        current_old = self.next
        while current_old is not None:
            current_new.next = LinkedList(current_old.value)
            current_old = current_old.next
            current_new = current_new.next
        return cloned_list

    def clone_recursive(self) -> LinkedList:
        """Create a shallow copy of the list (recursive)."""
        if self.next is None:
            return LinkedList(self.value)
        return LinkedList(self.value, self.next.clone_recursive())

    def remove_recursive(self, value: int) -> LinkedList | None:
        """Remove all nodes with the specified value (recursive)."""
        if self.value == value:
            return self.next
        new_next = self.next.remove_recursive(value) if self.next is not None else None
        return LinkedList(self.value, new_next)

    def linked_list_to_string(self) -> str:
        """Convert list to string (iterative)."""
        elements = []
        current = self
        while current is not None:
            elements.append(str(current.value))
            current = current.next
        return " -> ".join(elements)

    def linked_list_to_string_recursive(self) -> str:
        """Convert list to string (recursive)."""
        if self.next is None:
            return str(self.value)
        return str(self.value) + " -> " + self.next.linked_list_to_string_recursive()

    def extend(self, other: LinkedList):
        """Extend list by appending another list (iterative)."""
        current = self
        while current.next is not None:
            current = current.next
        current.next = other

    def extend_recursive(self, other: LinkedList):
        """Extend list by appending another list (recursive)."""
        if self.next is None:
            self.next = other
        else:
            self.next.extend_recursive(other)

    def get_size(self) -> int:
        """Get size of list (iterative)."""
        count = 1
        current = self
        while current.next is not None:
            current = current.next
            count += 1
        return count

    def get_size_recursive(self) -> int:
        """Get size of list (recursive)."""
        if self.next is None:
            return 1
        return 1 + self.next.get_size_recursive()

    def extract_sublist(self, n: int) -> LinkedList | None:
        """Extract sublist starting from index n."""
        current = self
        for _ in range(n):
            if current.next is None:
                return None
            current = current.next
        return current

    def __len__(self) -> int:
        """Return the length of the list."""
        count = 1
        current = self
        while current.next is not None:
            current = current.next
            count += 1
        return count

    def __getitem__(self, index: int) -> int:
        """Get element by index using square brackets."""
        if index < 0:
            # Support negative indices
            index = len(self) + index
        return self.get_element_by_index(index)

    def __setitem__(self, index: int, value: int):
        """Set element by index using square brackets."""
        if index < 0:
            index = len(self) + index
        current = self
        for _ in range(index):
            if current.next is None:
                raise IndexError("list index out of range")
            current = current.next
        current.value = value

    def __add__(self, other: LinkedList) -> LinkedList:
        """Concatenate two lists."""
        # Clone self
        result = self.clone()
        # Extend with clone of other
        result.extend(other.clone())
        return result

    def __repr__(self) -> str:
        """String representation of the list."""
        return self.linked_list_to_string()


# Example usage:

# Create initial list
my_list = LinkedList(1, LinkedList(2, LinkedList(3, None)))
print(f"{my_list=}")
print(f"{my_list.get_last_element_recursive()=}, {my_list.get_last_element()=}")

# Access by index
print(f"{my_list.get_element_by_index(1)=}, {my_list.get_element_by_index(2)=}")
print(f"{my_list.get_element_by_index_rec(2)=}")

# Append elements
my_list.append(4)
my_list.append(5)
print(f"after append {my_list=}")

my_list.append_recursive(6)
print(f"after append_recursive {my_list=}")

# Sum of elements
print(f"{my_list.sum()=}, {my_list.sum_recursive()=}")

# Search for values
print(f"{my_list.find(2)=}, {my_list.find_recursive(2)=}")
print(f"{my_list.find(99)=}, {my_list.find_recursive(99)=}")

# Replace values
my_list.replace(2, 42)
print(f"{my_list=}")
my_list.replace_recursive(42, 99)
print(f"{my_list=}")

# Clone list
cloned_list = my_list.clone()
print(f"{cloned_list=}")
cloned_list.replace(99, 88)
print(f"{cloned_list=}")
print(f"{my_list=}")

# Remove elements
list_without_99 = my_list.remove_recursive(99)
print(f"{list_without_99=}")

# Convert to string
print(f"{my_list.linked_list_to_string()=}")
print(f"{my_list.linked_list_to_string_recursive()=}")

# Extend list
list_a = LinkedList(10, LinkedList(20, LinkedList(30, None)))
my_list.extend(list_a)
print(f"{my_list=}")

list_b = LinkedList(100, LinkedList(200, None))
my_list.extend_recursive(list_b)
print(f"{my_list=}")

# Get size
print(f"{my_list.get_size()=}")
print(f"{my_list.get_size_recursive()=}")

# Extract sublist
sublist = my_list.extract_sublist(5)
print(f"{sublist=}")


##############

# Create lists
list1 = LinkedList(1, LinkedList(2, LinkedList(3, None)))
list2 = LinkedList(4, LinkedList(5, None))

# Length
print(len(list1))  # Output: 3

# Indexing
print(list1[0])  # Output: 1
print(list1[2])  # Output: 3

# Setting value
list1[1] = 42
print(list1)

# Concatenation
list3 = list1 + list2
print(list3)

# Representation
print(repr(list3))
