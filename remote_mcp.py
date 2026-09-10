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

# Export the FastMCP instance as a FastAPI app for cloud deployment.
# The platform will run the app with uvicorn automatically.
app = mcp