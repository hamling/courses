---
layout: default
title: Common Array Patterns
parent: Array Class
nav_order: 5
---

# Common Array Patterns

This page demonstrates common patterns and techniques for working with arrays that will help you solve many programming problems.

## Working with Multiple Arrays

Sometimes you need to use multiple arrays together:

```cpp
// Names and corresponding scores
Array<string> students = {"Alice", "Bob", "Charlie", "David"};
Array<int> scores = {92, 85, 78, 90};

// Find the student with the highest score
int highestIndex = 0;
for (int i = 1; i < scores.size(); i++) {
    if (scores[i] > scores[highestIndex]) {
        highestIndex = i;
    }
}

println("The student with the highest score is", students[highestIndex], 
        "with a score of", scores[highestIndex]);
```

## Building an Array Step by Step

Sometimes you need to build an array based on calculations:

```cpp
// Create an array of squares from 1 to 10
Array<int> squares;

for (int i = 1; i <= 10; i++) {
    squares.append(i * i);
}

// Print the squares
for (int i = 0; i < squares.size(); i++) {
    println(i+1, "squared =", squares[i]);
}
```

## Finding Elements that Match Criteria

When you need to locate elements based on conditions:

```cpp
Array<int> ages = {14, 7, 21, 16, 19, 8, 42, 17};
Array<int> adultIndices;

// Find indices of all adults (18 and older)
for (int i = 0; i < ages.size(); i++) {
    if (ages[i] >= 18) {
        adultIndices.append(i);
    }
}

println("Adult ages found at positions:");
for (int i = 0; i < adultIndices.size(); i++) {
    int index = adultIndices[i];
    println("Position", index, ":", ages[index]);
}
```

## Merging Arrays

You can combine multiple arrays:

```cpp
Array<string> list1 = {"apple", "banana", "cherry"};
Array<string> list2 = {"orange", "grape"};
Array<string> combined;

// Add all elements from the first list
for (int i = 0; i < list1.size(); i++) {
    combined.append(list1[i]);
}

// Add all elements from the second list
for (int i = 0; i < list2.size(); i++) {
    combined.append(list2[i]);
}

println("Combined list has", combined.size(), "elements");
```

## Checking if Arrays Are Equal

You can compare two arrays to see if they have the same elements:

```cpp
Array<int> array1 = {1, 2, 3, 4};
Array<int> array2 = {1, 2, 3, 4};
Array<int> array3 = {1, 2, 4, 3};

bool areEqual = true;

// First check if sizes match
if (array1.size() != array2.size()) {
    areEqual = false;
} else {
    // Then check each element
    for (int i = 0; i < array1.size(); i++) {
        if (array1[i] != array2[i]) {
            areEqual = false;
            break;
        }
    }
}

if (areEqual) {
    println("array1 and array2 are equal");
} else {
    println("array1 and array2 are NOT equal");
}
```

## Creating a Frequency Counter

Count how many times each value appears:

```cpp
Array<int> votes = {3, 1, 2, 3, 3, 1, 4, 2, 3, 2};
Array<int> candidates = {1, 2, 3, 4};
Array<int> counts = {0, 0, 0, 0};  // Initialize with zeros

// Count votes for each candidate
for (int i = 0; i < votes.size(); i++) {
    int candidate = votes[i];
    
    // Find the index of this candidate
    for (int j = 0; j < candidates.size(); j++) {
        if (candidates[j] == candidate) {
            counts[j]++;
            break;
        }
    }
}

// Display the results
for (int i = 0; i < candidates.size(); i++) {
    println("Candidate", candidates[i], "received", counts[i], "votes");
}
```

## Moving Elements Within an Array

Sometimes you need to rearrange elements:

```cpp
Array<string> queue = {"Alice", "Bob", "Charlie", "David"};

// Move the first person to the end of the queue
string firstPerson = queue[0];
queue.removeAtIndex(0);
queue.append(firstPerson);

println("After moving first person to the back:");
for (int i = 0; i < queue.size(); i++) {
    println(i, ":", queue[i]);
}
```
