import http

from fastmcp import FastMCP
import random

mcp = FastMCP(name="Test Remote Server")


@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return the sum."""
    return a + b


@mcp.tool()
def reverse_text(text: str) -> str:
    """Reverse a string and return it."""
    return text[::-1]

@mcp.tool()
def generate_random_number(min_val:int=1, max_val:int=100)-> int:
    """ Generate a random number between the min and max value
    """
    if min_val > max_val:
        raise ValueError("low must be <= high")
    return random.randint(min_val, max_val)


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
    