from fastmcp import FastMCP
mcp = FastMCP(name="Remote Server")

@mcp.tool
def add_numbers(a : float, b : float) -> float:
    """ Add two numbers """
    return a + b

@mcp.tool
def substract_number(a : float, b : float) -> float:
    """ substract one number from another """
    return a - b

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)