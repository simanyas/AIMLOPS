
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("First-MCP-Server")


#### Tools ####
# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print(f"Adding {a} and {b}")
    return a + b


# Another tool to count a letter in a word
@mcp.tool()
def letter_counter(word: str, letter: str) -> int:
    """Count the occurrences of a specific letter in a word.

    Args:
        word: The word or phrase to analyze
        letter: The letter to count occurrences of
        
    Returns:
        The number of times the letter appears in the word
    """
    output = word.lower().count(letter.lower())
    print(f"Count of {letter}: {output}")
    return output


#### Resources ####
# Add a static resource
@mcp.resource("resource://some_static_resource")
def get_static_resource() -> str:
    """Static resource data"""
    return "Any static data can be returned"


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


#### Prompts ####
@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"


@mcp.prompt()
def debug_error(error: str) -> list[tuple]:
    return [
        ("user", "I'm seeing this error:"),
        ("user", error),
        ("assistant", "I'll help debug that. What have you tried so far?"),
    ]


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
