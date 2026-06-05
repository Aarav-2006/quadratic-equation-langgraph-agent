# Quadratic Equation LangGraph Agent

A simple AI-powered workflow built using LangGraph and Google Gemini to solve quadratic equations through a conditional graph architecture.

This project demonstrates the core concepts of LangGraph, including:

- State Management
- Nodes
- Edges
- Conditional Routing
- Graph Execution
- LLM Integration
- Deterministic Workflows

---

## Architecture

```text
START
  |
  v
parse_equation
  |
  v
calculate_discriminant
  |
  v
route_discriminant
  |
  +-------- negative --------> no_real_roots
  |
  +---------- zero ----------> repeated_root
  |
  +-------- positive --------> distinct_roots
                                   |
                                   v
                           explain_solution
                                   |
                                   v
                                  END
```

---

## Project Structure

```text
quadratic-equation-langgraph-agent/
│
├── main.py
├── graph.py
├── state.py
├── nodes.py
├── routers.py
├── config.py
├── .env
├── .gitignore
└── README.md
```

---

## Workflow Overview

The application accepts a quadratic equation and processes it through a LangGraph workflow.

### Example Input

```text
x² - 5x + 6 = 0
```

### Workflow Steps

#### 1. Parse Equation

Extracts the coefficients:

```text
a = 1
b = -5
c = 6
```

#### 2. Calculate Discriminant

Uses the quadratic discriminant formula:

```text
d = b² - 4ac
```

For the example:

```text
d = (-5)² - 4(1)(6)
d = 25 - 24
d = 1
```

#### 3. Conditional Routing

Based on the discriminant value:

```text
d < 0  → No Real Roots

d = 0  → Repeated Root

d > 0  → Two Distinct Real Roots
```

#### 4. Solve Equation

The appropriate node calculates the final result.

#### 5. Generate Explanation

Produces a human-readable explanation of the solution.

---

## State Management

LangGraph uses a shared state object that is passed between all nodes.

### State Schema

```python
from typing import TypedDict

class QuadraticState(TypedDict):
    equation: str

    a: float
    b: float
    c: float

    discriminant: float

    result: str
    explanation: str
```

### State Evolution

Initial State:

```python
{
    "equation": "x^2 - 5x + 6 = 0"
}
```

After Parsing:

```python
{
    "equation": "x^2 - 5x + 6 = 0",
    "a": 1,
    "b": -5,
    "c": 6
}
```

After Discriminant Calculation:

```python
{
    "equation": "x^2 - 5x + 6 = 0",
    "a": 1,
    "b": -5,
    "c": 6,
    "discriminant": 1
}
```

Final State:

```python
{
    "equation": "x^2 - 5x + 6 = 0",
    "a": 1,
    "b": -5,
    "c": 6,
    "discriminant": 1,
    "result": "Roots are 3.0 and 2.0",
    "explanation": "The discriminant is positive, meaning the equation has two distinct real roots."
}
```

---

## Nodes

### parse_equation

Extracts the coefficients of the quadratic equation.

Input:

```text
x² - 5x + 6 = 0
```

Output:

```python
{
    "a": 1,
    "b": -5,
    "c": 6
}
```

---

### calculate_discriminant

Calculates:

```text
d = b² - 4ac
```

Output:

```python
{
    "discriminant": 1
}
```

---

### no_real_roots

Executed when:

```text
d < 0
```

Output:

```python
{
    "result": "No Real Roots"
}
```

---

### repeated_root

Executed when:

```text
d = 0
```

Output:

```python
{
    "result": "Repeated Root: x"
}
```

---

### distinct_roots

Executed when:

```text
d > 0
```

Uses the quadratic formula to compute:

```text
x₁ = (-b + √d)/(2a)
x₂ = (-b - √d)/(2a)
```

Output:

```python
{
    "result": "Roots are 3.0 and 2.0"
}
```

---

### explain_solution

Generates a human-readable explanation of the solution path and result.

---

## Conditional Routing

The routing logic is implemented using LangGraph conditional edges.

```python
builder.add_conditional_edges(
    "calculate_discriminant",
    route_discriminant,
    {
        "negative": "no_real_roots",
        "zero": "repeated_root",
        "positive": "distinct_roots"
    }
)
```

### Router Logic

```python
def route_discriminant(state):

    d = state["discriminant"]

    if d < 0:
        return "negative"

    elif d == 0:
        return "zero"

    return "positive"
```

This dynamically determines which node executes next.

---

## Technologies Used

- Python
- LangGraph
- LangChain
- Google Gemini
- TypedDict

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/quadratic-equation-langgraph-agent.git
```

Navigate into the project:

```bash
cd quadratic-equation-langgraph-agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Execute:

```bash
python main.py
```

Example Output:

```text
Result:
Roots are 3.0 and 2.0

Explanation:
The discriminant is 1, which is positive. This means the quadratic equation has two distinct real roots. The solutions are 3.0 and 2.0.
```

---

## Key Concepts Demonstrated

- LangGraph State Management
- Node-Based Workflows
- Conditional Graph Routing
- Deterministic Processing
- LLM Integration
- Graph Compilation
- Graph Execution

---

## Future Improvements

- Support natural language equation input
- Structured Gemini outputs using Pydantic
- Graph visualization generation
- Streaming execution
- Checkpointing and memory
- Support for linear and cubic equations
- Multi-agent math tutor architecture

---

## Learning Outcomes

This project was built to understand the fundamental building blocks of LangGraph:

- States
- Nodes
- Edges
- Conditional Edges
- Graph Compilation
- Graph Invocation

It serves as a foundation for building more advanced systems such as RAG pipelines, research agents, and multi-agent workflows.
