from langgraph.graph import StateGraph, START, END

from state import QuadraticState

from nodes import (
    parse_equation,
    calculate_discriminant,
    no_real_roots,
    repeated_roots,
    distinct_roots,
    explain_solution
)

from routers import route_discriminant


builder = StateGraph(QuadraticState)

builder.add_node(
    "parse_equation",
    parse_equation
)

builder.add_node(
    "calculate_discriminant",
    calculate_discriminant
)

builder.add_node(
    "no_real_roots",
    no_real_roots
)

builder.add_node(
    "repeated_root",
    repeated_roots
)

builder.add_node(
    "distinct_roots",
    distinct_roots
)
builder.add_node(
    "explain_solution",
    explain_solution
)


builder.add_edge(
    START,
    "parse_equation"
)

builder.add_edge(
    "parse_equation",
    "calculate_discriminant"
)

builder.add_conditional_edges(
    "calculate_discriminant",
    route_discriminant,
    {
        "negative": "no_real_roots",
        "zero": "repeated_root",
        "positive": "distinct_roots"
    }
)

builder.add_edge(
    "no_real_roots",
    "explain_solution"
)

builder.add_edge(
    "repeated_root",
    "explain_solution"
)

builder.add_edge(
    "distinct_roots",
    "explain_solution"
)

builder.add_edge(
    "explain_solution",
    END
)


graph = builder.compile()