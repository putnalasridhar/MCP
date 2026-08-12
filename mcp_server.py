from fastmcp import FastMCP

mcp = FastMCP(name="travel Agent")


@mcp.tool
def get_weather():
    """Weather of given location"""
    return {
        "location": "Hyderabad",
        "weather": "Sunny",
        "temperature": 30
    }


@mcp.tool
def add(a: int, b: int):
    """Addition of two numbers"""
    return a + b


@mcp.tool
def get_flights():
    """The flights from Hyderabad to Mumbai on 2022-12-31"""
    return {
        "Departure": "Hyderabad",
        "Arrival": "Mumbhai",
        "price": 5000,
        "available_seats": 50
    }


@mcp.tool
def get_hotels():
    """The hotels in Hyderabad"""
    return {
        "hotel": "Taj Hotel",
        "price": 10000,
        "available_rooms": 50
    }


@mcp.tool
def get_date():
    """Date of flight"""
    return {
        "date": "2022-12-31"
    }


if __name__ == "__main__":
    mcp.run()