from graph import graph

result = graph.invoke(
    {
        "equation": "x^2 - 5x + 6 = 0"
    }
)

print("\nResult:")
print(result["result"])

print("\nExplanation:")
print(result["explanation"])