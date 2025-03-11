---
title: Custom Array<> Class
---

# Array<> Class Documentation

Our custom `Array<>` class provides a safer alternative to raw arrays and simpler interface than `std::vector` for beginners.

## Features

- Bounds checking with descriptive error messages
- Simple, consistent interface
- Modern C++ integration
- Compatible with range-based for loops

## Basic Usage

```cpp
#include "Array.h"

int main() {
    // Create an array of integers with size 5
    Array<int> numbers(5);
    
    // Set values
    numbers[0] = 10;
    numbers[1] = 20;
    
    // Get values
    int first = numbers[0];  // 10
    
    // Iteration
    for (int num : numbers) {
        println(num);
    }
    
    return 0;
}
```

## Methods

| Method | Description |
|--------|-------------|
| `Array<T>(int size)` | Constructor with specified size |
| `size()` | Returns the number of elements |
| `operator[]` | Access or modify elements with bounds checking |
| `begin()`, `end()` | Iterator support for range-based for loops |
