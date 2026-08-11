from fastmcp import FastMCP

mcp = FastMCP('Restaurent')

@mcp.tool
def menu():
    """The Food items provided by restaurent"""
    food = ['biryani','ice cream','pizza']
    return food

@mcp.tool
def locations():
    """The locations where restaurent is available"""
    locations=['Hyderabad','Banglore','Mumbai','Delhi']
    return locations

if __name__ == '__main__':
    mcp.run(transport='streamable-http',port= 5001,host='0,0.0.0')