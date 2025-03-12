---
layout: default
title: Modifying Arrays
parent: Array Class
nav_order: 3
---

# Modifying Arrays

The Array class provides several methods for adding, removing, and changing elements.

## Adding Elements with `append`

The `append` method adds a new element to the end of the array:

```cpp
Array<string> fruits = {"apple", "banana"};

// Add a new element to the end
fruits.append("orange");  

// fruits now contains: {"apple", "banana", "orange"}
```

You can also use the alias `push_back` which does the same thing as `append`:

```cpp
fruits.push_back("grape");  // Same as append

// fruits now contains: {"apple", "banana", "orange", "grape"}
```

## Removing Elements with `removeAtIndex`

To remove an element at a specific position, use `removeAtIndex`:

```cpp
Array<string> colors = {"red", "green", "blue", "yellow"};

// Remove the element at index 1 (green)
colors.removeAtIndex(1);

// colors now contains: {"red", "blue", "yellow"}
```

When you remove an element, all elements after it will shift to fill the gap.

## Inserting Elements with `insertAtIndex`

To add an element at a specific position, use `insertAtIndex`:

```cpp
Array<string> weekdays = {"Monday", "Wednesday", "Thursday"};

// Insert "Tuesday" at index 1 (between Monday and Wednesday)
weekdays.insertAtIndex(1, "Tuesday");

// weekdays now contains: {"Monday", "Tuesday", "Wednesday", "Thursday"}
```

When you insert an element, all elements at or after that position will be shifted to make room.

## Changing the Size with `resize`

You can change the size of an array using the `resize` method:

```cpp
Array<int> numbers = {1, 2, 3};

// Resize to a larger size (new elements are initialized to 0)
numbers.resize(5);
// numbers now contains: {1, 2, 3, 0, 0}

// You can specify the value for new elements
Array<string> names = {"Alice", "Bob"};
names.resize(4, "Unknown");
// names now contains: {"Alice", "Bob", "Unknown", "Unknown"}

// Resize to a smaller size (extra elements are removed)
numbers.resize(2);
// numbers now contains: {1, 2}
```

## Clearing an Array with `clear`

To remove all elements from an array, use the `clear` method:

```cpp
Array<int> scores = {95, 88, 76, 92, 85};

// Remove all elements
scores.clear();

// scores is now empty, and scores.size() returns 0
```

## Getting the Size of an Array

The `size` method returns the number of elements in the array:

```cpp
Array<double> prices = {9.99, 15.50, 3.75, 20.00};

// Get the number of elements
int count = prices.size();  // 4

println("There are", count, "prices in the array.");
```

## Checking if an Array is Empty

You can check if an array has no elements using the `empty` method:

```cpp
Array<int> numbers;

if (numbers.empty()) {
    println("The array is empty!");
}

numbers.append(42);

if (!numbers.empty()) {
    println("The array now has elements!");
}
```
