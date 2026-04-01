from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Element:
    key: str
    value: int


@dataclass
class Dictionary:
    size: int
    data: list[list[Element]] = field(init=False)

    def __post_init__(self):
        """Initialize the bucket array after creation."""
        self.data = [[] for _ in range(self.size)]

    def _calculate_hash(self, key: str) -> int:
        """Calculate the hash of a key."""
        return hash(key) % self.size

    def __setitem__(self, key: str, value: int):
        """Allow using dictionary[key] = value."""
        key_hash = self._calculate_hash(key)

        # Search if the key already exists
        for element in self.data[key_hash]:
            if element.key == key:
                element.value = value
                return

        # Otherwise, add a new element
        self.data[key_hash].append(Element(key, value))

    def __getitem__(self, key: str) -> int:
        """Allow using dictionary[key]."""
        key_hash = self._calculate_hash(key)

        for element in self.data[key_hash]:
            if element.key == key:
                return element.value

        raise KeyError(f"Key '{key}' not found")

    def __contains__(self, key: str) -> bool:
        """Allow using 'key in dictionary'."""
        key_hash = self._calculate_hash(key)

        for element in self.data[key_hash]:
            if element.key == key:
                return True

        return False

    def __len__(self) -> int:
        """Allow using len(dictionary)."""
        total_count = 0
        for bucket in self.data:
            total_count += len(bucket)
        return total_count

    def __iter__(self):
        """Allow iterating over keys: for key in dictionary."""
        for bucket in self.data:
            for element in bucket:
                yield element.key

    def __str__(self) -> str:
        """Allow using print(dictionary) - human-readable representation."""
        item_strings = []
        for bucket in self.data:
            for element in bucket:
                item_strings.append(f"'{element.key}': {element.value}")

        return "{" + ", ".join(item_strings) + "}"

    def items(self):
        """Return an iterator over (key, value) pairs."""
        for bucket in self.data:
            for element in bucket:
                yield (element.key, element.value)

    def get(self, key: str, default: int | None = None) -> int | None:
        """Get a value with a default if the key doesn't exist."""
        try:
            return self[key]
        except KeyError:
            return default


if __name__ == "__main__":
    print("=== CREATION AND INSERTION ===")
    frequency = Dictionary(size=4)

    # Using [] notation
    frequency["a"] = 1
    frequency["b"] = 2
    frequency["c"] = 3
    frequency["d"] = 4
    frequency["e"] = 5

    # Display with print()
    print(frequency)

    print("\n=== UPDATE ===")
    frequency["a"] = 42
    print(frequency)

    print("\n=== VALUE ACCESS ===")
    print(f"Value for 'a': {frequency['a']}")
    print(f"Value for 'b': {frequency['b']}")

    print("\n=== IN OPERATOR ===")
    print(f"'a' in frequency: {'a' in frequency}")
    print(f"'z' in frequency: {'z' in frequency}")

    print("\n=== LENGTH ===")
    print(f"len(frequency): {len(frequency)}")

    print("\n=== ITEMS METHOD ===")
    for key, value in frequency.items():
        print(f"{key}: {value}")
