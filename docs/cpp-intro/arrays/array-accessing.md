---
layout: default
title: Accessing Elements
parent: Array Class
nav_order: 2
---

# Accessing Elements

One of the most common operations is accessing individual elements of an array. The Array class provides safe and easy ways to work with the data it contains.

## Using the Square Bracket Operator `[]`

You can access individual elements in an array using square brackets `[]` with the index of the element you want.

**Important: Array indices start at 0, not 1!**

```cpp
Array<int> scores = {95, 88, 76, 92, 85};

// Access the first element (index 0)
int firstScore = scores[0];  // 95

// Access the third element (index 2)
int thirdScore = scores[2];  // 76
```

## Modifying Elements

You can change the value of an element using the same square bracket notation:

```cpp
Array<int> scores = {95, 88, 76, 92, 85};

// Change the value of the second element (index 1)
scores[1] = 90;  // Changes 88 to 90

// Add 5 points to the fourth element (index 3)
scores[3] = scores[3] + 5;  // Changes 92 to 97
```

## Safety Features

One of the key benefits of the `Array<>` class is safety. If you try to access an element that doesn't exist, you'll get a helpful error message instead of a crash:

```cpp
Array<int> numbers = {10, 20, 30};

// This will throw an error with a message like:
// "Error: ArrayBase index 5 out of range (0, 2)"
int value = numbers[5];
```

This helps you quickly identify and fix index errors that would cause mysterious crashes with other array implementations.

## First and Last Elements

You can access the first element with `front()` and the last element with `back()`:

```cpp
Array<string> names = {"Alice", "Bob", "Charlie"};

string first = names.front();  // "Alice"
string last = names.back();    // "Charlie"
```

Like with the square bracket operator, the `front()` and `back()` methods will throw helpful error messages if the array is empty.
