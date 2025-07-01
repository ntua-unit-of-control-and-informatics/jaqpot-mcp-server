"""Example usage of the Jaqpot MCP Server with a client."""

import asyncio
import os
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client


async def main():
    """Example of how to use the Jaqpot MCP server."""
    
    # Set environment variables (in production, these should be set in your environment)
    os.environ["JAQPOT_API_KEY"] = "your-api-key-here"
    os.environ["JAQPOT_API_SECRET"] = "your-api-secret-here"
    
    # Start the server process
    server_process = await asyncio.create_subprocess_exec(
        "python", "-m", "jaqpot_mcp_server",
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    
    try:
        # Connect to the server
        async with stdio_client(server_process) as (read, write):
            async with ClientSession(read, write) as session:
                
                # Initialize the session
                await session.initialize()
                
                # List available tools
                tools_result = await session.list_tools()
                print("Available tools:")
                for tool in tools_result.tools:
                    print(f"- {tool.name}: {tool.description}")
                
                # Example 1: Get model information
                print("\\n=== Getting model info for model ID 1 ===")
                model_info_result = await session.call_tool(
                    "jaqpot_get_model_info",
                    {"model_id": 1}
                )
                print(f"Model info: {model_info_result.content}")
                
                # Example 2: Get model summary
                print("\\n=== Getting model summary for model ID 1 ===")
                model_summary_result = await session.call_tool(
                    "jaqpot_get_model_summary",
                    {"model_id": 1}
                )
                print(f"Model summary: {model_summary_result.content}")
                
                # Example 3: Search for models
                print("\\n=== Searching for models ===")
                search_result = await session.call_tool(
                    "jaqpot_search_models",
                    {"page": 0, "size": 5}
                )
                print(f"Search results: {search_result.content}")
                
                # Example 4: Make a prediction (adjust based on your model's input format)
                print("\\n=== Making a prediction ===")
                sample_data = [
                    {
                        "feature1": 1.0,
                        "feature2": 2.0,
                        "feature3": 3.0
                    }
                ]
                
                prediction_result = await session.call_tool(
                    "jaqpot_predict",
                    {
                        "model_id": 1,
                        "dataset": sample_data
                    }
                )
                print(f"Prediction result: {prediction_result.content}")
                
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Clean up the server process
        server_process.terminate()
        await server_process.wait()


if __name__ == "__main__":
    asyncio.run(main())