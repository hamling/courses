---
layout: default
title: Creating Arrays
parent: Array Class
nav_order: 1
---

# Creating Arrays

An array is a collection of elements of the same type. Think of it like a numbered list or a row of storage boxes, where each item has its own position (index). Arrays are useful when you need to store multiple related values.

## Common Uses for Arrays

Arrays are perfect for storing:
- A list of student grades
- Coordinates for a game
- A collection of names
- Daily temperatures for a week

## Creating an Empty Array

To create an empty array, specify the type of elements it will contain:

```cpp
// Create an empty array of integers
Array<int> numbers;

// Create an empty array of strings
Array<string> names;

// Create an empty array of floating-point numbers
Array<double> prices;
```

## Creating an Array with Initial Values

You can create an array with values already in it using curly braces:

```cpp
// Create an array with some initial integer values
Array<int> scores = {95, 88, 76, 92, 85};

// Create an array of strings
Array<string> names = {"Alice", "Bob", "Charlie"};

// Create an array of doubles
Array<double> prices = {9.99, 14.50, 3.75};
```

## Choosing the Right Type

The type inside the angle brackets `<>` determines what kind of elements your array can hold:

- `Array<int>` can hold whole numbers (like 1, 42, -7)
- `Array<double>` can hold decimal numbers (like 3.14, -2.5)
- `Array<string>` can hold text
- `Array<bool>` can hold true/false values
- `Array<char>` can hold single characters

Remember that all elements in an array must be of the same type.
