# Array Class Documentation

This guide will help you understand how to use the `Array<>` class, which is a beginner-friendly alternative to the standard C++ vector. The `Array<>` class provides helpful error messages and safety features to make working with collections of data easier for new programmers.

## Introduction to Arrays

An array is a collection of elements of the same type. Think of it like a numbered list or a row of storage boxes, where each item has its own position (index). Arrays are useful when you need to store multiple related values.

For example, you might use an array to store:
- A list of student grades
- Coordinates for a game
- A collection of names
- Daily temperatures for a week

## Creating Arrays

To use the `Array<>` class, you first need to include the appropriate header file:

```cpp
#include "array.h"
```

Then, you can create arrays in several ways:

### Empty Array

```cpp
// Create an empty array of integers
Array<int> numbers;
```

### Array with Initial Values

```cpp
// Create an array with some initial values
Array<int> scores = {95, 88, 76, 92, 85};

// Create an array of strings
Array<string> names = {"Alice", "Bob", "Charlie"};
```

## Basic Array Operations

### Accessing Elements with `operator[]`

You can access individual elements in an array using square brackets `[]` with the index of the element you want. **Remember: Array indices start at 0, not 1!**

```cpp
Array<int> scores = {95, 88, 76, 92, 85};

// Access the first element (index 0)
int firstScore = scores[0];  // 95

// Access the third element (index 2)
int thirdScore = scores[2];  // 76

// Change the value of an element
scores[1] = 90;  // Changes 88 to 90
```

If you try to access an index that doesn't exist (like `scores[10]` in an array with only 5 elements), the Array class will throw an error with a helpful message rather than allowing your program to crash mysteriously.

### Adding Elements with `append`

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

### Removing Elements with `removeAtIndex`

To remove an element at a specific position, use `removeAtIndex`:

```cpp
Array<string> colors = {"red", "green", "blue", "yellow"};

// Remove the element at index 1 (green)
colors.removeAtIndex(1);

// colors now contains: {"red", "blue", "yellow"}
```

### Inserting Elements with `insertAtIndex`

To add an element at a specific position, use `insertAtIndex`:

```cpp
Array<string> weekdays = {"Monday", "Wednesday", "Thursday"};

// Insert "Tuesday" at index 1 (between Monday and Wednesday)
weekdays.insertAtIndex(1, "Tuesday");

// weekdays now contains: {"Monday", "Tuesday", "Wednesday", "Thursday"}
```

### Getting the Size of an Array

The `size` method returns the number of elements in the array:

```cpp
Array<double> prices = {9.99, 15.50, 3.75, 20.00};

// Get the number of elements
int count = prices.size();  // 4

println("There are", count, "prices in the array.");
```

### Changing the Size with `resize`

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

### Clearing an Array with `clear`

To remove all elements from an array, use the `clear` method:

```cpp
Array<int> scores = {95, 88, 76, 92, 85};

// Remove all elements
scores.clear();

// scores is now empty, and scores.size() returns 0
```

## Working with Arrays in Loops

Loops are especially useful for working with arrays. Here are common patterns:

### Processing Each Element with a For Loop

```cpp
Array<int> scores = {95, 88, 76, 92, 85};
int sum = 0;

// Calculate the sum of all scores
for (int i = 0; i < scores.size(); i++) {
    sum += scores[i];
}

double average = static_cast<double>(sum) / scores.size();
println("Average score:", average);
```

### Finding Values in an Array

```cpp
Array<string> names = {"Alice", "Bob", "Charlie", "David"};
string searchName = "Charlie";
bool found = false;

for (int i = 0; i < names.size(); i++) {
    if (names[i] == searchName) {
        println("Found", searchName, "at position", i);
        found = true;
        break;  // Exit the loop once we've found what we're looking for
    }
}

if (!found) {
    println(searchName, "is not in the list.");
}
```

### Modifying All Elements

```cpp
Array<int> prices = {100, 200, 300, 400};

// Apply a 10% discount to all prices
for (int i = 0; i < prices.size(); i++) {
    prices[i] = prices[i] * 0.9;  // Reduce each price by 10%
}

// Print the discounted prices
println("Discounted prices:");
for (int i = 0; i < prices.size(); i++) {
    println("Item", i, ":", prices[i]);
}
```

### Filtering Elements into a New Array

```cpp
Array<int> numbers = {15, 8, 42, 3, 29, 14, 7};
Array<int> evenNumbers;

// Create a new array with only the even numbers
for (int i = 0; i < numbers.size(); i++) {
    if (numbers[i] % 2 == 0) {  // Check if the number is even
        evenNumbers.append(numbers[i]);
    }
}

// Print the even numbers
println("Even numbers:");
for (int i = 0; i < evenNumbers.size(); i++) {
    println(evenNumbers[i]);
}
```

## Common Array Patterns

### Counting Occurrences

```cpp
Array<int> values = {4, 2, 7, 4, 8, 4, 1, 9, 4};
int count = 0;

// Count how many times 4 appears
for (int i = 0; i < values.size(); i++) {
    if (values[i] == 4) {
        count++;
    }
}

println("The value 4 appears", count, "times.");
```

### Finding the Maximum Value

```cpp
Array<int> temperatures = {72, 68, 73, 85, 79, 68};
int maxTemp = temperatures[0];  // Start with the first element

for (int i = 1; i < temperatures.size(); i++) {
    if (temperatures[i] > maxTemp) {
        maxTemp = temperatures[i];
    }
}

println("The highest temperature is", maxTemp);
```

### Reversing an Array

```cpp
Array<int> original = {1, 2, 3, 4, 5};
Array<int> reversed;

// Add elements in reverse order
for (int i = original.size() - 1; i >= 0; i--) {
    reversed.append(original[i]);
}

println("Original array:", original);
println("Reversed array:", reversed);
```

## Error Handling

One of the key benefits of the `Array<>` class is safety. If you try to access an element that doesn't exist, you'll get a helpful error message instead of a crash:

```cpp
Array<int> numbers = {10, 20, 30};

// This will throw an error with a message like:
// "Error: ArrayBase index 5 out of range (0, 2)"
int value = numbers[5];
```

Similarly, attempting to use `removeAtIndex` or `insertAtIndex` with invalid indices will produce helpful error messages.

## Conclusion

The `Array<>` class provides an easy and safe way to work with collections of data. As you become more comfortable with arrays, you'll find them essential for solving many programming problems.

Remember these key points:
1. Arrays store multiple values of the same type
2. Array indices start at 0
3. The `size()` method tells you how many elements are in the array
4. For loops are commonly used with arrays to process multiple elements
5. The `Array<>` class provides helpful error messages if you make a mistake

Happy coding!
