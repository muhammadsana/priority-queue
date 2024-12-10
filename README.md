# Priority Queue Project

This project provides a **Priority Queue** implementation in Python, supporting standard operations such as adding elements with priorities, retrieving the highest-priority element, and inspecting the queue. It includes comprehensive testing, including unit tests, property-based testing, and mutation testing, to ensure robustness and reliability.

---

## Features
- **Push**: Add items to the priority queue with a specified priority.
- **Pop**: Retrieve and remove the highest-priority item.
- **Peek**: Inspect the highest-priority item without removing it.
- **Is Empty**: Check if the queue is empty.
- **Size**: Get the number of elements in the queue.

---

## Project Structure
```plaintext
priority-queue-project/
├── src/
│   └── priority_queue.py          # Source code for the Priority Queue
├── tests/
│   ├── test_priority_queue.py     # Unit tests for Priority Queue
│   └── mutation_tests.py          # Mutation testing scripts
├── requirements.txt               # List of Python dependencies
├── .gitignore                     # Files and directories to ignore in Git
├── README.md                      # Documentation for the project
└── run_tests.sh                   # Shell script to run all tests and coverage
```

---

## Prerequisites
Ensure you have Python 3.8 or higher installed. You will also need `pip` to install dependencies.

---

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd priority-queue-project
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Priority Queue API
You can use the `PriorityQueue` class in your Python code:
```python
from src.priority_queue import PriorityQueue

pq = PriorityQueue()
pq.push("Task1", priority=2)
pq.push("Task2", priority=1)
pq.push("Task3", priority=3)

print(pq.pop())  # Output: Task3
print(pq.peek())  # Output: Task1
print(pq.size())  # Output: 2
```

---

## Running Tests

### 1. Run Unit Tests
To verify the functionality of the `PriorityQueue`:
```bash
python -m unittest discover tests
```

### 2. Generate Coverage Report
To measure code coverage:
```bash
coverage run -m unittest discover tests
coverage report -m
```

### 3. Run Mutation Tests
To test the robustness of the code by injecting intentional mutations:
```bash
python tests/mutation_tests.py
```
Additional Notes
The project uses hypothesis for property-based testing and unittest for unit tests.
Mutation testing simulates possible bugs and verifies if the current tests can catch them.
You can enhance the mutation tests using external tools like MutPy.

---
