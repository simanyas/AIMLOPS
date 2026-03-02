from transformers import pipeline
from typing import List
from mcp.server.fastmcp import FastMCP

# Load Sentiment Pipeline from HuggingFace
sentiment_pipeline = pipeline("sentiment-analysis")


# Create an MCP server
mcp = FastMCP("Second-MCP-Server")


#### Tool ####
# Tool to do sentiment analysis for a list of sentences
@mcp.tool()
def sentiment_analyzer(sentences: List[str]) -> List[dict]:
    """
    Analyzes the sentiment of a list of input sentences using a preloaded sentiment analysis pipeline.
    Args:
        sentences (List[str]): A list of input strings to be analyzed.
    Returns:
        List[dict]: A list of dictionaries, each containing:
            - 'text' (str): The original input sentence.
            - 'sentiment' (str): The predicted sentiment label (e.g., 'POSITIVE', 'NEGATIVE', etc.).
    
    Example:
        sentiment_analyzer(["I love this!", "This is terrible."])
        [{'text': 'I love this!', 'sentiment': 'POSITIVE'}, 
         {'text': 'This is terrible.', 'sentiment': 'NEGATIVE'}]
    """
    result = sentiment_pipeline(sentences)
    sentiments = []
    for i in range(len(sentences)):
        sentiments.append({'text': sentences[i], 
                           'sentiment': result[i]['label']})
    
    return sentiments


#### Prompt ####
@mcp.prompt()
def review_code(sentences: List[str]) -> str:
    return f"Analyze the sentiment of the following sentences:\n\n{sentences}"


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='sse')
