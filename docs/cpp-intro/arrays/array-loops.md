---
layout: default
title: Using Loops with Arrays
parent: Array Class
nav_order: 4
---

# Using Loops with Arrays

Loops are especially useful for working with arrays, allowing you to process many elements with just a few lines of code. This page shows common patterns for using loops with arrays.

## Processing Each Element

The most common pattern is to use a for loop to process each element:

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

## Finding Values in an Array

You can use a loop to search for specific values:

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

## Modifying All Elements

Loops make it easy to apply the same operation to every element:

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

## Filtering Elements into a New Array

You can create a new array containing only elements that match certain criteria:

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

## Counting Occurrences

You can count how many times a specific value appears:

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

## Finding the Maximum Value

You can find the largest value in an array:

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

## Reversing an Array

You can create a new array with elements in reverse order:

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
