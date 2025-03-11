#!/usr/bin/env python3
import os
import sys

def create_file(path, content):
    """Create a file with the given content, creating parent directories if needed."""
    # Create parent directories if they don't exist
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    with open(path, 'w') as f:
        f.write(content)
    print(f"Created: {path}")

def create_skeleton(base_dir):
    """Create the entire skeleton structure for the course documentation site."""
    # Ensure base directory exists
    os.makedirs(base_dir, exist_ok=True)
    
    # Main configuration file
    config_yml = """remote_theme: pages-themes/primer@v0.2.0
plugins:
- jekyll-remote-theme

title: "Computer Science Courses"
description: "Course materials for CS classes"

# Build settings
markdown: kramdown
highlighter: rouge

# Default layout
defaults:
  -
    scope:
      path: ""
    values:
      layout: "default"
"""
    create_file(os.path.join(base_dir, "_config.yml"), config_yml)
    
    # Main layout template
    default_layout = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ page.title | default: site.title }}</title>
  <link rel="stylesheet" href="{{ '/assets/css/style.css?v=' | append: site.github.build_revision | relative_url }}">
  <style>
    .sidebar {
      width: 250px;
      position: fixed;
      height: 100%;
      padding: 20px;
      background-color: #f5f5f5;
    }
    .content {
      margin-left: 270px;
      padding: 20px;
    }
    @media (max-width: 768px) {
      .sidebar {
        position: relative;
        width: 100%;
        height: auto;
      }
      .content {
        margin-left: 0;
      }
    }
  </style>
</head>
<body>
  <div class="sidebar">
    {% include navigation.html %}
  </div>
  
  <div class="content">
    <header>
      <h1>{{ page.title | default: site.title }}</h1>
    </header>
    
    <main>
      {{ content }}
    </main>
    
    <footer>
      {% include footer.html %}
    </footer>
  </div>
</body>
</html>
"""
    create_file(os.path.join(base_dir, "_layouts/default.html"), default_layout)
    
    # Navigation include
    navigation_html = """<nav>
  <h2>Courses</h2>
  <ul>
    <li><a href="{{ site.baseurl }}/">Home</a></li>
    <li>
      <a href="{{ site.baseurl }}/cpp-intro/">Intro to C++</a>
      {% if page.url contains '/cpp-intro/' %}
      <ul>
        <li><a href="{{ site.baseurl }}/cpp-intro/setup/">Setup</a></li>
        <li><a href="{{ site.baseurl }}/cpp-intro/fundamentals/">Fundamentals</a></li>
        <li><a href="{{ site.baseurl }}/cpp-intro/arrays/">Arrays</a></li>
        <li><a href="{{ site.baseurl }}/cpp-intro/assignments/">Assignments</a></li>
      </ul>
      {% endif %}
    </li>
    <li>
      <a href="{{ site.baseurl }}/machine-learning/">Machine Learning</a>
      {% if page.url contains '/machine-learning/' %}
      <ul>
        <li><a href="{{ site.baseurl }}/machine-learning/setup/">Setup</a></li>
        <li><a href="{{ site.baseurl }}/machine-learning/fundamentals/">Fundamentals</a></li>
        <li><a href="{{ site.baseurl }}/machine-learning/projects/">Projects</a></li>
      </ul>
      {% endif %}
    </li>
    <li><a href="{{ site.baseurl }}/creative-robotics/">Creative Robotics</a></li>
    <li><a href="{{ site.baseurl }}/3d-animation/">3D Animation</a></li>
    <li><a href="{{ site.baseurl }}/game-development/">Game Development</a></li>
    <li><a href="{{ site.baseurl }}/web-development/">Web Development</a></li>
  </ul>
</nav>
"""
    create_file(os.path.join(base_dir, "_includes/navigation.html"), navigation_html)
    
    # Footer include
    footer_html = """<p>&copy; {{ 'now' | date: "%Y" }} Your Name / School Name. All rights reserved.</p>
"""
    create_file(os.path.join(base_dir, "_includes/footer.html"), footer_html)
    
    # Main landing page
    main_index = """---
title: Computer Science Courses
---

# Computer Science Course Materials

Welcome to the documentation site for our computer science curriculum. Here you'll find materials, guides, assignments, and resources for all courses.

## Courses

### [Introduction to C++]({{ site.baseurl }}/cpp-intro/)
A gentle introduction to modern C++ programming, focusing on a carefully selected subset of the language to build strong fundamentals.

### [Machine Learning]({{ site.baseurl }}/machine-learning/)
Explore the fundamentals of machine learning algorithms and their applications.

### [Creative Robotics]({{ site.baseurl }}/creative-robotics/)
Learn how to build and program Arduino-based robots for creative projects.

### [3D Rendering and Animation]({{ site.baseurl }}/3d-animation/)
Create stunning 3D models, animations, and renders using Blender.

### [Game Development]({{ site.baseurl }}/game-development/)
Design and program games using Unity and C#.

### [Web Application Development]({{ site.baseurl }}/web-development/)
Build interactive web applications with modern frontend and backend technologies.
"""
    create_file(os.path.join(base_dir, "index.md"), main_index)
    
    # Create course directories and index files
    courses = {
        "cpp-intro": {
            "title": "Introduction to C++",
            "description": """This course introduces modern C++ programming using a carefully selected subset of the language to build strong programming fundamentals.

## Course Approach

In this introductory class, we focus on:
- Modern C++ practices (C++23 features where appropriate)
- No use of pointers
- Custom Array<> class with helpful error messages
- print/println instead of cout
- Exclusive use of the string class (no char* style strings)

## Course Materials

- [Setup Guide]({{ site.baseurl }}/cpp-intro/setup/) - Setting up your development environment
- [C++ Fundamentals]({{ site.baseurl }}/cpp-intro/fundamentals/) - Core language concepts
- [Working with Arrays]({{ site.baseurl }}/cpp-intro/arrays/) - Using our Array<> class
- [Assignments]({{ site.baseurl }}/cpp-intro/assignments/) - Programming projects""",
            "subdirs": ["setup", "fundamentals", "arrays", "assignments"],
            "special_files": {
                "arrays/index.md": """---
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
"""
            }
        },
        "machine-learning": {
            "title": "Machine Learning",
            "description": """This course explores the fundamentals of machine learning algorithms and their practical applications.

## Course Overview

- Introduction to ML concepts and terminology
- Data preparation and feature engineering
- Supervised and unsupervised learning algorithms
- Model evaluation and improvement techniques

## Course Materials

- [Setup Guide]({{ site.baseurl }}/machine-learning/setup/) - Setting up your ML environment
- [Fundamentals]({{ site.baseurl }}/machine-learning/fundamentals/) - Core ML concepts
- [Projects]({{ site.baseurl }}/machine-learning/projects/) - Hands-on ML projects""",
            "subdirs": ["setup", "fundamentals", "projects"]
        },
        "creative-robotics": {
            "title": "Creative Robotics",
            "description": """This Arduino-based robotics course combines electronics, programming, and creativity.

## Course Overview

- Arduino programming fundamentals
- Electronics and circuit design
- Sensor integration and motor control
- Building creative interactive projects

## Course Materials

- [Setup Guide]({{ site.baseurl }}/creative-robotics/setup/) - Getting started with Arduino
- [Circuits]({{ site.baseurl }}/creative-robotics/circuits/) - Electronics basics
- [Programming]({{ site.baseurl }}/creative-robotics/programming/) - Arduino coding
- [Projects]({{ site.baseurl }}/creative-robotics/projects/) - Robotics project ideas""",
            "subdirs": ["setup", "circuits", "programming", "projects"]
        },
        "3d-animation": {
            "title": "3D Rendering and Animation",
            "description": """Learn to create stunning 3D models, animations, and renders using Blender.

## Course Overview

- 3D modeling techniques
- Animation principles and keyframing
- Material creation and texturing
- Lighting and rendering

## Course Materials

- [Basics]({{ site.baseurl }}/3d-animation/basics/) - Getting started with Blender
- [Modeling]({{ site.baseurl }}/3d-animation/modeling/) - 3D modeling techniques
- [Animation]({{ site.baseurl }}/3d-animation/animation/) - Creating movements and actions
- [Rendering]({{ site.baseurl }}/3d-animation/rendering/) - Final output creation""",
            "subdirs": ["basics", "modeling", "animation", "rendering"]
        },
        "game-development": {
            "title": "Game Development",
            "description": """Design and program games using Unity and C#.

## Course Overview

- Unity interface and workflow
- C# programming for games
- 2D and 3D game mechanics
- Game design principles

## Course Materials

- [Setup Guide]({{ site.baseurl }}/game-development/setup/) - Installing Unity
- [Basics]({{ site.baseurl }}/game-development/basics/) - Unity fundamentals
- [Scripting]({{ site.baseurl }}/game-development/scripting/) - C# for Unity
- [Projects]({{ site.baseurl }}/game-development/projects/) - Game project ideas""",
            "subdirs": ["setup", "basics", "scripting", "projects"]
        },
        "web-development": {
            "title": "Web Application Development",
            "description": """Build interactive web applications with modern frontend and backend technologies.

## Course Overview

- HTML, CSS and JavaScript fundamentals
- Frontend frameworks and libraries
- Backend development and API design
- Database integration

## Course Materials

- [Frontend]({{ site.baseurl }}/web-development/frontend/) - Client-side development
- [Backend]({{ site.baseurl }}/web-development/backend/) - Server-side programming
- [Databases]({{ site.baseurl }}/web-development/databases/) - Data persistence
- [Projects]({{ site.baseurl }}/web-development/projects/) - Web application projects""",
            "subdirs": ["frontend", "backend", "databases", "projects"]
        }
    }

    # Create course directories and files
    for course, details in courses.items():
        # Create course index
        course_index = f"""---
title: {details["title"]}
---

# {details["title"]}

{details["description"]}
"""
        create_file(os.path.join(base_dir, f"{course}/index.md"), course_index)
        
        # Create subdirectories with empty index files
        for subdir in details["subdirs"]:
            subdir_index = f"""---
title: {subdir.capitalize()}
---

# {subdir.capitalize()}

Content for {details["title"]} {subdir.capitalize()} section.
"""
            create_file(os.path.join(base_dir, f"{course}/{subdir}/index.md"), subdir_index)
        
        # Create any special files
        if "special_files" in details:
            for file_path, content in details["special_files"].items():
                create_file(os.path.join(base_dir, f"{course}/{file_path}"), content)

    print("\nSkeleton structure successfully created!")
    print(f"Files are located at: {os.path.abspath(base_dir)}")
    print("\nNext steps:")
    print("1. Initialize a Git repository in this directory (if not already done)")
    print("2. Commit all files to the repository")
    print("3. Push to GitHub")
    print("4. Enable GitHub Pages in repository settings (select /docs folder on main branch)")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        base_dir = sys.argv[1]
    else:
        base_dir = "docs"  # Default directory name
    
    create_skeleton(base_dir)
