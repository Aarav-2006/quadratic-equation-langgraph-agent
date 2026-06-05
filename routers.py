def route_discriminant(state):

    d = state["discriminant"]

    if d < 0:
        return "negative"

    elif d == 0:
        return "zero"

    else:
        return "positive"
    