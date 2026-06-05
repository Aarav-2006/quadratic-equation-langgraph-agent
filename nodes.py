import math

def parse_equation(state):

    return {
        "a": 1,
        "b": -5,
        "c": 6
    }


def calculate_discriminant(state):

    a = state["a"]
    b = state["b"]
    c = state["c"]

    discriminant = (b ** 2) - (4 * a * c)

    return {
        "discriminant": discriminant
    }


def no_real_roots(state):

    return {
        "result": "No Real Roots"
    }


def repeated_roots(state):

    a = state["a"]
    b = state["b"]

    root = -b / (2 * a)

    return {
        "result": f"Repeated Root: {root}"
    }


def distinct_roots(state):

    a = state["a"]
    b = state["b"]
    d = state["discriminant"]

    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)

    return {
        "result": f"Roots are {x1} and {x2}"
    }


def explain_solution(state):

    discriminant = state["discriminant"]
    result = state["result"]

    if discriminant > 0:
        explanation = (
            f"The discriminant is {discriminant}, which is positive. "
            f"This means the quadratic equation has two distinct real roots. "
            f"The solutions are {result.lower()}."
        )

    elif discriminant == 0:
        explanation = (
            f"The discriminant is {discriminant}, which means the equation has "
            f"one repeated real root. The solution is {result.lower()}."
        )

    else:
        explanation = (
            f"The discriminant is {discriminant}, which is negative. "
            f"This means the equation has no real roots."
        )

    return {
        "explanation": explanation
    }