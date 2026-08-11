from fastmcp import FastMCP

mcp = FastMCP("Restaurant")


@mcp.tool
def menu():
    """The food items provided by the restaurant."""
    food = ["biryani", "ice cream", "pizza"]
    return food


@mcp.tool
def locations():
    """The locations where the restaurant is available."""
    locations = ["Hyderabad", "Bangalore", "Mumbai", "Delhi"]
    return locations


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=5001
    )